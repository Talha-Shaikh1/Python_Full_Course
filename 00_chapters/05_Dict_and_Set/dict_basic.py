# dict is the built in data type used to store key value pair and it is unorderd
# key: we can set key immutables types such as string number boolean not list dict and set because they are mutable aur key hamesha unique hugi duplicate key entertain nh krta 

my_dict = {
    "id": 1,
    "first_name": "Talha",
    "last_name": "Shaikh",
    2: "Two",
    True: "Yes",
    ("key"): "Valid Key"
    # ["key"]: "not a valid key" # beacuse list is mutable and key must be immutables
}

print(my_dict)

# dict is onrdered but we can access value by using thier key example 
print(my_dict["first_name"])

# and dict have unique key name but if we create duplicate python nerver raise a error but ignore the first and take the last one

print("my_dict2")
my_dict2 = {
    "name": "Talha",
    "name": "Shaikh"
} # will take a second and ignore the first one

print(my_dict2)

# we can update value of dict example
student = {
    "id": 1,
    "name": "Ahmed",
    "subject": "Science"
}

print("Before update", student)
# we want to update the subject science to math
student['subject'] = "Math"
print("After update", student)

# we can also add a new key value pair we want to add some more info in student dict like class 10

student["class"] = "10th"

print("add new pair" ,student)