variable "name" {
  description = "Enter the name to be added with different resource names"
  type        = string
  default     = "jenkins"
}

variable "storage_name" {
  type    = string
  default = "surenstorage"
}

variable "location" {
  description = "Location for creating resources"
  default     = "East US"
}

variable "ports" {
  default = ["8080", "22"]
}

variable "file_share_quota" {
  default = 5
}