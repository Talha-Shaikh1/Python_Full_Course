# 3. Logical Operators
# Used to combine conditional statements.


# Operator	       Name	            Example
# and	           Logical AND	    (5 > 3 and 10 > 5) → True
# or	           Logical OR	    (5 > 3 or 10 < 5) → True
# not	           Logical NOT	    not(5 > 3) → False

x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False