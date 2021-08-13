user=input("enter the name")
user1=int(input("enter the password"))
if user=="sheetal":
	if user1==9873912901:
		print("successfully login")
	else:
		print("wrong password")	
if user!="sheetal":
	if user1==9873912901:
		print("wrong name")		
if user!="sheetal":
	if user1!=9873912901:
		print("both are wrong")
		print("create new account")