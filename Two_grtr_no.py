a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=int(input("enter the number"))
if a>b and a>c and a>d:
	if b>c and b>d:
		print(a,b)
	elif c>b and c>d:
		print(a,c)
	elif d>b and d>c:
		print(a,d)
elif b>a and b>c and b>d:
	if a>c and a>d:
		print(b,a)
	elif c>a and c>d:
		print(b,c)
	elif d>a and d>c:
		print(b,d)
elif c>a and c>b and c>d:
	if a>b and a>d:
		print(c,a)
	elif b>a and b>d:
		print(c,b)
	elif d>a and d>b:
		print(c,d)
elif d>a and d>b and d>c:
	if a>b and a>c:
		print(d,a)
	elif b>a and b>c:
		print(d,b)
	elif c>a and c>b:
		print(d,c)			
else:
	print(" there is no greater number")