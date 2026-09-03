#1.	Write a function factorial(n) that accepts an integer and returns its factorial.
n=int(input("Enter a number"))
def evenorodd(n):
    if(n%2==0):
        return "Number is Even"

    else:
        return "Number is Odd"


print(evenorodd(n))