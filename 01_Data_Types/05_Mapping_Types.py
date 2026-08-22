# 5. Mapping Type
# Dictionary (dict) Stores key-value pairs.

my_dict: dict = {
    "name": "Talha",
    "age": 21,
    "language": "python"
}

print(my_dict["age"])   # access value using key
print(my_dict.get("name")) # access value safely only can access no update

my_dict["name"] = "Talha Shaikh"
my_dict["city"] = "Karachi" # add new key value pair
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())