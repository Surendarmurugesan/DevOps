variable "name" {
  description = "Base name of CRD resources"
  default     = "designer-ambassador"
}

variable "namespace" {
  description = "Namespace to create resources in"
  default     = "designer"
}

variable "mapping_labels" {
  description = "Labels for mapping"
  default = {
    "service"     = "designer"
    "servicename" = "designer"
    "tenant"      = "shared"
  }
}

variable "service" {
  description = "Name of the service to map the host to, using the specified resolver"
  type        = string
  default     = "http://designer-green.designer:8888"
}

variable "prefix" {
  description = "Path prefix for the mapping"
  default     = "/"
}

variable "hostname" {
  description = "Hostname for the designer"
  type        = string
  default     = "designer.api01-uswest2.dev.gengcp.com"
}

variable "timeout_ms" {
  description = "timeout_ms for the mapping"
  default     = "50000"
}