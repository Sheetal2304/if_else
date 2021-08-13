user=int(input("enter the number"))
y=user
x=0
while user>0:
	a=user%10
	x=x+(a**3)
	user=user//10
if y==x:
	print("it is armstrong number")	
else:
	print(" it is not a armstrong number")