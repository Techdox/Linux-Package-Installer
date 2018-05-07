import os, time, collections

DEBUG = True

install = {
	"Steam": 'sudo apt install steam',
	'Chromium': 'sudo apt install chromium-browser',
	'Spotify': 'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886 0DF731E45CE24F27EEEB1450EFDC8610341D9410 && echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list && sudo apt-get update && sudo apt-get install spotify-client',
	'Sublime':	'sudo apt install sublime-text',
	'VLC Media Player': 'sudo apt install vlc',
	'GIMP':	'sudo apt install gimp',
	'Dropbox': 'sudo apt install dropbox',
	'Visual Studio Code': 'curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && sudo sh -c \'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list\' && sudo apt update && sudo apt install code',
	'Kodi Media Player': 'sudo apt install kodi',
}
install = collections.OrderedDict(sorted(install.items()))
numberofitems = len(install.items())

selecteditems = []

def getinput(get_string):
	try:
		return int(get_string)
	except Exception:
		return -1

def render_menu():
	print(35 * '-')	
	print ("    TECHDOX - PACKAGE - INSTALLER")
	print ('''
\t      \  |  /
\t       \ | /
\t  ______\|/______
\t /_______n_______\\
\t~~~~~~~~~~~~~~~~~~~''')
	print (35 * '-')
	print ("Install:")
	for i in range(numberofitems):
		print ('{}\t[{}] {}'.format(i+1, 'X' if i in selecteditems else ' ',list(install.keys())[i]))
	print (35 * '-')
	print("Enter q to quit, Enter c to confirm selection")

def help_message():
	print("Some helpful infomation ;)")
	print("Press enter to continue")

def parse_input(choice):
	if choice == 'c':
		return True
	elif choice == 'q':
		print("Exiting!")
		quit()
	elif choice == "help":
		help_message()
		input()


	choice = getinput(choice)-1
	if getinput(choice) >= numberofitems or getinput(choice) < 0:
		print ('Please Follow The INSTRUCTIONS!')
	else:
		selecteditems.append(choice)
	
	return False
	

def run_installers():
	for i in selecteditems:
		if DEBUG:
			print('%s -y'%list(install.values())[i])
		else:
			os.system('%s -y'%list(install.values())[i])

		

def main():
	while True:
		render_menu()
		choice = input("Enter Your Choice [1-{}]: ".format(numberofitems)).lower()
		
		if parse_input(choice):
			run_installers()
			break

		
		

if __name__ == "__main__":
	main()
