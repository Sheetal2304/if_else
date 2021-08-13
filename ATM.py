a="insert your ATM card"
print(a)
user=input("select language:-"" ""english or hindi")
if user=="english":
	usera=int(input("enter 4-digit pin"))
	if usera!=1234:
		print("wrong pin")
	elif usera==1234:
		userb=input("type of account:"" ""current account or saving account")
		if userb=="saving account" or "current account":
			userc=int(input("enter the withdrawal amount"))
			if userc<=100000 and userc%100==0:
				print("collect your cash")
				print(" thank you")
			else:
				print("unsufficient amount")
elif user=="hindi":
	user1=int(input("4 akshar ka pin daale"))
	if user1!=1234:
		print("pin galat hai")
	elif user1==1234:
		user2=input("khaate ka prakaar:-"" ""bachat khaata ya chaalu khaata")	
		if user2=="bachat khaata" or "chaalu khaata":
			user3=int(input("nikaali gyi raashi daale"))
			if user3<=100000 and user3%100==0:
				print("apna cash jmaa kre")
				print("dhanyvaad")
			else:
				print("aparyaapt raashi")
				
else:
	print("invalid language")