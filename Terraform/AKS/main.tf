terraform {
  # This block helps in maintaining terraform statefile on azure Storage Containers instead of managing it in local workspace
  backend "azurerm" {
    resource_group_name  = "remote-tf-state"
    storage_account_name = "tfststatekul"
    container_name       = "tfstates"
    key                  = "suren.tfstate"
  }
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
  # client_id       = "516ef891-8458-4154-abc8-1ca310bd3ccc"
  # client_secret   = "P.q7Q~bgSbY.EaiydC5PkzNVqIs_1Bnbeqj3n"
  # subscription_id = "312b69f3-480b-46a3-afd6-ae7c053ab0ae"
  # tenant_id       = "af1b6ff7-ddf1-4bd1-acf5-5b432a4c65c0"
}

#To work with local
provider "local" {}

# Resource Group
resource "azurerm_resource_group" "aks" {
  name     = local.resourceName
  location = var.location
  tags = {
    Name = var.name
  }
}

resource "azurerm_kubernetes_cluster" "aks" {
  name                = local.resourceName
  location            = var.location
  resource_group_name = azurerm_resource_group.aks.name
  dns_prefix          = local.resourceName

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  service_principal {
    client_id     = var.client_id
    client_secret = var.client_secret
  }

  addon_profile {
    oms_agent {
      enabled = true
      log_analytics_workspace_id = azurerm_log_analytics_workspace.aks.id
    }
  }

  tags = {
    Name = local.resourceName
  }
}

provider "null" {}

# Configure the kube_config in Local
resource "null_resource" "download_kube_config" {
provisioner "local-exec" {
command = "echo '${azurerm_kubernetes_cluster.aks.kube_config_raw}' > C:/Users/smuruges/.kube/config"
interpreter = ["powershell", "-Command"]
}
}

# Creating Namespace & Service resources in AKS created above using kubernetes provider.

# kubernetes blocks
provider "kubernetes" {
  config_path = "C:/Users/smuruges/.kube/config"
  config_context = local.resourceName
}

resource "kubernetes_namespace" "aks" {
  depends_on = [
    null_resource.download_kube_config
  ]
  metadata {
    name = var.subname
  }
}

resource "kubernetes_service" "aks" {
  metadata {
    name = var.subname
    namespace = kubernetes_namespace.aks.metadata.0.name
  }
  spec {
    selector = {
      app = var.subname
    }
    session_affinity = "ClientIP"
    port {
      port        = 80
      target_port = 80
    }
    type = "LoadBalancer"
  }
}

resource "kubernetes_deployment" "aks" {
  metadata {
    name = "${var.subname}-deploy"
    namespace = kubernetes_namespace.aks.metadata.0.name
    labels = {
      app = var.subname
    }
  }
  
  spec {
    replicas = 2

    selector {
      match_labels = {
        app = var.subname
      }
    }

    template {
      metadata {
        labels = {
          app = var.subname
        }
      }

      spec {
        container {
          image = "nginx:latest"
          name  = "${var.subname}-pod"
        }
      }
    }
  }
}

resource "azurerm_log_analytics_workspace" "aks" {
  name                = local.resourceName
  location            = var.location
  resource_group_name = azurerm_resource_group.aks.name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}