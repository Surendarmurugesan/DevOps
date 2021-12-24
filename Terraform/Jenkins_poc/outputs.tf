output "subnet_id" {
  value = module.vnet.subnet_id
}

output "nsg_name" {
  value = azurerm_network_security_group.jenkins.name
}

output "jenkins-url" {
  value = "http://${azurerm_public_ip.pip.ip_address}:8080"
}