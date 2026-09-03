#to check given number is prime or not
n=int(input("Enter a Number"))
def prime(n):


        if n<=1:
            return False

        for i in range(2,n):
              if n% i==0:
                    return False

              return True
if prime(n):
      print("Number is Prime")

else:
      print("Number is not prime")



