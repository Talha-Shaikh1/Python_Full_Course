# 4. Assignment Operators
# Used to assign values to variables.


# Operator	Example	    Equivalent To
# =	        x = 5	    x = 5
# +=	    x += 3	    x = x + 3
# -=	    x -= 3	    x = x - 3
# *=	    x *= 3	    x = x * 3
# /=	    x /= 3	    x = x / 3
# //=	    x //= 3	    x = x // 3


x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0


# walrus operator
# The walrus operator := was introduced in Python 3.8.

# It allows assignment and evaluation in a single expression.

# Great for use in loops or conditional statements to reduce redundancy.

# Example: if (n := len(data)) > 10: assigns and checks in one go.

# It improves readability and efficiency when used wisely!

if (user_input := input("Enter a Number")) and user_input.isdigit():
    print("user_input = ",user_input)
else:
    print("enter a valid number!")