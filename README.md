# PyStructures 🧱

> A pure Python library implementing custom data structures and mathematical types — no external dependencies, built from scratch.

---

## Overview

**PyStructures** provides four fully-featured Python classes covering fundamental computer science data structures and mathematical objects:

- `Stack` — LIFO data structure
- `Queue` — FIFO data structure
- `Polynomial` — Algebraic polynomial with calculus operations
- `Matrix` — 2D matrix with linear algebra operations

All logic is implemented manually using core Python — no NumPy, no math libraries (except `math.sqrt` in Polynomial), no shortcuts.

---

## Files

```
PyStructures/
├── Stack.py
├── Queue.py
├── Polynomial.py
├── Matrix.py
└── README.md
```

---

## Stack

**File:** `Stack.py`

A Last-In-First-Out (LIFO) data structure.

```python
from Stack import Stack

s = Stack()
s.push(10)
s.push(20)
s.peek()     # 20
s.pop()      # 20
s.size()     # 1
s.isempty()  # False
s.clear()
```

| Method | Description |
|---|---|
| `push(x)` | Adds element x to the top of the stack |
| `pop()` | Removes and returns the top element. Returns None if empty |
| `peek()` | Returns the top element without removing it. Returns None if empty |
| `isempty()` | Returns True if the stack is empty, False otherwise |
| `size()` | Returns the number of elements in the stack |
| `clear()` | Removes all elements from the stack |
| `merge(x)` | Merges another stack x into this stack |
| `help()` | Prints all methods with descriptions |

---

## Queue

**File:** `Queue.py`

A First-In-First-Out (FIFO) data structure.

```python
from Queue import Queue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.front()    # 1
q.rear()     # 2
q.dequeue()  # 1
q.size()     # 1
```

| Method | Description |
|---|---|
| `enqueue(x)` | Adds element x to the rear of the queue |
| `dequeue()` | Removes and returns the front element. Returns None if empty |
| `front()` | Returns the first element without removing it. Returns None if empty |
| `rear()` | Returns the last element without removing it. Returns None if empty |
| `isempty()` | Returns True if the queue is empty, False otherwise |
| `size()` | Returns the number of elements in the queue |
| `clear()` | Removes all elements from the queue |
| `merge(x)` | Merges another queue x into this queue |
| `help()` | Prints all methods with descriptions |

---

## Polynomial

**File:** `Polynomial.py`

Represents a polynomial as a list of coefficients (highest degree first).

`[3, 2, 1]` → `3x² + 2x¹ + 1`

```python
from Polynomial import Polynomial

p1 = Polynomial([3, 2, 1])
p2 = Polynomial([1, 0])

p1.display()       # 3x^2 + 2x^1 + 1
p1.evaluate(2)     # 17
p1.solution()      # roots of the polynomial
p1.degree()        # 2
p1.derivative()    # Polynomial([6, 2])
p1.integral()      # Polynomial([1.0, 1.0, 1.0])
p1.add(p2)         # Polynomial([3, 3, 1])
p1.subtract(p2)    # Polynomial([3, 1, 1])
p1.multiply(p2)    # Polynomial([3, 2, 1, 0])
```

| Method | Description |
|---|---|
| `display()` | Displays the polynomial in readable format |
| `evaluate(x)` | Evaluates the polynomial for a given value of x |
| `solution()` | Returns root(s). Supports linear and quadratic only |
| `degree()` | Returns the degree (highest power) of the polynomial |
| `derivative()` | Differentiates and returns a new Polynomial |
| `integral()` | Integrates and returns a new Polynomial |
| `add(other)` | Adds two polynomials, returns a new Polynomial |
| `subtract(other)` | Subtracts another polynomial, returns a new Polynomial |
| `multiply(other)` | Multiplies two polynomials, returns a new Polynomial |
| `help()` | Prints all methods with descriptions |

---

## Matrix

**File:** `Matrix.py`

Represents a 2D matrix as a list of lists.

```python
from Matrix import Matrix

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

m1.add(m2.matrix)        # [[6, 8], [10, 12]]
m1.subtract(m2.matrix)   # [[-4, -4], [-4, -4]]
m1.multiply(m2.matrix)   # [[19, 22], [43, 50]]
m1.transpose()           # [[1, 3], [2, 4]]
m1.determinant()         # -2
m1.trace()               # 5
m1.char_eqn()            # λ² - 5λ + -2
```

| Method | Description |
|---|---|
| `add(matrix2)` | Adds two matrices element by element. Both must be same size |
| `subtract(matrix2)` | Subtracts matrix2 from current matrix element by element |
| `multiply(matrix2)` | Multiplies two matrices. Columns of first must equal rows of second |
| `transpose()` | Flips matrix over its diagonal. Rows become columns |
| `determinant()` | Returns the determinant of a square matrix. Works recursively |
| `trace()` | Returns sum of diagonal elements of a square matrix |
| `char_eqn()` | Returns the characteristic equation: λ² - trace·λ + det |
| `help()` | Prints all methods with descriptions |

---

## Requirements

- Python 3.x
- No external libraries required

---

## Usage

Clone the repo and import any class directly:

```bash
git clone https://github.com/ArshZaidi/PyStructures.git
cd PyStructures
```

```python
from Stack import Stack
from Queue import Queue
from Polynomial import Polynomial
from Matrix import Matrix
```

---

## Author

**Arsh Zaidi**  
Built as part of an exploration into implementing core Python data structures and mathematical types from scratch.

---

## License

MIT License