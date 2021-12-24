# Printing important information on the screen/console
# terraform output # could be post to get the info about outputs defined in terraform files later on after apply is done
output "vm_ip" {
  value = azurerm_linux_virtual_machine.vm.public_ip_address
}

output "apache_link" {
  value = "http://${azurerm_linux_virtual_machine.vm.public_ip_address}:80"
}

output "vm_username" {
  value = azurerm_linux_virtual_machine.vm.admin_username
}