def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def xgcd(a, b):
    prev_x, x = 1, 0
    prev_y, y = 0, 1
    while b:
        q = a//b
        x, prev_x = prev_x - q*x, x
        y, prev_y = prev_y - q*y, y
        a, b = b, a % b
    return a, prev_x, prev_y


if __name__ == '__main__':
    print(xgcd(51, 89))
    print(xgcd(102, 202))
    print(xgcd(666, 1414))
    print(xgcd(50, 127))
    print(xgcd(5, 192))
    print(xgcd(9876543210, 123456789))
    print(xgcd(11111111111, 1000000001))
    print(xgcd(45666020043321, 73433510078091009))
