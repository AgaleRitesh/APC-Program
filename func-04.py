#function to clculate Simple iNtererest
n=int(input("Enter a Amount to CAlculate si"))
r=int(input("Enter Annual interet Rate"))
t=int(input("Enter the Time(int years)"))

def simpleInterest(n,r,t):
    return (n*r*t)/100

print(simpleInterest(n,r,t))
