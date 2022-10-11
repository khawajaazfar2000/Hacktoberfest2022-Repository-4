'''def mutiply(x):
    return x*x
print(mutiply(2))

def mutiply(x,y):

    print("X:",x)
    print("Y:",y)
    return x*y
print(mutiply(2,8))

def mutiply(x,y,z):
    return (x+y+z)
print(mutiply(2,7,7))
def mutiply(*x):
    return x
print(mutiply(2,3,3,3,4,4,5))'''

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
# take input from the user
num = int(input("Enter a number: "))
# check is the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))