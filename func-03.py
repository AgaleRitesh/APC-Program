#deffine a fuction that returns greater number between two numbers
n=int(input("Enter a Number"))
m=int(input("Enter a Another Number"))

def greater(n,m):
    if(n>m):
        return n
    else:
        return m

print(greater(n,m))
      