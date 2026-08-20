# a. String (str)
# a sequence of character enclosed in quotes

text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!
Python is my fav programing lang''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!
                    Pyhton is my fav programing lang.""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>


# Key Takeaways
# Double Quotes ("): Use when the string contains single quotes.
# Single Quotes ('): Use when the string contains double quotes.
# Triple Quotes (''' or """): Use for multi-line strings or docstrings.

# Understanding these variations allows you to write cleaner, more readable, and error-free code. As you progress in Python, you’ll find that strings are incredibly powerful, especially when combined with string methods, formatting, and manipulation techniques.

# b. List (list)
# an ordered, mutable collection

my_list_1: int = [1,2,3, "python", 4.4, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'

my_list: list = [1,2,3, "python", 4.4, 3 + 2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)
print(type(my_list), " my_list = " + str(my_list))


# c. Tuple (tuple)
# an ordered, immutable collection.

my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3, 3+2j)
print(type(my_tuple), " my_tuple = ", my_tuple )


# d. Range (range)
# Reperesents a sequence of numbers.

num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)

for i in range(1,10,2):
    print(i)