provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
  client_id       = "516ef891-8458-4154-abc8-1ca310bd3ccc"
  client_secret   = "P.q7Q~bgSbY.EaiydC5PkzNVqIs_1Bnbeqj3n"
  subscription_id = "312b69f3-480b-46a3-afd6-ae7c053ab0ae"
  tenant_id       = "af1b6ff7-ddf1-4bd1-acf5-5b432a4c65c0"
}

#Generating  private key to be used VM's
provider "tls" {}

#provider to interact with resources
provider "null" {}

#To work with local
provider "local" {}