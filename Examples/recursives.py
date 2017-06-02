#define multiplication by recursive-sum function - valid for integers
def mult_rec_sum(m,n):
    if n == 0 or m == 0:
        return 0
    
    elif n == 1:
        return m
    
    elif n == -1:
        return -m
    
    elif n > 1:
        return m + mult_rec_sum(m, n-1)
    
    else:
        return -m + mult_rec_sum(m,n+1)

print("\nRecursive sum of 1 and -3 is:", mult_rec_sum(1,-3))
print("Recursive sum of 0 and -98 is:", mult_rec_sum(0,-98))
print("Recursive sum of -8.37 and 3 is:", mult_rec_sum(-8.37,3))

#define factorial function
def fact(num):
    if num == 0:
        return 1
    
    elif num < 0:
        return "Value is not valid"

    else:
        x = num * fact(num-1)
    return x

#i = int(input("\nChoose a number for factorial: "))
#print("Factorial of {} is:".format(i), fact(i))
print("\nFactorial of 0 is:", fact(0))
print("Factorial of -1 is:", fact(-1))

#define Ackermann-Peter function (2 variables)
def ack(m,n):
    if m == 0:
        return n+1

    elif m > 0 and n == 0:
        return ack(m-1, 1)
    
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))
    
    elif m < 0:
        return "Value of 'm' is not valid"
    
    else:
        return "Value of 'n' is not valid"

print("\nAckermann of 1,3 is:", ack(1,3))
print("Ackermann of 0,0 is:", ack(0,0))
print("Ackerman of -1,8 is:", ack(-1,8))
print("Ackermann of 0,-1 is:", ack(1,-1))
    
