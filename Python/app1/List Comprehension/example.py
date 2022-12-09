filenames = ["1.doc", "2.repo", "3.bucket"]

file_list = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(file_list)


# Expected output:
# ['1-doc.txt', '2-repo.txt', '3-bucket.txt']