n = int(input("Check this number: "))

def prime_checker(num):
    prime = True
    for i in range(2, num):
        if(num%i == 0):
            prime = False
    return prime

if(n == 1 or n == 2 or n == 3):
    print("Prime")
else:
    if(prime_checker(n)):
        print("Prime")
    else:
        print("Non Prime")