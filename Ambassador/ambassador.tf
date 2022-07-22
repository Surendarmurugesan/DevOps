resource "kubernetes_manifest" "mapping" {
  manifest = {
    apiVersion = "getambassador.io/v3alpha1"
    kind       = "Mapping"
    metadata = {
      name      = "designer-ambassador"
      namespace = var.namespace
      labels    = local.labels
    }
    spec = {
        service    = "http://designer-${var.ambassadorProdColor}.designer:8888"
        prefix     = "/"
        hostname   = "example.api01-${local.location}.${local.environment}.gcp.com"
        timeout_ms = "120000"
      }
  }
}

# Mapping for Designer Blue Service
resource "kubernetes_manifest" "mapping-blue" {
  manifest = {
    apiVersion = "getambassador.io/v3alpha1"
    kind       = "Mapping"
    metadata = {
      name      = "designer-ambassador-blue"
      namespace = var.namespace
      labels    = local.labels
    }
    spec = {
        service    = "http://designer-blue.designer:8888"
        prefix     = "/"
        hostname   = "designer-blue.api01-${local.location}.${local.environment}.gengcp.com"
        timeout_ms = "120000"
      }
  }
}

# Mapping for Designer Green Service
resource "kubernetes_manifest" "mapping-green" {
  manifest = {
    apiVersion = "getambassador.io/v3alpha1"
    kind       = "Mapping"
    metadata = {
      name      = "designer-ambassador-green"
      namespace = var.namespace
      labels    = local.labels
    }
    spec = {
        service    = "http://designer-green.designer:8888"
        prefix     = "/"
        hostname   = "designer-green.api01-${local.location}.${local.environment}.gengcp.com"
        timeout_ms = "120000"
      }
  }
}