# None Data Type in Python
# In Python, None is a special data type that represents the absence of a value or a null object reference. It is a singleton object, meaning that there is only one instance of None in the entire Python environment.

# No value: None represents the absence of a value or a null object reference.

x: str = None
y: str = None
z: str = x

print(type(x))
print("value of x = ", str(x))
print("x == y = ",x == y)
print("id(x) =",id(x))
print("id(y) =",id(y))
print("id(z) =",id(z))

print("x is y", x is y)
print("x is z", x is z)

print("id(x) is id(z)", id(x) is id(z)) # False :( why? you will get the answer in topic 'Integer Literals in Python'
print("id(x) == id(z)", id(x) == id(z))

'''
In Python, `==` is the equality operator, which checks if the values of two objects are equal.
On the other hand, `is` is the identity operator, which checks if two objects are the same object in memory.
'''

print("--" * 16)

print("None is None            = ", None is None) # True
print("None == None            = ", None == None) # True
print("None == x               = ", None == x)
print("None is x               = ", None is x)
print("id(None) is id(None)    = ", id(None) is id(None)) # 'is' check memory space sharing
#If number is out of integer literal range -5 to 256 then even the same number are considered as seprate object





# id() Function in Python
# The id() function in Python returns the unique identifier for an object. This identifier is a small integer that is unique among all objects currently in existence of your python environment.

# What is the Purpose of id()
# The id() function is used to:

# Identify objects: The id() function returns a unique identifier that can be used to identify objects in memory.
# Check object equality: By checking the id() of two objects, you can determine if they are the same object in memory.
# Debugging: The id() function can be useful for debugging purposes, such as identifying which object is being referenced by a variable.

print("--" * 16)


print("""Variable x, y & z have 'None' value, as we know that 'None' is a singleton object,
meaning that there is only one instance of `None` in the entire Python environment.
So the id(x), id(y) & id(z) represents the same object id in memory.\n""")

x: str = None
y: str = None
z: str = x

print("ID of variable x  = " + str(id(x)))
print("ID of variable y  = " + str(id(y)))
print("ID of variable z  = " + str(id(z)))

print("\nIs variable x & y shares the same memory space? \nThe answer is: " + str(id(x) == id(y)))


# Integer Literals in Python
# In Python, an integer literal is a sequence of characters that represents an integer value. Integer literals are used to define integer constants in Python code.

# Memory Space Sharing
# In Python, integer literals can share the same memory space under certain conditions. This is due to a process called interning, where Python stores a pool of interned objects that can be reused when the same value is needed again.

# Lets assign value to variable x, y & z

print("--------------------","Integer Literals","--------------------")

x:int = 1
y:int = 1
z:int = x

print("value of x = " + str(x) + "and id(x) = " + str(id(x)))
print("value of y = " + str(y) + "and id(y) = " + str(id(y)))
print("value of x = " + str(z) + "and id(z) = " + str(id(z)))
print("id(x) == id(y) = ", id(x) == id(y) )
print("id(x) is id(y) = ", id(x) is id(y) ) # ;)





# Integer Interning in Python
# In Python, integers in the range -5 to 256 are interned, meaning that they are stored in a pool of interned objects. This means that when you create an integer literal within this range, Python returns a reference to the existing object in the pool.

print("--------------------","Integer Interning","--------------------")