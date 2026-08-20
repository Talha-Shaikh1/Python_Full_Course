# 1. Numeric Types
# Python has three main types:

# a. Integer (int)
# whole numbers, positive or negative, without decimal

num_int: int = 42 #int is type for this var
print("num_int = ",num_int)
print(type(num_int))

# b. Floating-Point (float)
# Numbers with decimal point 

num_float: float = 3.14
# num_float: float = .14

print(type(num_float), " num_float = ",num_float )

# c. Complex (complex)
# Numbers with a real and imaginary part 

num_complex: complex = 2 + 3j
print(type(num_complex), " num_complex = ",num_complex)

# with .real and .imag attribute we can extract the real and imaginary parts of  complex number

print("Real Part: ",num_complex.real) # 2
print("Imaginary Part: ",num_complex.imag) # 3.0