a=int(input("enter the number"))
if a!=2 and a!=3 and a!=5 and a!=7 and a!=11:
	if  a%2==0 or a%3==0 or a%5==0 or a%7==0 or a%11==0:
		print(" it is a not prime number")
	else:
		print("is a prime number")
else:
	print("It is prime number")