#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Schedule de tâches V1
#######################################################

from scapy.all import sendrecv
import wx
import threading, Queue, time
#import GestionFich
import AnaTrames
import LectTrames
from MyIHM import MaFramePrincipale

import sys
#####  Redirection des sorties pour debuggage
sys.stdout = open("stdout.log", 'a')
sys.stderr = open("stdout.log", 'a')

class Task_Lect_Trame( threading.Thread ):
	#Si Trame_a_analyser = None ==> Sniff sur le réseau
	#Si Trame_a_analyser = "nom dun fichier" ==> Lecture dans le fichier

	def __init__( self, Trame_a_analyser= None, N=1 ):
		threading.Thread.__init__(self)
		print "Tasks.Task_Lect_Trame.INIT\n"
		self.MaTrame_a_analyser = Trame_a_analyser
		self.count = N
		self.setName(Task_Lect_Trame)

	def run(self):
		i=0
		while (1):
			i=i+1
			data=""
			#Si sniff sur le reseau
			if self.MaTrame_a_analyser==None :
				data = LectTrames.Sniff_Reseau_Win()
			#Sinon lire dans le fichier fourni
			else :
				data = sendrecv.sniff(count=self.count, offline=self.MaTrame_a_analyser)
			if data != "":
				#print "presence Data dans Task_Lect_Trame = \n",data," \n"
				print "presence Data dans Task_Lect_Trame \n"
			else :
				print "No DATA dans Task_Lect_Trame\n"
			print "I = ", i,"\n"
			#print "DATA dans Task_Lect_Trame = \n", data
			queue_LectTrame_to_AnaTrames.put(data)

			if (i == 100):
				stop_event.set()
				print "END Task_Lect_Trame\n"
				break
			if (stop_event.isSet()):
				print "END Task_Lect_Trame\n"
				break
			time.sleep(0.2)


class Task_AnaTrames( threading.Thread ):
	
	def __init__( self ):
		threading.Thread.__init__(self)
		#print "INIT task_AnaTrames\n"
		#self.MaTrame_a_analyser = Trame_a_analyser
		self.Trame_analysee = AnaTrames.TrameAsterix3448()
		self.setName(Task_AnaTrames)
		
	def run(self):
		while (1):
			self.MaTrame_a_analyser=""
			#print "DANS ", self.getName(),"\n"			
			if queue_LectTrame_to_AnaTrames.empty()== False:
				try:
					print"Queue is not empty \n"
					self.MaTrame_a_analyser = queue_LectTrame_to_AnaTrames.get()
					#print "DATA dans Task_AnaTrames = \n", self.MaTrame_a_analyser,"\n"
				except:
					print"Task_AnaTrames Can't read in the queue\n"
			#if self.MaTrame_a_analyser!="":
			#		self.Trame_analysee = AnaTrames.MainAppAnaTrames(self.MaTrame_a_analyser)
			#		print "DATA dans Task_AnaTrames RADAR = \n", self.Trame_analysee.Radar,"\n"
			#		#print "DATA dans Task_AnaTrames = \n", self.Trame_analysee.show(),"\n"
			else :
				print "No DATA IN queue_LectTrame_to_AnaTrames\n"
			if (stop_event.isSet()):
				print "END task_AnaTrames\n"
				break

class Task_Controleur( threading.Thread ):
	
	def __init__( self ):
		print "In INIT Task_Controleur\n"
		threading.Thread.__init__(self)

	def run(self):
		while (1):
			if queue_IHM_to_TaskControl.empty()==False:
				data = queue_IHM_to_TaskControl.get()
				#print "data in queue_IHM_to_TaskControl = ",data,"\n"
			
			if (stop_event.isSet()):
				print "END Task_Controleur\n"
				break



class Task_GestionFich(threading.Thread):
	def __init__( self ):
		threading.Thread.__init__(self)
		print "INIT task_GestionFich\n"
		self.setName(Task_GestionFich)
		

	def run(self):
		print "DANS ", self.getName(),"\n"			
		while (1):
			#print "Hello ici task_GestionFich ; j= %d \n" %j
			time.sleep(4)
			#Condition de sortie : Fin d'exécution de la tache
			if (stop_event.isSet()):
				print "END task_GestionFich\n"
				break

#class Task_TEST1(threading.Thread):
#	def __init__( self ):
#		threading.Thread.__init__(self)
#		print "INIT task_TEST_1\n"
#		self.setName(Task_TEST1)
#
#	def run(self):
#		item=0
#		print "DANS ", self.getName(),"\n"			
#		while (1):
#			item += 1 
#			queue_Test1_to_Test2.put(item)
#			time.sleep(0.2)
#			#Condition de sortie : Fin d'exécution de la tache
#			if (stop_event.isSet()):
#				print "END task_TEST_1, Compteur put = %d \n" %(item)
#				break
#
#class Task_TEST2(threading.Thread):
#	def __init__( self ):
#		threading.Thread.__init__(self)
#		print "INIT task_TEST_2\n"
#		self.setName(Task_TEST2)
#
#	def run(self):
#		print "DANS ", self.getName(),"\n"			
#		while (1):
#			item = queue_Test1_to_Test2.get(timeout=1)
#			print"ITEM = %d\n" %(item)
#			time.sleep(0.3)
#			#Condition de sortie : Fin d'exécution de la tache
#			if (stop_event.isSet()):
#				print "END task_TEST_2, Compteur get = %d\n" %(item)
#				break

#class Task_Main(threading.Thread):
#	def __init__(self):
#		threading.Thread.__init__(self)
#	
#	def run(self):
#		print"Tasks.Task_Main.run\n"
#		app = MainAppIHM(redirect = True, filename = 'stdout.log')
#		app.MainLoop()


#def Tasks_Launcher():
#	try:
#		print"Tasks.Tasks_Launcher\n"
#		My_task_LectTrame = Task_Lect_Trame()
#		My_task_LectTrame.start()
#	except:
#		print "Error: unable to start thread Task_Lect_Trame \n"
	
class MainAppIHM(wx.App):
	def __init__(self, mavariable=None):
		# Call the base class constructor.
		wx.App.__init__(self)
		#self.queue_to_contr = queue_to_contr
		print mavariable
		#self.tempo = mavariable

	def OnInit(self):
		#print "MON IHM "
		#self.RedirectStdio(filename = 'stdout.log')
		#print "self.tempo = ", self.tempo

		#print mavariable + "DANS ON INIT\n"
		#self.mainfrm = MaFramePrincipale(None)
		print "IN ONINIT\n"
		#wx.CallAfter(self.OnRun(self.tempo))
		
		#self.SetTopWindow(self.mainfrm)
		#self.mainfrm.Show()
		return True

	def OnRun(tempo):
		print "	ON RUN \n"
		self.mainfrm = MaFramePrincipale(None)
		self.SetTopWindow(self.mainfrm)
		self.mainfrm.Show()
		return True
		
	def OnExit(self):
		print "MON IHM EXIT"
	

########################  PROGRAMME PRINCIPAL #######################
if __name__ == '__main__':
	
	#import sys
	#
	######  Redirection des sorties pour debuggage
	#sys.stdout = open("stdout.log", 'a')
	#sys.stderr = open("stdout.log", 'a')

	print"\n-----------------MON MAIN------------------\n"
	print time.strftime("%d/%m/%Y  %H:%M:%S")
	print"Operating System = ", sys.platform

	#on instancie et on initialise l'évènement pour arreter toutes les taches.
	stop_event = threading.Event()
	stop_event.clear()

	
	#Instanciation des canaux de communication entre les taches
	#queue_Test1_to_Test2 = Queue.Queue()
	queue_LectTrame_to_AnaTrames = Queue.Queue()
	queue_TaskControl_to_IHM = Queue.Queue()
	queue_IHM_to_TaskControl = Queue.Queue()

	#If Trame_a_analyser = None, Sniffing network, else read in the file
	Trame_a_analyser = None
	#Trame_a_analyser = "captures SIRSUR"
	N=2


	############### Lancement des taches

	#try:
	#	My_task_IHM = Task_Main()
	#	My_task_IHM.start()
	#except:
	#	print "Error: unable to start thread Task_Main \n"

	#try:
	#	#My_task_LectTrame = Task_Lect_Trame(N=50)
	#	My_task_LectTrame = Task_Lect_Trame(Trame_a_analyser, N)
	#	My_task_LectTrame.start()
	#	print"Lancement Task_Lect_Trame\n "
	#except:
	#	print "Error: unable to start thread Task_Lect_Trame \n"

	try:
		My_task_Controleur = Task_Controleur()
		My_task_Controleur.start()
		print"Lancement Task_Controleur\n "
	except:
		print "Error: unable to start thread Task_Controleur \n"

	#try:
	#	My_task_AnaTrames = Task_AnaTrames()
	#	My_task_AnaTrames.start()
	#	print"Lancement Task_AnaTrames\n "
	#except:
	#	print "Error: unable to start thread Task_AnaTrames \n"
	
	#try:
	#	My_task_GestionFich = Task_GestionFich()
	#	My_task_GestionFich.start()
	#except:
	#	print "Error: unable to start thread my_task_GestionFich \n"
	#	
	#try:
	#	My_task_TEST1 = Task_TEST1()
	#	My_task_TEST1.start()
	#except:
	#	print "Error: unable to start thread task_TEST1 \n"
	#	
	#try:
	#	My_task_TEST2 = Task_TEST2()
	#	My_task_TEST2.start()
	#except:
	#	print "Error: unable to start thread task_TEST2 \n"
	#

	############### Lancement du GUI
	print"Lancement IHM\n"
	#app = MainAppIHM(redirect = True, filename = 'stdout.log', queue_Controleur_to_IHM, queue_IHM_to_Controleur )
	#app = MainAppIHM(redirect = True, filename = 'stdout.log', mavariable="print me")
	#app = MainAppIHM(queue_to_contr = queue_IHM_to_TaskControl)
	app = MainAppIHM(mavariable="print me")


	#app = MainAppIHM(redirect = True, filename = 'stdout.log')
	#app = MainAppIHM(IHM_to_TaskControl = queue_IHM_to_TaskControl )
	app.MainLoop()
	
	#Apres avoir fermé la fenetre principale, on quitte les autres taches.

	if (app.GetExitOnFrameDelete()):
		stop_event.set()
		print "Waiting for all the threads to finish........."
		#My_task_LectTrame.join()
		#My_task_AnaTrames.join()
		My_task_Controleur.join()
	#	My_task_GestionFich.join()
	#	My_task_TEST1.join()
	#	My_task_TEST2.join()

	#if (stop_event.isSet()):
	#	print "Waiting for all the threads to finish........."
	#	My_task_LectTrame.join()


	print time.strftime("%d/%m/%Y  %H:%M:%S")
	print"---------------- FIN DU PROGRAMME --------------------\n"

	############### Retablissement des sorties
	#sys.stdout = sys.__stdout__
	#sys.stderr = sys.__stderr__
