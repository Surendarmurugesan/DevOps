# Creating modules for ssh-key generation

resource "tls_private_key" "private-key" {
    algorithm = "RSA"
    rsa_bits = "2048"
}

resource "local_file" "private-key" {
  filename = var.private-key
  content = tls_private_key.private-key.private_key_pem
}