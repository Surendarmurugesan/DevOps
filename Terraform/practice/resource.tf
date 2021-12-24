resource "local_file" "sample" {
    filename = var.file_path
    content =  var.file_content
}