import os
#Funtion#1
def BasicLinuxCom():
	while(1):
		print("\n 1.Show Date \n 2.Show Calendar \n 3.Show network details \n 4.Custom Linux Commands \n 5.Return to main menu \n")
		sub_choice=input("Enter Your Choice: ")
		if sub_choice=='1':
			os.system("tput setaf 4")				
			os.system("date")
		elif sub_choice=='2':	
			os.system("tput setaf 4")			
			os.system("cal")
		elif sub_choice=='3':
			os.system("tput setaf 4")
			os.system("ifconfig")
		elif sub_choice=='4':
			li_cmd=input("Enter the Linux command:")
			os.system("tput setaf 4")
			os.system("{}".format(li_cmd))
		elif sub_choice=='5':
				break;
		else:
			print("Oops!!! Wrong Choice, Please Try Again")
			os.system("tput setaf 2")
#Funtion#2
def Docker():
	while(1):
		os.system("tput setaf 6")
		print("*".center(150,"*"))
		print("\n1.Docker Installation \n2.Docker Search \n3.Docker Pull\n4.Show Docker Images\n5.Show All Docker Containers\n6.Return to main menu")
		sub_choice=input("\nEnter Your Choice : ")
		if sub_choice=='1':
			os.system("yum install docker-ce --nobest -y")
			print("Docker sucessfully installed....")
		if sub_choice=='2':
			img=input("Enter The Image Name To Search : ")
			os.system("docker search "+img)
		if sub_choice=='3':
			img=input("Enter The Image Name You Want To Pull : ")
			os.system("docker pull "+img)
		if sub_choice=='4':
			os.system("docker images")
		if sub_choice=='5':
			os.system("docker ps -a")
		if sub_choice=='6':
			break;
		

os.system("tput setaf 3")
print("-".center(150,"-"))
os.system("tput setaf 2")
welcome="Linux Menu Program Using Python"
print(welcome)
while True:
	os.system("tput setaf 3")
	print(" \n 1.Basic Linux Commands \n 2.Docker \n 3.Apache httpd(WebServer) \n 4.Exit \n")
	print("-".center(150,"*"))
	main_choice=input("Choose your domain(1-4):")
	if main_choice=='4':
		os.system("tput setaf 5")
		print("\nThanks For Using Python Menu Program\n")
		os.system("tput setaf 7")
		exit(); 
	while True:
		os.system("tput setaf 3")
		if main_choice=='1':
			BasicLinuxCom()
			break;
				
		elif main_choice=='2':
			Docker()
			break;
		else:
			print("Wrong command!!Please try again")
				
		
	else:
		print("Wrong command!!Please try again")
		break
