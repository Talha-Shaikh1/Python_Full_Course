# we have some built-in method of dict


# dict.values() for get all values of dict

my_dict1 = {
    "id": "001",
    "name": "username1",
    "subject": "python"
}

print(my_dict1.values())

# dict.keys() for get all keys of dict

print(my_dict1.keys())

# dict.items() for get all keys and values return in tuple format

print(my_dict1.items())

# dict.get("key") for get specific value of key in safe mode we 

print(my_dict1.get("name"))
print(my_dict1["name"])  # both use case is same but this throw error if key not found and .get() return None if key not found

print(my_dict1.get("last_name")) # no error safe mode return None
# print(my_dict1["last_name"]) # throw KeyError

# dict.pop() delete specific value of key

print(my_dict1.pop("id"))
print(my_dict1)


# dict.clear() delete the all keys and values
my_dict1.clear()
print(my_dict1)