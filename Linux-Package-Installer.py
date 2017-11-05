import subprocess
import os
import time

## Show menu ##
def render_menu():
	print (30 * '-')
	print ("   TECHDOX - PACKAGE - INSTALLER")
	print (30 * '-')
	print ("1. Install Steam")
	print ("2. Install Chromium")
	print ("3. Install Spotify")
	print ("4. Install Sublime")
	print ("5. Install VLC Media Player")
	print ("6  Install Dropbox")
	print ('7  About')
	print (30 * '-')

loop=True

while loop:
	render_menu()
## Get input ###
	choice = input('Enter your choice [1-6] : ')
 
### Convert string to int type ##
	choice = int(choice)
	 
	### Take action as per selected menu-option ###
	if choice == 1:
	        os.system('sudo apt install steam -y')
	elif choice == 2:
	        os.system('sudo apt install chromium-browser -y')
	elif choice == 3:
	        os.system ("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886 0DF731E45CE24F27EEEB1450EFDC8610341D9410 && echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list && sudo apt-get update && sudo apt-get install spotify-client -y")
	elif choice == 4:
			os.system ('sudo apt install sublime-text -y')
	elif choice == 5:
			os.system ('sudo apt install vlc -y')
	elif choice == 6:
			os.system ('sudo apt install dropbox -y')
	elif choice == 7:
			print ('Techdox installer is an Open Source Program that makes it quick and easy to install common programs - Website techdox.nz')
			time.sleep(10)
	else:    ## default ##
	        print ("Invalid number. Try again...")
