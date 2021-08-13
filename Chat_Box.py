user=input("are you willing to chat with me. if 'yes'' then say hii").lower()
if user=="hii":
	print("hello")
user2=input("how are you?")	
if user2=="how are you ?":
	print("i m fine")
	print("what about you")
if user2=="i m not well":
	print("why what happened to you")
elif user2=="i m good" or "i m fine too.":
	print("that's great to hear")
user3=input(" are u doing studies?")
if user3=="yes":
		print("what are you doing in your studies")
		usera=int(input("in which class are you?"))
		if usera>=1 and usera<=12:
			print("that's nice")
if user3=="no":
	print("why you don't go to school?")
	userb=input("do you have any family issue?")
	if userb=="yes":
		print("ok")		
	else:
		print("study is important for everyone")	
user4=input("do you liked to communicate to me?")
if user4=="yes":
	 print("it's my pleasure")
if user4=="no":
	 print("hope it will be better next time")