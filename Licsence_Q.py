speed=int(input("enter the speed"))
a=(speed-70)//5
if speed<=70:
	print("speed is okk")
elif speed>70 and a<=12:
		print(a,"points")
		print("if points are more than 12 your lisence will be cancelled")	
else:
	print("your lisence is cancelled")