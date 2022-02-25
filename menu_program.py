import os
def BasicLinuxCom():
	while(1):
		print("\n 1.Show Date \n 2.Show Calendar \n 3.Show network details \n 4.Custom Linux Commands \n 5.Return to main menu \n")
		basic_choice=input("Enter Your Choice:")
		if basic_choice=='1':
			os.system("tput setaf 4")				
			os.system("date")
		elif basic_choice=='2':	
			os.system("tput setaf 4")			
			os.system("cal")
		elif basic_choice=='3':
			os.system("tput setaf 4")
			os.system("ifconfig")
		elif basic_choice=='4':
			li_cmd=input("Enter the Linux command:")
			os.system("tput setaf 4")
			os.system("{}".format(li_cmd))
		elif basic_choice=='5':
				break;
		else:
			print("Oops!!! Wrong Choice, Please Try Again")
			os.system("tput setaf 2")

os.system("tput setaf 3")
print("-".center(150,"-"))
os.system("tput setaf 2")
welcome="Linux Menu Program Using Python"
print(welcome)
while True:
	os.system("tput setaf 3")
	print(" \n 1.Basic Linux Commands \n 2.Docker \n 3.Apache httpd(WebServer) \n 4.Exit \n")
	os.system("tput setaf 2")
	print("-".center(150,"*"))
	main_choice=input("Choose your domain(1-4):")
	if main_choice=='4':
		exit(); 
	while True:
		os.system("tput setaf 3")
		if main_choice=='1':
			BasicLinuxCom()
			break;
				
		elif main_choice=='2':
			break
		else:
			print("Wrong command!!Please try again")
				
		
	else:
		print("Wrong command!!Please try again")
		break
