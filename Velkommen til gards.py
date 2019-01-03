def start():
	print:('''
	***********************
	* Velkommen te gards! *
	***********************				  
	''')

global høns
høns = 0
global korn
korn = 1000
global polakker
polakker = 3
global konto
konto = 10000 
global helse
helse = 10 

## spillfunksjoner
def sjekkstatistikk():
	print('''
		***********************''')
	print('her er helsen din\n', helse)
	print('pengene på kortet', konto)
	print('her er oversikt over hønsene', høns)
	print('her er kornmassen', korn)


def Fortset():
	x = input('dersom du vil fortsette, send 0')
	return x

def prompt():
	x=input("Skriv inn en av kommandoene")
	return x

## rommene****************************************************************************************************
## ståvo
def ståvo():
	print('''Du er i ståvo di, med ei lita kopp konjakk og kaffi, som du plar på føremiddagen.
		''')
	print('''Aksjonsmuligheter:
		1. Gå ut
		2. Sove
		9. Sjekke helse
		''')
	command = prompt ()
	if command == '2':
		print("*************")
		print("Du er frisk. (",helse,"/",helse,")")
	elif command == '1':
		ute ()
	elif command == '9':
		sjekkstatistikk()
		ståvo ()

	else:
	 ståvo ()

## Låven
def Låven():
	print('''Du er i låven, her lukte da vondt, sikker på at du ikkje vil inn og ha deg ein konjakk og kaffi?''')
	print('''aksjonsmuligheter:
		1. Gå inn igjen og drikka konjakk
		2. se til hønsene 
		3. Gå ned til bygdahuset
		9. sjekke status
		''')
	command = prompt()
	if command == '1':
		ståvo ()
	elif command == '2':
		hønseburet ()
	elif command =='3':
		bygdahuset()
	elif command == '9':
		sjekkstatistikk()
		Fortset()
		låven()
	else:
		låven()

start()





