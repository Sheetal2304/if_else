num1=int(input("enter the number"))
symbol=input("enter the operator")
num2=int(input("enter the other number"))
if symbol=="+": 
	print(num1+num2)
elif symbol=="-":
	print(num1-num2)
elif symbol=="*":
	print(num1*num2)	
elif symbol=="/":
	print(num1/num2)
else:
	print("invalid")