# --------------
# Code starts here

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2

print("new class = ",new_class)

new_class.append('Peter Warden')

print("added new student = ",new_class)

new_class.remove('Carla Gentry')

print("removed Carla Gentry from the list = ",new_class)

courses = {
    "Math" : 65,
    "English" : 70,
    "History" : 80,
    "French" : 70,
    "Science" : 60
}

total = courses["Math"] + courses["English"] + courses["History"] + courses["French"] + courses["Science"]

print("Sum of marks",total)

percentage = total / 500 * 100

print("Percentage of marks", percentage)


mathematics = {
    "Geoffrey Hinton" : 78,
    "Andrew Ng" : 95,
    "Sebastian Raschka" : 65,
    "Yoshua Benjio" : 50,
    "Hilary Mason" : 70,
    "Corinna Cortes" : 66,
    "Peter Warden" : 75
}

print(mathematics)

topper = max(mathematics,key = mathematics.get)
print ("Topper in Mathematics = ",topper)

# first_name = topper[0:6]

first_name = topper.split()[0]

print("First name of the topper",first_name)

# last_name = topper[7:9]
last_name = topper.split()[1]

print("Last name of the topper",last_name)

full_name = last_name + " "  + first_name

print("Full name for certificate",full_name)

certificate_name = full_name.upper()

print("Upper case certificate name", certificate_name)

# code ends here








