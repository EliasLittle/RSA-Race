import math
import numpy as np
from qprimes import primelist


def Q(x, n):
    return pow((x + int(math.sqrt(n))), 2) - n


def remove(val, n):
    # print("Removing "+str(n)+" from "+str(val))
    nval = val
    count = 0
    while nval % n == 0:
        nval = nval / n
        count += 1
    return [nval, count]


def legendre_symbol(n, p):
    ls = pow(n, (p - 1)/2, p)
    if ls == p - 1:
        return -1
    return ls


def prime_mod_sqrt(a, p):
    """
    Square root modulo prime number
    Solve the equation
        x^2 = a mod p
    and return list of x solution
    http://en.wikipedia.org/wiki/Tonelli-Shanks_algorithm
    """
    a %= p

    # Simple case
    if a == 0:
        return [0]
    if p == 2:
        return [a]

    # Check solution existence on odd prime
    if legendre_symbol(a, p) != 1:
        return []

    # Simple case
    if p % 4 == 3:
        x = pow(a, (p + 1)/4, p)
        return [x, p-x]

    # Factor p-1 on the form q * 2^s (with Q odd)
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2

    # Select a z which is a quadratic non resudue modulo p
    z = 1
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    # Search for a solution
    x = pow(a, (q + 1)/2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        # Find the lowest i such that t^(2^i) = 1
        i, e = 0, 2
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        # Update next value to iterate
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]


def ShanksTonelli(n, p):
    if n == 0:
        return [0]
    if p == 2:
        return [n]

    if legendre_symbol(n, p) != 1:
        return []

    if p % 4 == 3:
        r = pow(n, (p + 1)/4, p)
        return [r, p-r]

    Q, s = p - 1, 0
    while Q % 2 == 0:
        s += 1
        Q //= 2
    for i in range(p):
        if pow(i, (p-1)//2, p) == (p-1):
            z = i
            break
    M = s
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q+1)//2, p)

    if t == 0:
        return 0
    while t != 1:
        e = 1
        for i in range(0, M):
            if pow(t, pow(2, i), p) == 1:
                e = i
                break
        b = pow(c, pow(2, M-e-1), p)
        M = e
        c = pow(b, 2, p)
        t = (t*c) % p
        R = (R*b) % p
    else:
        return [R, n-R]


def binReduce(A):
    rows = len(A)
    cols = len(A[0])
    for i in range(0, cols):  # For each column
        maxRow = i
        if i < rows-1:
            start = i
        else:
            break
        for k in range(start, rows-1):
            if A[k][i] == 1:
                maxRow = k
                break
        try:
            A[maxRow][i]
        except Exception:
            print("Cols: "+str(cols))
            print("Rows: "+str(rows))
            print("maxRow "+str(maxRow))
            print("i "+str(i))
        if A[maxRow][i] == 1:
            A[i], A[maxRow] = A[maxRow], A[i]  # swaps max row with current row
            for u in range(i+1, rows):
                if A[u][i] == 1:
                    A[u] = [sum(j) % 2 for j in zip(A[u], A[i])]

    return A


alf = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1]
]

for row in binReduce(alf):
    print(row)

n = 37211
M = 1000
xset = list(range(-1*M, M))
s = primelist  # set of primes
XtoQ = {x: Q(x, n) for x in xset}  # X : Q(x)
pVectors = {}  # x : {p1: c1, p2: c2}
for x in xset:
    pVectors[x] = {p: 0 for p in s}

for p in s[1:]:
    # print("sieving")
    st = ShanksTonelli(n, p)
    if len(st) == 0:
        continue
    else:
        a = st[0]-int(math.sqrt(n)) % p
        b = p-a % p

        for x in xset:
            xfixed = x % p
            if xfixed == a:
                result = remove(XtoQ[x], p)
                XtoQ[x] = result[0]
                pVectors[x][p] = (pVectors[x][p] + result[1]) % 2
            if xfixed == b:
                result = remove(XtoQ[x], p)
                XtoQ[x] = result[0]
                pVectors[x][p] = (pVectors[x][p] + result[1]) % 2

matrix = []
for key in XtoQ:
    # print(XtoQ[key])
    if XtoQ[key] == 1:
        v = []
        for p in pVectors[key]:
            v.append(pVectors[key][p])
        # print(v)
        matrix.append(v)


mat = binReduce(matrix)
M = np.array([[i for i in mat] for row in mat])

if len(matrix) < 1:
    print("Matrix is empty")
else:
    sol = np.linalg.solve(M, np.array([0 for row in matrix]))
    print(sol)
    print("Success?")
