import socket
import time
import socket
import shutil # to copy files
import re #to remove special chars
from linecache import getline
from linecache import clearcache
import os # for testing existanz of a file
import random
from _thread import start_new_thread
#konstanten
whiteWords = ['ein','eine','einer','eines','der','die','das','halt','des','dem','dessen','nem','enm','nes','ner','rer','rem','res','denn','los','a','e','i','o','u']
noAwnser =['Ich kenne keine Antwort','Darauf kann ich leider nicht reagieren']
Ansatz = ['Hallo']

host = '192.168.8.120'
port = 80

playerList = []
# copy ,'','','','','','','','','','','','',''
#VarsEnd

class c: #colors
	def p(x): #print(c.p('Hello'))
		return('\033[95m'+x+'\033[0m')
	def b(x):
		return('\033[94m'+x+'\033[0m')
	def y(x):
		return('\033[93m'+x+'\033[0m')
	def g(x):
		return('\033[92m'+x+'\033[0m')
	def r(x):
		return('\033[91m'+x+'\033[0m')



def remove(x,y,a):
        z=0
        while z<=len(x)-1:
                y = y.replace(x[z],a)
                z+=1
        return y

def user_accept(a):
	erweiterung_meines_gedaechnisses = 'on'
	li=1
	path = 0
	setF = 'true'
	kaese = "com"
	f = ''
	def nanrep(sentence):
		global whiteWords
		global Ansatz
		global noAwnser
		nonlocal kaese
		nonlocal setF
		nonlocal li
		nonlocal erweiterung_meines_gedaechnisses
		nonlocal path
		nonlocal f
		#Code
		sen = sentence
		sen = sen.lower()
		sen = ''.join(re.findall(r"[a-z0-9]*", sen)).replace("  "," ")
		sen = remove(whiteWords, sen,'')
		# print(sen)
		if setF == 'true':
			f = './storage/'+sen
			setF = 'false'
			fortsetzung = 'false'
			li=1
		else:
			fortsetzung = 'true'
		while 'true':
		#if sen == 'help'
			if sen == 'ichhlfdr':
				erweiterung_meines_gedaechnisses = 'on'
				return('Danke')
			elif not sen :
				#print ('String ist leer')
				setF= 'true'
				return(random.choice(Ansatz))
			#Readfile
			elif os.path.exists(f):
				Known='true'
				if fortsetzung == 'true':
					#print('fort')
					li=li+1
					line = getline(f,li).strip().split(';')
					#print(line)
					if sen in line:
						#print('sen is in line')
						li=li+1
						paths = 0
						while len(line)-1 >= paths:
							if line[paths] == sen:
								path = paths
								#print(path)
								break
							else:
								paths =paths +1
					else:
						li=1
						f='./storage/'+ sen
						if os.path.exists(f):
							return(getline(f,li))			
						else:
							Known = 'false'
				if Known is 'true':
					#print(li)
					#print(path)
					rep0 = getline(f,li).split(';')
					if len(rep0)-1 >= path:
						return(rep0[path].strip())
					else:
						return(rep0[0]+ '\n')
					break
			li=1

			#editmode
			#createmodus
			if  erweiterung_meines_gedaechnisses == 'on':
				cl.sendall(('Keine Antwort vorhanden: Helfen (y), Abbruch (n), Synonym(s)').encode('UTF-8'))
				sen1 , addr = cl.recvfrom(1024)
				sen1 = sen1.decode('utf-8')
				#createFile
				if sen1 == 'y':
					Erweiterungsmodus = 'on'
					f = open('./storage/' + sen, 'w')
					cl.sendall(('Ich bin bereit.\n').encode('utf-8'))
					createFileInput, addr = cl.recvfrom(1024)
					createFileInput = createFileInput.decode('utf-8')
					createFileInput = createFileInput.replace('ä','ae')
					createFileInput =createFileInput.replace('ö','oe')
					createFileInput =createFileInput.replace('ü','ue')
					createFileInput =createFileInput.replace('ß','ss')
					f.write(createFileInput+'\n')
					f.close()
					
					while 'true':
						cl.sendall(' '.encode('UTF-8'))
						weiter, addr = cl.recvfrom(1024)
						weiter = weiter.decode('utf-8')
						if weiter == "n":
							setF='true'
							return('Dateibearbeitung wurde beendet')
						elif kaese == "com":
							weiter =weiter.lower()
							weiter =''.join(re.findall(r"[a-z0-9;]*", weiter)).replace("  "," ")
							weiter = remove(whiteWords,weiter,'')
							kaese = "Person"
						else:
							weiter = weiter.replace('ä','ae')
							weiter =weiter.replace('ö','oe')
							weiter =weiter.replace('ü','ue')
							weiter =weiter.replace('ß','ss')
							kaese = "com"
						file = open('./storage/' + sen,'a')
						file.write(weiter + '\n')
						file.close()
				#createSysnonym
				elif sen1=='s':
					cl.sendall(('Gib das Wort ein, das ich schon kenne').encode('utf-8'))
					normalName, addr = cl.recvfrom(1024)
					normalName = normalName.decode('utf-8')
					normalName = normalName.lower()
					normalName = ''.join(re.findall(r"[a-z0-9]*", normalName)).replace("  "," ")
					normalName = remove(whiteWords, normalName,'')
					while True:
						if normalName == 'n':
							synRep = 'Wir koennen dann wieder reden\n'
							break
						elif os.path.exists('./storage/'+normalName):
							shutil.copy2('./storage/'+normalName,'./storage/'+sen)
							synRep = 'Das Synonym wurde  erfolgreich hinzugefuegt\n'
							break
						else:
							cl.sendall(('Diesen Anfang einer Konversation kenne ich nicht').encode('UTF-8'))
							normalName, addr = cl.recvfrom(1024)
							normalName = normalName.decode('utf-8')
					setF='true'
					return(synRep)
				else:
					setF='true'
					return(random.choice(Ansatz))
			else:
				setF='true'
				return(random.choice(noAwnser))
			break
	running = True
	cl,addr =s.accept()
	start_new_thread(user_accept,(9,))
	name , addr = cl.recvfrom(1024)
	name = name.decode()
	conFile = open('./conversations/' + name,'w')
	playerList.append(name)
	print (c.r(name + ' connected'))
	time.sleep(0.5)
	cl.sendall(b'Hello, I am NAN')
	conFile.write(c.y('NAN: ')+'Hello, I am NAN\n')
	while running:
		try:
			conFile = open('./conversations/' + name,'a')
			data, addr = cl.recvfrom(1024)
			data = data.decode('utf-8')
			conFile.write(c.g(name)+': '+data+'\n')
			if 'q' in str(data):
				running = False
			rep = nanrep(data).strip()
			conFile.write(c.y('NAN:')+rep+'\n')
			cl.sendall(rep.encode('utf-8'))
			conFile.close()
		except ConnectionResetError:
			print(c.r(name+" disconnected"))
			playerList.remove(name)
			break		
	
def screenManager(a):
	global screenStatusChanged
	global screenStatus
	filePath = 'notSet'
	screenStatusChanged = False
	screenStatus = 0
	li = 1
	while True:
		clearcache()
		if screenStatusChanged == True:
			screenStatusChanged = False
			if screenStatus == 0:
				for x in range(100):
					print('')
			else:
				li = 1
				try:
					filePath = './conversations/' + playerList[screenStatus -1]
				except:
					print(c.r("This screen doesn't exists"))
		if getline(filePath,li) != '' and screenStatus !=0:
			print(getline(filePath,li).strip())
			li += 1

#Code
prev_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	prev_s.close((host,port))
except:
	pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
print (c.r('Server started'))
s.listen(100)
start_new_thread(screenManager,(9,))# 9 is not important but this command needs a number
start_new_thread(user_accept,(9,))
while True:
	command = input()
	command = command.split(' ')
	if command[0] == 'help':
		print(c.r('\nplayer -list all Players'))
		print(c.r('screen - can change between the conversation'))
	elif command[0] == 'player':
		print(c.r('\nSpieler online: '+ str(len(playerList))))
		print(c.r('Spieler: '+str(playerList)))
	elif command[0] == 'screen':
		try:
			if command[1] == 'help':
				print(c.r('\nusage:'))
				print(c.r('screen <name of player>'))
				print(c.r('or'))
				print(c.r('screen 0 -to get an empty screen'))
			else:
				if command[1] == '0':
					screenStatus = 0
					
				else:
					screenStatus = int(command[1])
					
				screenStatusChanged = True
		except:
			print(c.r('\ntype "screen help" to get help'))
	elif command[0] == 'python':
		os.system('python3')
	else:
		print(c.r('\nUnknown command. Try "help".'))
	
