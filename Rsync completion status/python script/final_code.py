import os
# Declaring Variables Used
ip = [] 
error = []
ip_error = []
ip_count = {}
error_count = {}
ip_error_count = {}


path = r"C:/Users/ibasha/Desktop/python proj/logs"
list = os.listdir(path)
print(list)
file_path = input('Please Enter Date in "DDMM" Format: ')
global name
for name in os.listdir(path + '/' + file_path):
    print(path + '/' +file_path + '/' + name)
    myfile = open(path + '/' + file_path + '/' + name,"r")
    global content
    content = myfile.readlines()
    myfile.close()

# Splitting the data based on white spaces
for each_line in content:
    splitdata = each_line.split(' ')
    ip.append(splitdata[3])
    error.append(splitdata[8])
    ip_error.append(str(splitdata[3])+' '+str(splitdata[8]))


# Counting the IP's
if os.path.exists("output.txt"):
    os.remove("output.txt")
    print("file deleted")
for item in ip:
    if item.split(":")[0] in ip_count:
        ip_count[item.split(":")[0]] += 1
    else:
        ip_count[item.split(":")[0]] = 1
f = open("output.txt", "a")
f.write("Printing the IPs in the log files\n")
for i,j in ip_count.items():
    print(i,j)
    f = open("output.txt", "a")
    f.write(name +'\n' + str(i) +'\t' + str(j) + '\n')
    f.close()

# Counting the Error's
for item in error:
    if item in error_count:
        error_count[item] += 1
    else:
        error_count[item] = 1
f = open("output.txt", "a")
f.write("\n\nPrinting the codes present in the Log files\n")
for i,j in error_count.items():
    print(i,j)
    f = open("output.txt", "a")
    f.write(str(i) +'\t' + str(j) + '\n')
    f.close()

# Counting the Ip's and Error's
for item in ip_error:
    if item in ip_error_count:
        ip_error_count[item] += 1
    else:
        ip_error_count[item] = 1
f = open("output.txt", "a")
f.write("\n\nPrinting the ips & codes present in the Log files\n")
for i,j in ip_error_count.items():
    print(i,j)
    f = open("output.txt", "a")
    f.write(name +'\n' + str(i) +'\t' + str(j) + '\n')
    f.close()    

# Counting based on Dynamic Input
error_code = int(input("Enter the ERROR CODE :"))
dynamic_dict = {}
for x,y in ip_error_count.items():
    if str(error_code) == x[-3:]:
        dynamic_dict[x] = y
for i,j in dynamic_dict.items():
    print(i,j)