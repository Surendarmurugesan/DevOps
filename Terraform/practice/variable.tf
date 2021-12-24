variable "file_path" {
  type = string
  description = "Here are the file location"
  default = "./sample.txt"
}

variable "file_content" {
  type = string
  description = "Here are the file content"
  default = "sample data storage"
}

variable "prefix" {
  type = list (number)
  default = [1,4]
}

variable "set" {
  type = set (string)
  default = [ "apple", "banana", "apple"]
}