#importe
import linecache
import os.path # for testing existanz of a file
import random
import time
import shutil # to copy files
import re #to remove special chars

#Definitionen
def remove(x,y,a):
        z=0
        while z<=len(x)-1:
                y = y.replace(x[z],a)
                z+=1
        return y
#Vars
noAwnser =['Ich kenne keine Antwort\n','Darauf kann ich leider nicht reagieren\n']
nan_rep = '\nHallo, Ich bin Nan\n\n'
rot = ' '
weiss = ' '
erweiterung_meines_gedaechnisses = 'on'
Ansatz = ['Hallo\n']
li=1
path = 0
setF = 'true'
kaese = "com"
#to copy ,'','','','','','','','','','','','',''
whiteWords = ['ein','eine','einer','eines','der','die','das','halt','des','dem','dessen','nem','enm','nes','ner','rer','rem','res','denn','los','a','e','i','o','u']

#Code
if not os.path.exists('./storage'):
        os.makedirs('./storage')
        
while 'true':
        sen = input(rot+nan_rep+'\n'+weiss)
        sen = sen.lower()
        #print('dein Text tief:'+sen)
        sen = ''.join(re.findall(r"[a-z0-9]*", sen)).replace("  "," ")
        #print('dein Text ohne Sonderzeichen:'+sen)
        sen = remove(whiteWords, sen,'')
        #print('dein Text ohne bestimmte Wörter:'+sen)
        if setF == 'true':
                f = './storage/'+sen
                setF = 'false'
                fortsetzung = 'false'
                li=1
        else:
                fortsetzung = 'true'
        if sen == 'bsbld':
                break
        
        while 'true':
        #if sen == 'help'
                if sen == 'ichhlfdr':
                        erweiterung_meines_gedaechnisses = 'on'
                        nan_rep = 'Danke'
                        break
                elif not sen :
                        #print ('String ist leer')
                        setF= 'true'
                        nan_rep=random.choice(Ansatz)
                        break

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
                                                nan_rep = linecache.getline(f,li)
                                                break
                                                
                                        else:
                                                Known = 'false'
                        if Known is 'true':
                                #print(li)
                                #print(path)
                                rep0 = linecache.getline(f,li).split(';')
                                if len(rep0)-1 >= path:
                                        nan_rep = rep0[path].strip() + '\n\n'
                                else:
                                        nan_rep=rep0[0]+ '\n'
                                break

                        
                        

                li=1
                #editmode
                #createmodus
                if  erweiterung_meines_gedaechnisses == 'on':
                        sen1 = input(rot +'Keine Antwort vorhanden: Helfen (y), Abbruch (n), Synonym(s)'+weiss)
                        #createFile
                        if sen1 == 'y':
                                Erweiterungsmodus = 'on'
                                f = open('./storage/' + sen, 'w')
                                createFileInput = input(rot +'Ich bin bereit.\n'+ weiss)
                                createFileInput = createFileInput.replace('ä','ae')
                                createFileInput =createFileInput.replace('ö','oe')
                                createFileInput =createFileInput.replace('ü','ue')
                                createFileInput =createFileInput.replace('ß','ss')
                                f.write(createFileInput+'\n')
                                f.close()
                                
                                while 'true':
                                        weiter = input(' ')
                                        if weiter == "n":
                                                nan_rep ='Dateibearbeitung wurde beendet'
                                                setF='true'
                                                break
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
                                normalName = input(rot+'Gib das Wort ein, das ich schon kenne'+weiss)
                                while 'true':
                                        if normalName == 'n':
                                                synRep = 'Wir koennen dann wieder reden\n'
                                                break
                                        elif os.path.exists('./storage/'+normalName):
                                                shutil.copy2('./storage/'+normalName,'./storage/'+sen)
                                                synRep = 'Das Synonym wurde  erfolgreich hinzugefuegt\n'
                                                break
                                        else:
                                                normalName= input(rot+'Diesen Anfang einer Konversation kenne ich nicht'+weiss)
                                nan_rep = synRep
                                setF='true'
                        else:
                                nan_rep=random.choice(Ansatz)
                                setF = 'true'
                else:
                        nan_rep = random.choice(noAwnser)
                        setF='true'
                break

print (rot +'Ich wuensche dir noch einen intellektuellen Tag\nHoffentlich sehen wir uns bald wieder')
time.sleep(3)


