# Creating Azure Vault and pushing private key generated to the same.resource 

data "azurerm_client_config" "current" {}
resource "azurerm_key_vault" "key_vault" {
  name                        = "suren-key-vault"
  location                    = azurerm_resource_group.Surendar.location
  resource_group_name         = azurerm_resource_group.Surendar.name
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  sku_name                    = "standard"

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    key_permissions = [
      "Get",
    ]
    secret_permissions = [
      "backup",
      "delete",
      "get",
      "list",
      "purge",
      "recover",
      "restore",
      "set"
    ]

    storage_permissions = [
      "Get",
    ]
  }
}

resource "azurerm_key_vault_secret" "secret-private-key" {
  name         = "${azurerm_linux_virtual_machine.vm.name}-${azurerm_linux_virtual_machine.vm.admin_username}-private-key"
  value        = tls_private_key.private-key.private_key_pem
  key_vault_id = azurerm_key_vault.key_vault.id
  tags = {
    server-name = azurerm_linux_virtual_machine.vm.name
    admin_user  = azurerm_linux_virtual_machine.vm.admin_username
  }
}