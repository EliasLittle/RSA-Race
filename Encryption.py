import random
from EuclideanAlgo import gcd


def genEncKey(p, q):
    nprime = (p-1)*(q-1)
    run = True
    while run:
        E = 2*random.randint(1, 1000000)+1
        if gcd(E, nprime) == 1:
            run = False
    return E


def encrypt(M, p, q, E):
    return pow(M, E, p*q)


if __name__ == '__main__':
    print("Welcome to RSA Encryption")
    M = int(input("What is your message: "))
    p = int(input("Input your first large prime: "))
    q = int(input("Input your second large prime: "))
    E = int(input("Input Encryption Key if available (0 if not): "))
    print("")
    print("-------------------------------------------")
    print("")
    if E == 0 or type(E) != int:
        E = genEncKey(p, q)
    print("Your Encryption Key is: ", E)
    print("Your public modulus is: ", p*q)
    C = encrypt(M, p, q, E)
    print("Your encrypted message is: ", C)
    print("")
    print("-------------------------------------------")
    print("")
