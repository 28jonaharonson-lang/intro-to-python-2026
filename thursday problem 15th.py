
def detPrime(num):
    prime = True
    div = num - 1
    while div > 1:
        if num % div == 0:
            return False
        div = div - 1
    return prime

def lDigits(num):
    upper = 10**(num) - 1
    lower = 10**(num - 1)
    for i in range(lower, upper):
        if detPrime(i) == True:
            temp = i
    return temp
print(lDigits(6))




