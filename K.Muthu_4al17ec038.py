attempt=1
while attempt<=3:
	usr=input("Enter the username : ")
	pwd=input("Enter the password : ")
	if usr=="Micheal" and pwd=="e3$WT89x":
		print("Yoy have successfully logged in ")
		break
	else:
		attempt+=1
		print("Invalid username or password \n")