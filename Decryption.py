from Lockers import test
from EuclideanAlgo import xgcd
from PollardRho import factor


def Decrypt(C, E, n):
    p, q = factor(n)
    nprime = (p-1)*(q-1)
    print("Factored: ", p, " ", q)
    val = xgcd(E, nprime)
    print("Inverses: ", ''.join(str(i)+' ' for i in val))
    D = int(val[1] % nprime)

    print("Decryption Key found: ", D)
    return pow(C, D, n)


if __name__ == '__main__':
    print("Welcome to RSA Decryption")
    C = int(input("What is your encrypted message: "))
    n = int(input("What is your public modulus: "))
    E = int(input("What is your public encryption key: "))
    print("")
    print("-------------------------------------------")
    print("")
    D = Decrypt(C, E, n)
    print(D)
    print(test(str(D)[:4]), str(D)[0:4], " : ", str(D)[4:])
    print(test(str(D)[6:]), str(D)[6:], " : ", str(D)[:6])
    print("")
    print("-------------------------------------------")
    print("")
