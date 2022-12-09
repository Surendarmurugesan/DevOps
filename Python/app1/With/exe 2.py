with open("file.txt", 'r') as file:
    content = file.read()

print(type(content))
print(content)
print(len(content))

# If you want to get all the text as one single string, use read().
# If you want to get separate strings for each line as List, use readlines().