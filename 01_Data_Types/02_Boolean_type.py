# 2. Boolean (bool)

# represents True or False

is_python_fun: bool = True  # False

print(type(is_python_fun), "is_python_fun =", is_python_fun)
# with type() function we can see the type of any variable


# Example 1: Comparison
is_true = 2 == 2

print(type(is_true), "is_true =", is_true)


# Example 2: Greater than
is_greater = 10 > 5

print(type(is_greater), "is_greater =", is_greater)


# Example 3: Less than
is_less = 3 < 7

print(type(is_less), "is_less =", is_less)


# Example 4: Equal to
is_equal = 10 == 10

print(type(is_equal), "is_equal =", is_equal)


# Example 5: Not equal to
is_not_equal = 10 != 5

print(type(is_not_equal), "is_not_equal =", is_not_equal)


# Example 6: Checking a condition
age = 20
is_adult = age >= 18

print(type(is_adult), "is_adult =", is_adult)


# Example 7: Boolean with strings
name = "Talha"
has_name = name != ""

print(type(has_name), "has_name =", has_name)


# Example 8: Boolean with AND
has_username = True
has_password = True

can_login = has_username and has_password

print(type(can_login), "can_login =", can_login)


# Example 9: Boolean with OR
is_weekend = False
is_holiday = True

can_relax = is_weekend or is_holiday

print(type(can_relax), "can_relax =", can_relax)


# Example 10: NOT operator
is_raining = False

is_not_raining = not is_raining

print(type(is_not_raining), "is_not_raining =", is_not_raining)


# Comparison operators

5 == 5    # True   → equal
5 != 3    # True   → not equal
5 > 3     # True   → greater than
5 < 3     # False  → less than
5 >= 5    # True   → greater than or equal
3 <= 5    # True   → less than or equal


# Logical operators

True and True    # True
True and False   # False

True or False    # True
False or False   # False

not True         # False
not False        # True