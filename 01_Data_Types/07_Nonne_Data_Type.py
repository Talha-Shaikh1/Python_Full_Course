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


print("--------------------","id() function","--------------------")


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

x = -6
y = -6
z = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(z) = " + str(id(z)))

print("\n ===================== \n")

a = 257
b = 257
c = a

print("Value of x = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of y = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of z = " + str(c) + ", and id(c) = " + str(id(c)))


# Type Casting
# Type casting is the process of converting a value of one data type to another data type. Python supports several types of type casting, including:

# Implicit Type Casting: Python automatically converts a value of one data type to another data type when necessary. For example, when you add an integer and a float, Python converts the integer to a float.
# Explicit Type Casting: You can use functions like int(), float(), str(), and bool() to explicitly convert a value of one data type to another data type.

print("--------------------","Type Casting","--------------------")

i: int = 10
print("Value of i = " + str(i) + ",     Type of i = " + str(type(i)))

j: float = 20.6

f: float = i + j #Implicit Type Casting
print("Value of f = " + str(f) + ",   Type of f = " + str(type(f)))

f1: float = 66.89
print("Value of f1 = " + str(f1) + ", Type of i = " + str(type(f1)))

i1: int = int(f1) #When ever you type cast a float value into an integer it truncate
             #the decimal part and only keeps the whole number
print("Value of i1 = " + str(i1) + ",    Type of i = " + str(type(i1)))

s: str = "25.8"
f2: float = float(s)
print("Value of f2 = " + str(f2) + ",  Type of i = " + str(type(f2)))

#uncomment the below line of code to see error
#i2 = int(s) #correct this error by casting with float()
#print("Value of i2 = " + str(i2) + ", Type of i = " + str(type(i2)))


# Truthy and Falsy Values in context of boolean data type
# In Python, some values are considered truthy, while others are considered falsy. Truthy values are treated as True in a boolean context, while falsy values are treated as False.

# Here are some examples of truthy and falsy values:

# Truthy values:
# Non-zero integers (e.g., 1, 2, -3, etc.)
# Non-empty strings (e.g., "hello", "world", etc.)
# Non-empty lists (e.g., [1, 2, 3], ["a", "b", "c"], etc.)
# Non-empty dictionaries (e.g., {"a": 1, "b": 2}, etc.)
# Falsy values:
# Zero (e.g., 0)
# Empty strings (e.g., "")
# Empty lists (e.g., [])
# Empty dictionaries (e.g., {})
# None


print("--------------------","Truty and Falsy Values","--------------------")
k: int = -9 #Any number either positive or negative, beside '0' ZERO is considered True
b: bool = bool(k)
print("Value of b = " + str(b) + ", Type of b = " + str(type(b)))

print("\n =================== \n")

if(k):
  print("""if block: This line of code will execute if we provide any integer value
          other then '0' ZERO""")
else:
  print("else block: As '0' is considered False, so this line of code will not execute")

print("\n =================== \n")

print("check: bool(\"55\")             = ", bool("55"))
print("check: bool(\"\")               = ", bool(""))
print("check: bool([1, 2, 3])        = ", bool([1, 2, 3]))
print("check: bool({\"key\", \"value\"}) = ", bool({"key", "value"}))

#Note: we will learn about list and dictionary in up comming classes
print("check: bool([])               = ", bool([])) #[] square brackets used to represent list
print("check: bool({})               = ", bool({})) #{} curly brackets used to represent dictionary



# isinstance() Function in Python
# The isinstance() function in Python is used to check if an object (first argument) is an instance of a class (second argument). It returns True if the object is an instance of the class, and False otherwise.

# Syntax
# The syntax of the isinstance() function is as follows:

# isinstance(object, classinfo)
# Where:

# object is the object to be checked.
# classinfo is the class or a tuple of classes to check against.

print("--------------------","isinstance() Function in Python","--------------------")

age: int = 20
weight: float = 66.89
print("check: isinstance(age, int)      = ", isinstance(age, int))
print("check: isinstance(weight, int)   = ", isinstance(weight, int))
print("check: isinstance(weight, float) = ", isinstance(weight, float))