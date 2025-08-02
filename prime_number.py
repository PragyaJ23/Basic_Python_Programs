def prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):    #prime number
        if n % i == 0:
            return False
    return True
num=int(input("enter your number:"))
if prime(num):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
