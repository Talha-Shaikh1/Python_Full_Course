# Operator and Operand in Python

**Operator** — A symbol that performs an operation (e.g. `+`, `-`, `*`, `/`, `not`).

**Operand** — The value(s) or variable(s) that the operator works on.  
Think of operands as the “inputs” for an operator.

---

## Key Points

- Operands are the values/variables an operator acts on.
- The number of operands depends on the operator:
  - **Unary operators** → work with **one** operand
  - **Binary operators** → work with **two** operands

---

## Unary Operators

Unary operators work with **one operand** (a single value or variable).

### 1. Unary Minus (`-`)

Changes the sign of the operand.

```python
x = 5
y = -x          # y becomes -5
print("y =", y)
```

**Output:**
```
y = -5
```

### 2. Logical NOT (`not`)

Reverses a boolean value.

```python
a = True
b = not a       # b becomes False
print("b =", b)

print(not False)   # True
print(not 0)       # True  (0 is falsy)
print(not 42)      # False (non-zero is truthy)
```

**Output:**
```
b = False
True
True
False
```

### 3. Bitwise NOT (`~`)

Inverts all bits of a number (two’s complement).

```python
x: int = 5          # binary: 0b101
y: int = ~x         # y becomes -6
print("y =", y)

# Viewing binary representation
print("bin(x)  =", bin(x), type(bin(x)))
print("bin(~x) =", bin(~x))

# Clean binary without '0b' prefix
num = 5
print(format(num, 'b'))   # 101
print(f"{num:b}")         # 101
```

**Output:**
```
y = -6
bin(x)  = 0b101 <class 'str'>
bin(~x) = -0b110
101
101
```

---

## Binary Operators

Binary operators work with **two operands**.

### 1. Arithmetic Operators

```python
a = 15
b = 4

print("a + b  =", a + b)   # Addition
print("a - b  =", a - b)   # Subtraction
print("a * b  =", a * b)   # Multiplication
print("a / b  =", a / b)   # Division (float)
print("a // b =", a // b)  # Floor division
print("a % b  =", a % b)   # Modulus (remainder)
print("a ** b =", a ** b)  # Exponentiation
```

**Output:**
```
a + b  = 19
a - b  = 11
a * b  = 60
a / b  = 3.75
a // b = 3
a % b  = 3
a ** b = 50625
```

### 2. Comparison Operators

Return `True` or `False`.

```python
x = 10
y = 7

print(x == y)   # Equal to
print(x != y)   # Not equal to
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal
print(x <= y)   # Less than or equal
```

**Output:**
```
False
True
True
False
True
False
```

### 3. Logical Operators

```python
p = True
q = False

print(p and q)   # True only if both are True
print(p or q)    # True if at least one is True
print(not p)     # Unary – reverses the value
```

**Output:**
```
False
True
False
```

### 4. Assignment Operators

```python
n = 10
print("n =", n)

n += 5          # n = n + 5
print("n += 5 →", n)

n -= 3          # n = n - 3
print("n -= 3 →", n)

n *= 2          # n = n * 2
print("n *= 2 →", n)

n //= 4         # n = n // 4
print("n //= 4 →", n)
```

**Output:**
```
n = 10
n += 5 → 15
n -= 3 → 12
n *= 2 → 24
n //= 4 → 6
```

---

## Key Difference

| Type       | Operands | Examples                  |
|------------|----------|---------------------------|
| **Unary**  | 1        | `-x`, `not a`, `~n`       |
| **Binary** | 2        | `a + b`, `x > y`, `p and q` |

---

> **Note:** Python has many more operators (bitwise, membership, identity, etc.). We will explore them in upcoming topics.
```
