import subprocess
import os
import time

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
numberofitems = len(install.values())
def getinput(get_string):
	try:
		return int(input(get_string))
	except Exception as ex:
		return - 1

def render_menu():
	print (35 * '-')
	print ("   TECHDOX - PACKAGE - INSTALLER")
	print ('''
\t      \  |  /
\t       \ | /
\t  ______\|/______
\t /_______n_______\\
\t~~~~~~~~~~~~~~~~~~~''')
	print (35 * '-')
	for i in range(numberofitems):
		print ('%i Install %s'%(i+1,install.keys()[i]))
	print (30 * '-')

while True:
	render_menu()
	choice = getinput('Enter Your Choice [1-%i]: '%(numberofitems))-1
	if choice >= numberofitems or choice < 0:
		print ('Please Follow The INSTRUCTIONS!')
		continue
	os.system('%s -y'%install.values()[choice])
