#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Schedule de tâches V2
#######################################################

from scapy.all import sendrecv
import wx
import threading, Queue, time
import GestionFich
import AnaTrames
import LectTrames
from MyIHM import *
import sys

################################## Tache Lect_Trame ##################################
# Cette tache ne fait que lire les données sur le support physique
# et envoie le résultat à la tache d'analyse des trames
# En entrée : Le nombre de trames à analyser.
#	Il est possible de prendre les données dans un fichier ou directement sur le réseau
# En sortie : Les données récupérées sur le réseau et transférées en brute
#			  Le drapeau de fin, la tuyau de communication avec la tache analyse de trames

class TaskLectTrame( threading.Thread ):
	#Si Trame_a_analyser = None ==> Sniff sur le réseau
	#Si Trame_a_analyser = "nom d'un fichier" ==> Lecture dans le fichier

	def __init__( self, trameAAnalyser=None, nbr=1, queueToAnatrames=None, stopFlag=None):
		threading.Thread.__init__(self)

		#Si trame_a_analyser = None, on scanne le réseau, sinon, on va lire les données dans un fichier
		self.maTrameAAnalyser = trameAAnalyser
		self.count = nbr
		self.queueLectTrameToAnatrames = queueToAnatrames
		self.stopEvent = stopFlag

		self.setName(TaskLectTrame)

		#print "trameAAnalyser = ", self.maTrameAAnalyser, "\n"
		#print "Nbr = ", self.count, "\n"
		#print "queue_to_anatrames = ", self.queueLectTrameToAnatrames, "\n"
		#print "stopFlag = ",self.stopEvent, "\n"
		#print "Task Name = ", self.getName
		
	def run(self):
		i=0
		while (self.stopEvent.is_set()==False):
			i=i+1
			data=None
			#Si sniff sur le reseau
			if self.maTrameAAnalyser==None :
				data = LectTrames.Sniff_Reseau_Win()
			#Sinon lire dans le fichier fourni
			else :
				data = sendrecv.sniff(count=self.count, offline=self.maTrameAAnalyser)
			if data != None:
				try:
					#print "Data dans Task_Lect_Trame = \n",data," \n"
					self.queueLectTrameToAnatrames.put(data)
				except:
					print"TaskLectTrame Can't write in the queue : %s \n" %(sys.exc_info()[0])
			else :
				#print "No DATA dans TaskLectTrame"
				pass
			#print "I = ", i,"\n"
			#print "DATA dans TaskLectTrame = \n", data

			#if (i == 100):
			#	self.stopEvent.set()
				#print "END TaskLectTrame : %s", self.get_ident(),"\n"
				#break

			time.sleep(0.2)
		#print time.strftime("%d/%m/%Y  %H:%M:%S"),"   END TaskLectTrame\n"
		print "   END TaskLectTrame\n"


################################## Tache AnaTrames ##################################
#Tache qui analyse les trames recues. Si ce sont des trames ASTERIX CAT34/48, envoie le résultat de l'analyse à la tache controleur.
#Entree : 	le canal de communication entre Lecture_Trames et Ana_Trames
#			le flag d'arret de la tache
#Sortie :	Les donnees analysees, et pretes a etre envoyees a la tache controleur

class TaskAnaTrames( threading.Thread ):
	def __init__( self, fromLectTrames=None, stopFlag=None ):
		threading.Thread.__init__(self)
		self.maTrameAAnalyser=""
		#self.maTrameAAnalyser = trameAAnalyser
		self.trameAnalysee = AnaTrames.TrameAsterix3448()
		self.setName(TaskAnaTrames)
		self.queueLectTrameToAnatrames = fromLectTrames
		self.stopEvent = stopFlag
		
	def run(self):
		while (self.stopEvent.is_set()==False):
			self.maTrameAAnalyser=None
			if self.queueLectTrameToAnatrames.empty()== False:
				try:
					self.maTrameAAnalyser = self.queueLectTrameToAnatrames.get()
					self.queueLectTrameToAnatrames.task_done()
					#print " Trame = ",self.maTrameAAnalyser
				except:
					print"TaskAnaTrames Can't read in the queue : %s \n" %(sys.exc_info()[0])
	
				#self.Traitement_Trame(self.maTrameAAnalyser)
			
			if self.maTrameAAnalyser!=None:
					self.trameAnalysee = AnaTrames.MainAppAnaTrames(self.maTrameAAnalyser)
					#print "DATA dans TaskAnaTrames RADAR = \n", self.trameAnalysee.Radar,"\n"
					#print "DATA dans TaskAnaTrames = \n", self.trameAnalysee.show(),"\n"
			else :
				#print "No DATA IN queueLectTrameToAnatrames\n"
				pass
		
		#print time.strftime("%d/%m/%Y  %H:%M:%S"),"   END TaskAnaTrames\n"
		print"   END TaskAnaTrames\n"
	
	#Fonction temporaire de traitement de la trame afin de dissocier chaque trame
	def traitement_trame(self, maTrame):
		result=()
		#print"Ma Trame dans traitement_trame = ", maTrame
		#result = maTrame.split(Dot3)
		#print "Mon split = ", result
		

	

################################## Tache Controleur ##################################
class TaskControleur( threading.Thread ):
	def __init__( self, stopFlag=None, toIHM=None, fromIHM=None, toGestionFich=None, fromGestionFich=None, fromAnaTrame=None):

		threading.Thread.__init__(self)
		self.setName(TaskControleur)

		#Initialisation des files d'attente
		self.queueIHMToControler = fromIHM
		self.queueControlerToIHM = toIHM

		self.queueGestFichToControler = fromGestionFich
		self.queueControlerToGestFich = toGestionFich

		self.queueAnaTrameToControler = fromAnaTrame
		#self.queueControlerToAnaTrame = toAnaTrame

		#Drapeau de fin de tache
		self.stopEvent = stopFlag


	def run(self):
		compt=0 	#A chaque boucle du "Run", on va vérifier un canal de communication différent.
		while (self.stopEvent.is_set()==False):
			data=None
			#print "HELLO From Controleur"
			
			#Verifier la file d'attente IHM -> Controleur
			if (compt==0):
				#Si la file d'attente est remplie, on recupere les infos
				if (self.queueIHMToControler.empty()==False):
					try:
						(commande,data)=self.queueIHMToControler.get()
						self.queueIHMToControler.task_done()
						#print "TaskControleur commande = ", commande, "\n"
					except:
						print "Can't get data in queueIHMToControler : %s \n" %(sys.exc_info()[0])

					#En fonction de l'info recuperee, on execute la fonction ad hoc		
					commande = {"histo_R": self.histo_affiche(commande),
								#"conf_R" : self.Conf_Affiche(commande),
								#"conf_W" : self.Conf_Save(),
								#"pref_R" : self.Pref_Affiche(),
								#"pref_W" : self.Pref_Save(),
								#"aide_R" : self.Aide_Affiche(),
					}
				time.sleep(0.5)
				
			#Verifier la file d'attente Anatrame -> Controleur
			if (compt==1):
				#Si la file d'attente est remplie, on recupere les infos
				if (self.queueAnaTrameToControler.empty()==False):
					try:
						(commande,data)=self.queueAnaTrameToControler.get()
						self.queueAnaTrameToControler.task_done()
					except:
						print "Can't get data in queueAnaTrameToControler : %s \n" %(sys.exc_info()[0])

					#En fonction de l'info recuperee, on execute la fonction ad hoc		
					commande = {
								#"trame": self.Traitement_data(data),
								#"histo_W": self.Ecrire_Histo(self.data),
								#"conf_R" : self.Conf_Affiche(commande),
								#"conf_W" : self.Conf_Ecrire(),
								#"pref_R" : self.Pref_Affiche(),
								#"pref_W" : self.Pref_Ecrire(),
								#"aide_R" : self.Aide_Affiche(),
					}
				time.sleep(0.5)
			
			#Verifier la file d'attente Gestion Fichier -> Controleur
			if (compt==2):
				pass
			
			compt=(compt+1)%3 
		
		#Arret de la tache
		#print time.strftime("%d/%m/%Y  %H:%M:%S"),"   END TaskControleur\n"
		print"   END TaskControleur\n"

	def histo_affiche(self, commande):
		#Envoi de l'info vers la tache de gestion des fichiers
		#print"HELLO from affiche_fichier \n"
		try:
			self.queueControlerToGestFich.put((commande,None))
			#print "data in Controler_to_Gest \n"
		except:
			print "Can't put in queueControlerToGestFich : %s \n" %( sys.exc_info()[0] )
		
		#Attendre la reponse du gestionnaire de fichiers
		while(self.queueGestFichToControler.empty()==True):
			time.sleep(0.2)
			#print "Wait in Histo_Affiche ============= \n"
		(commande,data)=self.queueGestFichToControler.get()
		#print time.strftime("%d/%m/%Y  %H:%M:%S"),"   Histo_Affiche apres get \n"
		self.queueGestFichToControler.task_done()
		try:
			self.queueControlerToIHM.put((commande,data))
			#print "DATA in queueControlerToIHM\n"
			#self.dataForIHMFlag.set()
		except:
			print "Can't put data in queueControlerToIHM : %s \n" %(sys.exc_info()[0])
					
	def histo_ecrire(self, data):
		#Envoi les infos a ecrire dans le fichier historique
		print"Data A Ecrire dans le fichier Histo = ", data
		try:
			self.queueControlerToGestFich.put(("histo_W",data))
		except:
			print "Can't put in queueControlerToGestFich : %s \n" %( sys.exc_info()[0] )
		
################################## Tache GestionFich ##################################

class TaskGestionFich(threading.Thread):
	
	def __init__( self, stopFlag=None, toControler=None, fromControler=None ):
		
		threading.Thread.__init__(self)
		self.setName(TaskGestionFich)
		self.stopEvent = stopFlag
		self.queueToControler = toControler
		self.queueFromControler = fromControler
		self.Fichier_Historique = "Historique.log"

	def run(self):
		#print "DANS ", self.getName(),"\n"			
		#data=GestionFich.Lire_Fichier("Historique.log")
		while (self.stopEvent.is_set()==False):
			if self.queueFromControler.empty()==False:
				try:
					(commande,data) = self.queueFromControler.get()
					self.queueFromControler.task_done()
					#print"TaskGestionFich Commande = ", commande, "\n"
					#print "data = ", data, "\n"
					commande = {
						#L'utilisateur demande à visualiser le fichier historique
							"histo_R": self.visu_fichier_histo(self.Fichier_Historique, commande),
									#"histo_W": Histo_Ecrire(self.Fichier_Historique, data)
									#"conf_R" : self.Lire_Envoyer("Configuration", commande),
									#"conf_W" : Conf_Ecrire,
									#"pref_R" : Pref_Affiche,
									#"pref_W" : Pref_Ecrire,
									#"aide_R" : Aide_Affiche,
					}
				except:
					print "Can't get data in queue From Controler To Gestion Fich : %s \n" %(sys.exc_info()[0])

		print"   END TaskGestionFich \n"

	def visu_fichier_histo(self, monFichier, commande):
		data = GestionFich.Lire_Fichier(monFichier)
		try:
			self.queueToControler.put((commande,data))
		except:
			print "Can't put in queue From Gestion Fich To Controler : %s \n" %( sys.exc_info()[0] )
		
	def extraction_nom_radar(self,data):
		pass


################################## MainAppIHM ##################################
	
class MainAppIHM(wx.App):
	def OnInit(self):
		print "TASKS MainAppIHM ON INIT \n "

		#Instanciation de l'évènement pour arreter toutes les taches.
		self.stopEvent = threading.Event()
		self.stopEvent.clear()
		#On averti la tache IHM qu'il y a des donnees dans la file d'attente
		self.dataForGUI = threading.Event()
		self.dataForGUI.clear()
				
		#Instanciation des canaux de communication entre les taches
		#self.queue_Test1_to_Test2 = Queue.Queue()
		self.queueLectTrameToAnatrames = Queue.Queue()
		self.queueControlerToIHM = Queue.Queue()
		self.queueIHMToControler = Queue.Queue()
		self.queueControlerToGestionFich = Queue.Queue()
		self.queueGestionFichToControler = Queue.Queue()
		self.queueAnaTramesToControler = Queue.Queue()
	
		#If Trame_a_analyser = None, Sniffing network, else reading the file
		#self.Trame_a_analyser = None
		self.trameAAnalyser = "captures SIRSUR"
		self.nbr=4
		
		############### Lancement des taches ###############

		try:
			print"Lancement TaskGestionFich\n "
			self.MyTaskGestionFich = TaskGestionFich(stopFlag = self.stopEvent, toControler = self.queueGestionFichToControler, fromControler = self.queueControlerToGestionFich)
			self.MyTaskGestionFich.start()
		except:
			print "Error: unable to start thread MyTaskGestionFich  : %s \n" %(sys.exc_info()[0])
			self.stopEvent.set()

		try:
			print"Lancement TaskControleur\n "
			self.MyTaskControleur = TaskControleur(stopFlag = self.stopEvent, toIHM = self.queueControlerToIHM, fromIHM = self.queueIHMToControler, fromGestionFich = self.queueGestionFichToControler, toGestionFich = self.queueControlerToGestionFich, fromAnaTrame=self.queueAnaTramesToControler)
			self.MyTaskControleur.start()
		except:
			print "Error: unable to start thread TaskControleur  : %s \n" %(sys.exc_info()[0])
			self.stopEvent.set()

		try:
			print"Lancement TaskLectTrame\n "
			self.MyTaskLectTrame = TaskLectTrame( trameAAnalyser = self.trameAAnalyser, nbr = self.nbr, queueToAnatrames = self.queueLectTrameToAnatrames, stopFlag = self.stopEvent )
			self.MyTaskLectTrame.start()
		except:
			print "Error: unable to start thread TaskLectTrame : %s \n" %(sys.exc_info()[0])
			self.stopEvent.set()

		try:
			print"Lancement TaskAnaTrames\n "
			self.MyTaskAnaTrames = TaskAnaTrames(fromLectTrames=self.queueLectTrameToAnatrames, stopFlag=self.stopEvent)
			self.MyTaskAnaTrames.start()
		except:
			print "Error: unable to start thread TaskAnaTrames  : %s \n" %(sys.exc_info()[0])
			self.stopEvent.set()
		
		#Si les autres taches se sont lancées sans problème, on lance l'IHM
		if self.stopEvent.is_set() == False:
			print "Lancement de l'IHM\n"
			self.mainfrm = MaFramePrincipale(parent=None, queueControlerToIHM = self.queueControlerToIHM, queueIHMToControler = self.queueIHMToControler)
			self.SetTopWindow(self.mainfrm)
			self.mainfrm.Show()
		else :
			print"ERREUR DE LANCEMENT de l'IHM : %s \n" %(sys.exc_info()[0])
		
		return True

	def OnExit(self):
		print "\n-----------------MON IHM ONEXIT-----------------\n"
		self.stopEvent.set()
		print "Waiting for all the threads to finish.........\n"
		self.ExitMainLoop()
		self.MyTaskLectTrame.join()
		self.MyTaskAnaTrames.join()
		self.MyTaskControleur.join()
		self.MyTaskGestionFich.join()

		print time.strftime("%d/%m/%Y  %H:%M:%S"),"     ALL TASKS HAVE JOINED \n"
		
		#Facultatif
		wx.Exit()
		
	

########################  PROGRAMME PRINCIPAL #######################
if __name__ == '__main__':
	
	import os
	#####  Redirection des sorties pour debuggage
	#On efface le contenu du fichier stdout.log avant de lancer une nouvelle exécution.
	os.remove("stdout.log")
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')

	print"\n-----------------MON MAIN------------------\n"
	print time.strftime("Lancement le %d/%m/%Y  %H:%M:%S")
	print"Operating System = ", sys.platform
	
	################ Lancement du GUI
	app = MainAppIHM(redirect = True, filename = 'stdout.log')
	app.MainLoop()


	print time.strftime("Fin le %d/%m/%Y  %H:%M:%S")
	print"---------------- FIN DU PROGRAMME --------------------\n"

	############### Retablissement des sorties
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
