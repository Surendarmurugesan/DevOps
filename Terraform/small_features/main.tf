terraform {
    backend "azurerm" {
    resource_group_name = "remote-tf-state"
    storage_account_name = "tfststatekul"
    container_name = "tfstates"
    key = "suren_sf.tfstate"
  }
}
provider "azurerm" {
  features {
  }
}
variable "location" {
  default = "East US"
}
variable "name" {
  default = "suren"
}
variable "resource" {
  default = "sf"
}
locals {
  resourceName = "${var.name}-${var.resource}-${terraform.workspace}"
}
resource "azurerm_resource_group" "sf" {
  name = local.resourceName
  location = var.location
  tags = {
    "Name" = local.resourceName
  }
}
module "vnet" {
  source = "./modules/vnet"
  location = var.location
  vnet_name = local.resourceName
  subnet_name = "Default"
  address_space = "10.10.0.0/16"
  address_prefixes = "10.10.86.0/24"
  resource_group_name = azurerm_resource_group.sf.name
}
resource "azurerm_network_security_group" "sf" {
  name = local.resourceName
  location = var.location
  resource_group_name = azurerm_resource_group.sf.name
}
variable "ports" {
  default = ["22","8080"]
}
resource "azurerm_network_security_rule" "sf" {
  for_each = toset(var.ports)
  name                        = each.value
  priority                    = "${index(var.ports, each.value) + 100}"
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = each.value
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.sf.name
  network_security_group_name = azurerm_network_security_group.sf.name
}
variable "private-key" {
  default = "C:/Users/smuruges/Documents/Terraform/genesys-terraform-dec-2021/small_features/private_key.pem"
}
resource "tls_private_key" "private-key" {
  algorithm = "RSA"
  rsa_bits = "2048"
}
resource "local_file" "private-key" {
  filename = var.private-key
  content = tls_private_key.private-key.private_key_pem
}

resource "azurerm_public_ip" "sf" {
  resource_group_name = azurerm_resource_group.sf.name
  location = var.location
  sku = "Basic"
  allocation_method = "Dynamic"
  name = local.resourceName
}

resource "azurerm_network_interface" "sf" {
  resource_group_name = azurerm_resource_group.sf.name
  location = var.location
  name = "suren-nic"
  ip_configuration {
    name = "suren"
    subnet_id = module.vnet.subnet_id
    public_ip_address_id = azurerm_public_ip.sf.id
    private_ip_address_allocation = "Dynamic"
  }
}
variable "admin_username" {
  default = "suren"
}
resource "azurerm_linux_virtual_machine" "server" {
  resource_group_name = azurerm_resource_group.sf.name
  location = var.location
  name = local.resourceName
  size = "Standard_B1s"
  source_image_reference {
    publisher = "Canonical"
    offer = "UbuntuServer"
    sku = "18.04-LTS"
    version = "latest"
  }
  admin_username = var.admin_username
  admin_ssh_key {
    username = var.admin_username
    public_key = tls_private_key.private-key.public_key_openssh
  }
  os_disk {
    name = local.resourceName
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  tags = {
    "Name" = local.resourceName
  }
  network_interface_ids = [ azurerm_network_interface.sf.id ]
}

# File Provisioner to copy files or folder from local to remote
resource "null_resource" "file_provisioner" {
  provisioner "file" {
    connection {
      type = "ssh"
      user = var.admin_username
      private_key = tls_private_key.private-key.private_key_pem
      host = azurerm_linux_virtual_machine.server.public_ip_address
    }
    source = "main.tf"
    destination = "main.tf"
  }
}

output "vm_ip" {
  value = azurerm_linux_virtual_machine.server.public_ip_address
}


# Conditional Expressions
variable "high_availability" {
  type = bool
  default = false
}

resource "azurerm_public_ip" "sf-ce" {
  count = var.high_availability ? 2 : 1
  resource_group_name = azurerm_resource_group.sf.name
  location = var.location
  sku = "Basic"
  allocation_method = "Dynamic"
  name = "${local.resourceName}-${count.index}"
}

variable "csv" {
  default = "ets-1,ets-2,ets-3,etc-1,etc-2,etc-3"
}

locals {
  components = split(",",var.csv)
}

resource "azurerm_public_ip" "sf-sf" {
  for_each = toset(local.components)
  resource_group_name = azurerm_resource_group.sf.name
  location = var.location
  sku = "Basic"
  allocation_method = "Dynamic"
  name = "${local.resourceName}-${each.value}"
}

