# Python Data Types

Python men 5 main data types hote hain, jo further apni sub-types men divide hote hain.

---

## 1. Numeric

**Definition:** Numeric data type numbers ko store karta hai — integers, floating point numbers, aur complex numbers.

### a) Integer (`int`)
Whole numbers, bina decimal point ke (positive ya negative).

```python
x = 10
y = -25
print(type(x))  # <class 'int'>
```

### b) Float (`float`)
Decimal point wale numbers.

```python
x = 10.5
y = -3.14
print(type(x))  # <class 'float'>
```

### c) Complex (`complex`)
Real aur imaginary part wale numbers, `j` ke sath likhe jaate hain.

```python
x = 3 + 5j
print(type(x))  # <class 'complex'>
```

---

## 2. Dictionary (`dict`)

**Definition:** Key-value pairs store karta hai. Unordered (Python 3.7+ men insertion order maintain hoti hai), mutable, aur keys unique hoti hain.

```python
student = {
    "name": "Talha",
    "age": 25,
    "city": "Karachi"
}
print(student["name"])  # Talha
print(type(student))    # <class 'dict'>
```

---

## 3. Boolean (`bool`)

**Definition:** Sirf do values hoti hain — `True` ya `False`. Conditions aur comparisons ka result usually boolean hota hai.

```python
x = True
y = 5 > 3
print(y)         # True
print(type(x))   # <class 'bool'>
```

---

## 4. Set (`set`)

**Definition:** Unordered collection jisme duplicate values allowed nahi hoti. Mutable hota hai, lekin elements unique aur unindexed hote hain.

```python
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)        # {'apple', 'banana', 'mango', 'orange'} (order vary kar sakta hai)
print(type(fruits))  # <class 'set'>
```

---

## 5. Sequence Type

**Definition:** Ordered collection of items, jisme indexing aur slicing support hoti hai.

### a) String (`str`)
Characters ki ordered sequence, quotes men likhi jaati hai.

```python
name = "Talha"
print(name[0])   # T
print(type(name)) # <class 'str'>
```

### b) List (`list`)
Ordered aur mutable collection, `[]` men likhi jaati hai. Duplicate values allowed hoti hain.

```python
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)      # [1, 2, 3, 4, 5]
print(type(numbers)) # <class 'list'>
```

### c) Tuple (`tuple`)
Ordered aur **immutable** collection, `()` men likhi jaati hai.

```python
coordinates = (10, 20)
print(coordinates[0])  # 10
print(type(coordinates)) # <class 'tuple'>
```

---

## Quick Summary Table

| Data Type | Mutable? | Ordered? | Example |
|-----------|----------|----------|---------|
| int       | -        | -        | `10` |
| float     | -        | -        | `10.5` |
| complex   | -        | -        | `3+5j` |
| dict      | ✅ Yes   | ✅ Yes (insertion order) | `{"a": 1}` |
| bool      | -        | -        | `True` |
| set       | ✅ Yes   | ❌ No    | `{1, 2, 3}` |
| str       | ❌ No    | ✅ Yes   | `"hello"` |
| list      | ✅ Yes   | ✅ Yes   | `[1, 2, 3]` |
| tuple     | ❌ No    | ✅ Yes   | `(1, 2, 3)` |