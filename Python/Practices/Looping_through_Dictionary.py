sample_data = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
for data in sample_data.items():
    print(data)

for data in sample_data.keys():
    print(data)

for data in sample_data.values():
    print(data)

# Dictionary Loop and String Formatting
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key}: {value}")

