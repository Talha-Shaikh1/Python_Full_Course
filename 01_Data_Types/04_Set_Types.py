# 4. Set Types 
# Unordered collections with unique elements

# a. Set (set)
# Mutable, onorderd, and contains unique values.

my_set: set = {1,2,3,4,5}
print(type(my_set), "my_set = ",my_set)

# b. Frozen Set (frozenset)
# immutable version of a set

frozen_set : frozenset = ([1,2,3,4,5,6])
frozen_set = frozenset(my_set)

print(type(frozen_set), " frozen_set = ", frozen_set)  