resource "azurerm_resource_group" "Surendar" {
  name     = "Surendar"
  location = "East US"
  tags = {
    Name = "Surendar"
    Day  = "1"
  }
}

resource "azurerm_virtual_network" "vnet" {
  name          = "suren-vnet"
  address_space = ["10.10.0.0/16"]
  # Referencing the values from resources created in the workspace
  resource_group_name = azurerm_resource_group.Surendar.name
  location            = azurerm_resource_group.Surendar.location
}

resource "azurerm_subnet" "subnet-1" {
  name                 = "suren-subnet-1"
  resource_group_name  = azurerm_resource_group.Surendar.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.10.86.0/24"]
}

resource "azurerm_public_ip" "pip" {
  resource_group_name = azurerm_resource_group.Surendar.name
  location            = azurerm_resource_group.Surendar.location
  name                = "suren-ip"
  sku                 = "Basic"
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "nic" {
  resource_group_name = azurerm_resource_group.Surendar.name
  location            = azurerm_resource_group.Surendar.location
  name                = "suren-nic"
  ip_configuration {
    name                          = "suren"
    subnet_id                     = azurerm_subnet.subnet-1.id
    public_ip_address_id          = azurerm_public_ip.pip.id
    private_ip_address_allocation = "Dynamic"
  }
}

#Creating Linux Virtual Machine
resource "azurerm_linux_virtual_machine" "vm" {
  resource_group_name = azurerm_resource_group.Surendar.name
  location            = azurerm_resource_group.Surendar.location
  name                = "suren-vm"
  size                = "Standard_B1s"
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
  admin_username = "suren"
  admin_ssh_key {
    username   = "suren"
    public_key = tls_private_key.private-key.public_key_openssh
  }
  os_disk {
    name                 = "suren-disk"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  tags = {
    "Name" = "suren"
    "Day"  = "1"
  }
  network_interface_ids = [azurerm_network_interface.nic.id]
}

# Adding null_resource to install apache2 on the already created VM's.
# Block to perform certain actions post resource creation, there are three types of provisioner, remote-exec, local-exec, file (copy files or folder from local to remote server)
resource "null_resource" "install_apache2" {
  provisioner "remote-exec" {
    # Connection detail to connect with the remote host
    connection {
      type        = "ssh"
      user        = azurerm_linux_virtual_machine.vm.admin_username
      private_key = tls_private_key.private-key.private_key_pem
      host        = azurerm_linux_virtual_machine.vm.public_ip_address
    }
    # Define commands to be triggered on the remote machie
    inline = [
      "sudo apt-get update -y && sudo apt-get install -y apache2",
      "curl localhost:80"
    ]
  }
}