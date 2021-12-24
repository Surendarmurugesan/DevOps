resource "azurerm_virtual_network" "vnet" {
    name = var.vnet_name
    location = var.location
    resource_group_name = var.resource_group_name
    address_space = [ var.address_space ]
}

resource "azurerm_subnet" "subnet-1" {
    name = var.subnet_name
    resource_group_name = var.resource_group_name
    virtual_network_name = azurerm_virtual_network.vnet.name
    address_prefixes = [ var.address_prefixes ]  
}