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
		print("\n1.Docker Installation \n2.Docker Search \n3.Docker Pull\n4.Show Docker Images\n5.Show All Docker Containers\n6.Launch A Docker Container\n7.Start Docker Container\n8.Stop Docker Container\n9.Remove A Docker Container\n10.Return to main menu")
		sub_choice=input("\nEnter Your Choice : ")
		if sub_choice=='1':
			os.system("yum install docker-ce --nobest -y")
			print("Docker sucessfully installed....")
		elif sub_choice=='2':
			img=input("Enter The Image Name To Search : ")
			os.system("docker search "+img)
		elif sub_choice=='3':
			img=input("Enter The Image Name You Want To Pull : ")
			os.system("docker pull "+img)
		elif sub_choice=='4':
			os.system("docker images")
		elif sub_choice=='5':
			os.system("docker ps -a")
		elif sub_choice=='6':
			con_name=input("Enter Name For Your Container : ")
			img=input("Enter Image Name : ")
			os.system("tput setaf 3")
			os.system("docker run -dit --name {} {}".format(con_name, img))
		elif sub_choice=='7':			
			img=input("Enter Image Name : ")
			os.system("docker start "+img)
		elif sub_choice=='8':			
			img=input("Enter Container Name : ")
			os.system("docker stop "+img)
		elif sub_choice=='9':
			img=input("Enter Container Name : ")
			os.system("docker rm -f "+img)
		elif sub_choice=='10':
			break;
		else:
			print("Oops!!! Wrong Choice, Please Try Again")
			os.system("tput setaf 2")	
#Function#3
def ApacheHTTPD():
	from tqdm import tqdm, trange
	import time 
	os.system("tput setaf 2")
	print("Hold on tight while we're configuring apache webserver for you ;)")
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("systemctl enable httpd")
	os.system("cp index.html /var/www/html")
	pbar = tqdm(total=100)
	for i in range(10):
		time.sleep(0.3)
		pbar.update(10)
	pbar.close()	
	print("\n\n\t\t\t\tSuccessfully Finished!!!\n\n")
	while(1):
		print("Do you want to open localhost in browser ?\n")
		inp=input("Press Y to open\nPress N to finish and return to main menu : ")
		if(inp=='y' or inp=='Y'):
			os.system("firefox 127.0.0.1")
			break;
		elif(inp=='n' or inp=='N'):
			break;
		else:
			break;

os.system("tput setaf 3")
print("-".center(150,"-"))
os.system("tput setaf 2")
welcome="Linux Menu Program Using Python"
print(welcome)
while True:
	os.system("tput setaf 3")
	print(" \n 1.Basic Linux Commands \n 2.Docker \n 3.Apache HTTPD Configuration\n 4.Exit \n")
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

		elif main_choice=='3':
			ApacheHTTPD()
			break;
		else:
			os.system("tput setaf 6")
			print("\n\nWrong command!!Please try again\n\n")
			break;
		
		
	else:
		print("Wrong command!!Please try again")
		break
