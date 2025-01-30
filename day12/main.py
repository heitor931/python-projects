# prime number checker

def is_prime(num):
    divisor = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisor+=1
    if divisor == 2:
        return True
    else:
        return False

result = is_prime(75)
print(result)
