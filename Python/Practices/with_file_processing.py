with open("file.txt", "w") as myfile:
    myfile.write("snail")


# Create first.txt file that contains the first 90 characters of bear.txt.
with open("bear.txt", "r") as myfile:
    content = myfile.read()
    
with open("first.txt", "w") as file:
    file.write(content[:90])