class_held=int(input("number of classes held"))
class_attended=int(input("number of class attended"))
if (class_attended//class_held)*100>=75:
	print("he is allowed to sit in exam")
else:
	print("he is not allowed")