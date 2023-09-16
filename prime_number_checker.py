#prime number checker
n=int(input("type a number:"))
prime_num=True
def prime_checker(number):
  for i in range(2,number):
     if number%i==0:
            prime_num=False
if prime_num:
     print("It's a prime number")
else:
     print("It is not a prime number")

prime_checker(number=n)     