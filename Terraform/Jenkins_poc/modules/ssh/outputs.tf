output "public-key" {
  value = tls_private_key.private-key.public_key_openssh
}

output "private-key" {
  value = tls_private_key.private-key.private_key_pem
}