resource "azurerm_resource_group" "jenkins" {
  name     = local.resourceName
  location = var.location
  tags = {
    Name = var.name
  }
}

module "vnet" {
  source              = "./modules/vnet"
  location            = var.location
  vnet_name           = "local.vnet_name"
  subnet_name         = "Default"
  address_space       = "10.10.0.0/16"
  address_prefixes    = "10.10.86.0/24"
  resource_group_name = azurerm_resource_group.jenkins.name
}

resource "azurerm_network_security_group" "jenkins" {
  name                = local.resourceName
  location            = var.location
  resource_group_name = azurerm_resource_group.jenkins.name
}

resource "azurerm_network_security_rule" "jenkins" {
  for_each                    = toset(var.ports)
  name                        = each.value
  priority                    = index(var.ports, each.value) + 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = each.value
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.jenkins.name
  network_security_group_name = azurerm_network_security_group.jenkins.name
}


resource "azurerm_storage_account" "jenkins" {
  name                     = var.storage_name
  location                 = var.location
  resource_group_name      = azurerm_resource_group.jenkins.name
  account_tier             = "Standard"
  account_replication_type = "GRS"
  tags = {
    Name = var.name
  }
}

resource "azurerm_storage_share" "jenkins" {
  name                 = var.storage_name
  storage_account_name = azurerm_storage_account.jenkins.name
  quota                = var.file_share_quota
}

module "ssh" {
  source      = "./modules/ssh"
  private-key = "C:/Users/smuruges/Documents/Terraform/genesys-terraform-dec-2021/terraform/azure_suren-private-key.pem"
}

resource "azurerm_linux_virtual_machine_scale_set" "jenkins" {
  name                = "${local.resourceName}-vm"
  resource_group_name = azurerm_resource_group.jenkins.name
  location            = var.location
  sku                 = "Standard_B1s"
  instances           = 2
  admin_username      = "suren"

  admin_ssh_key {
    username   = "suren"
    public_key = module.ssh.public-key
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  os_disk {
    storage_account_type = "Standard_LRS"
    caching              = "ReadWrite"
  }

  network_interface {
    name    = var.name
    primary = true
    ip_configuration {
      name                                   = "internal"
      primary                                = true
      subnet_id                              = module.vnet.subnet_id
      load_balancer_backend_address_pool_ids = [azurerm_lb_backend_address_pool.jenkins.id]
      load_balancer_inbound_nat_rules_ids    = [azurerm_lb_nat_pool.jenkins.id, azurerm_lb_nat_pool.ssh.id]
    }
  }
}

resource "null_resource" "setup_jenkins" {
  depends_on = [
    azurerm_linux_virtual_machine_scale_set.jenkins
  ]
  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      user        = "suren"
      private_key = module.ssh.private-key
      host        = azurerm_public_ip.pip.ip_address
    }
    inline = [
      "sudo apt-get update -y && sudo apt-get install -y default-jre nodejs npm && sudo npm install -f forever",
      "wget https://get.jenkins.io/war/2.324/jenkins.war"
      #"forever start -c java -jar jenkins.war"
    ]
  }
}


