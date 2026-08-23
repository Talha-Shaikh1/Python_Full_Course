# 6. Binary Types
# In Python, binary types are used to handle binary data, such as raw bytes, binary files, or data exchanged over networks. Binary types are distinct from text types (str) and are specifically designed to represent and manipulate sequences of bytes. Python provides three built-in binary types:

# a. Bytes (bytes)
    # 1. Definition: an immutable sequence of bytes 
    # 2. Purpose: Used to reperesent binary data, such as byte sequences coming from files, network communications, or raw data.
    # 3. Key Points: 
        # * a bytes object is immutable, meaning you cannot modify its content after creation.
        # * it is often used when you need to work with fixed binary data.
        # * literal syntax: b"..." or b'...'

byte_data: bytes = b'hello'
print(type(byte_data), " byte_data = ", byte_data)

with open("test.png", "rb") as image_file:
    image_data = image_file.read()
print(image_data)

with open("test.png", "rb") as source_file:
    data = source_file.read()

with open("copy.png", "wb") as target_file:
    target_file.write(data)

print("Image copied successfully!")

# b. Bytearray (bytearray)
    # 1. Defination: A mutable sequence of bytes.
    # 2. Purpose: Like bytes, but allows modification of its content.
    # 3. Key Points:
        # 1. you can modify the content of bytearray object in place
        # 2. Suitable for cases where you need tu update or manipulate binary data frequently. 
        # 3. literal syntax: Does not have direct literal syntax (must use bytearray() constructor)



# Number Systems
# ASCII:

# The American Standard Code for Information Interchange (ASCII) is a character encoding standard that represents text in computers using numeric codes. It maps 128 characters (letters, digits, punctuation, and control characters) to values from 0 to 127.

# Decimal:

# The decimal system is the standard numerical system used in everyday life, based on 10 digits (0 through 9). It's a base-10 system, where each digit's position represents a power of 10.

# Hexadecimal:

# The hexadecimal system is a base-16 numbering system, using 16 symbols: 0–9 to represent values 0 to 9, and A–F (or a–f) to represent values 10 to 15. It's widely used in computing for compact representation of binary data.

# Octal:

# The octal system is a base-8 numbering system, using digits 0 through 7. It was more commonly used in older computer systems and is still occasionally used in modern computing, especially for file permissions in Unix/Linux.

# Binary:

# The binary system is a base-2 numbering system that uses only two digits: 0 and 1. It's the fundamental language of computers, where each binary digit (bit) represents a state of off or on.

# What is a Base in Number Systems?
# A base (or radix) in a number system refers to the number of unique digits (including zero) used to represent numbers. It defines how place values are assigned to digits in a numeral

byte_array: bytearray = bytearray([65, 66, 67, 69])
print(type(byte_array), " byte_array = ", byte_array)
print(byte_array[0])
print(chr(byte_array[0]))
byte_array[0] = 68
print(byte_array[0])
print(chr(byte_array[0]))
print("Emoty bytearray(): ",bytearray())


# c. Memoryview (memoryview)
# The memoryview object in Python provides an efficient way to work with binary data by allowing you to access and manipulate the memory of another object (like bytes or bytearray) without copying the data. This is particularly useful when working with large datasets or binary streams, as it avoids the overhead of creating additional copies.

mem_view: memoryview = memoryview(b'Talha Shaikh')

print(type(mem_view), " mem_view = ", mem_view)
print(bytes(mem_view[0:9]))
print(mem_view[9:14])