import socket
import time
import socket
import time
import shutil # to copy files
import re #to remove special chars
import linecache
import os.path # for testing existanz of a file
import random

#Vars
noAwnser =['Ich kenne keine Antwort\n','Darauf kann ich leider nicht reagieren\n']
rot = ' '
weiss = ' '
erweiterung_meines_gedaechnisses = 'on'
Ansatz = ['Hallo\n']
li=1
path = 0
setF = 'true'
kaese = "com"
# copy ,'','','','','','','','','','','','',''
whiteWords = ['ein','eine','einer','eines','der','die','das','halt','des','dem','dessen','nem','enm','nes','ner','rer','rem','res','denn','los','a','e','i','o','u']
#VarsEnd
def nanrep(sentence):
	global setF
	global path
	global li
	global kaese
	global Ansatz
	global weiss
	global whiteWords
	global rot
	global noAwnser
	global f
	global erweiterung_meines_gedaechnisses
	#Code
	sen = sentence
	sen = sen.lower()
	sen = ''.join(re.findall(r"[a-z0-9]*", sen)).replace("  "," ")
	sen = remove(whiteWords, sen,'')
	print(sen)
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
				line = linecache.getline(f,li).strip().split(';')
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
						return(linecache.getline(f,li))			
					else:
						Known = 'false'
			if Known is 'true':
				#print(li)
				#print(path)
				rep0 = linecache.getline(f,li).split(';')
				if len(rep0)-1 >= path:
					return(rep0[path].strip() + '\n\n')
				else:
					return(rep0[0]+ '\n')
				break
		li=1

		#editmode
		#createmodus
		if  erweiterung_meines_gedaechnisses == 'on':
			cl.sendall((rot +'Keine Antwort vorhanden: Helfen (y), Abbruch (n), Synonym(s)'+weiss).encode('UTF-8'))
			sen1 , addr = cl.recvfrom(1024)
			sen1 = sen1.decode('utf-8')
			#createFile
			if sen1 == 'y':
				Erweiterungsmodus = 'on'
				f = open('./storage/' + sen, 'w')
				cl.sendall((rot +'Ich bin bereit.\n'+ weiss).encode('utf-8'))
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
				cl.sendall((rot+'Gib das Wort ein, das ich schon kenne'+weiss).encode('UTF-8'))
				normalName, addr = cl.recvfrom(1024)
				normalName = normalName.decode('utf-8')
				while 'true':
					if normalName == 'n':
						synRep = 'Wir koennen dann wieder reden\n'
						break
					elif os.path.exists('./storage/'+normalName):
						shutil.copy2('./storage/'+normalName,'./storage/'+sen)
						synRep = 'Das Synonym wurde  erfolgreich hinzugefuegt\n'
						break
					else:
						cl.sendall((rot+'Diesen Anfang einer Konversation kenne ich nicht'+weiss).encode('UTF-8'))
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

def remove(x,y,a):
        z=0
        while z<=len(x)-1:
                y = y.replace(x[z],a)
                z+=1
        return y

#Code
host = '192.168.8.120'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

running = True
print ('Server started')
s.listen(5)
cl,addr =s.accept()
name , addr = cl.recvfrom(1024)
print (name.decode() , 'connected')
cl.sendall(b'Hello, I am NAN')
while running:
				#try:
                data, addr = cl.recvfrom(1024)
                data = data.decode('utf-8')
                print(data)
                if 'q' in str(data):
                        running = False
                rep = nanrep(data)
                print(rep)
                cl.sendall(rep.encode('utf-8'))
				#except:
                pass




        

