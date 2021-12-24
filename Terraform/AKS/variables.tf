variable "location" {
  default = "East US"
}

variable "name" {
  default = "Suren"
}
variable "subname" {
  default = "suren"
}

variable "resource" {
  default = "aks"
}

locals {
  resourceName = "${var.name}-${var.resource}"
}

variable "client_secret" {
  default = "P.q7Q~bgSbY.EaiydC5PkzNVqIs_1Bnbeqj3n"
}
variable "client_id" {
  default = "516ef891-8458-4154-abc8-1ca310bd3ccc"
}