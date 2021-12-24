resource "azurerm_public_ip" "pip" {
  name                = "${local.resourceName}-public-ip"
  location            = var.location
  resource_group_name = azurerm_resource_group.jenkins.name
  allocation_method   = "Static"
}

resource "azurerm_lb" "lb" {
  name                = "${local.resourceName}-elb"
  location            = var.location
  resource_group_name = azurerm_resource_group.jenkins.name
  frontend_ip_configuration {
    name                 = var.name
    public_ip_address_id = azurerm_public_ip.pip.id
  }
}

resource "azurerm_lb_backend_address_pool" "jenkins" {
  loadbalancer_id = azurerm_lb.lb.id
  name            = var.name
}

resource "azurerm_lb_nat_pool" "jenkins" {
  resource_group_name            = azurerm_resource_group.jenkins.name
  loadbalancer_id                = azurerm_lb.lb.id
  name                           = local.resourceName
  protocol                       = "Tcp"
  frontend_port_start            = 8080
  frontend_port_end              = 8090
  backend_port                   = 8080
  frontend_ip_configuration_name = var.name
}
resource "azurerm_lb_nat_pool" "ssh" {
  resource_group_name            = azurerm_resource_group.jenkins.name
  loadbalancer_id                = azurerm_lb.lb.id
  name                           = "ssh"
  protocol                       = "Tcp"
  frontend_port_start            = 22
  frontend_port_end              = 28
  backend_port                   = 22
  frontend_ip_configuration_name = var.name
}

