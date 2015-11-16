#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Main
#######################################################

import threading, Queue, time
import MyIHM
#import GestionFich, AnaTrames, LectTrames
import Tasks
import wx

###################################################################

class MainAppIHM(wx.App):

	#Trame_a_analyser = None; Sniff le réseau
	#Trame_a_analyser = nom_d_un_fichier; Lecture dans un fichier
	Trame_a_analyser = "sample"
	#Trame_a_analyser = "captures SIRSUR"
	N=1

	My_task_LectTrame = Tasks.Task_Lect_Trame(Trame_a_analyser, N)
	#My_task_AnaTrames = Tasks.Task_AnaTrames()
	My_task_GestionFich = Tasks.Task_GestionFich()
	#My_task_TEST1 = Tasks.Task_TEST1()
	#My_task_TEST2 = Tasks.Task_TEST2()
	
	#on instancie et on initialise l'évènement pour arreter toutes les taches.
	stop_event = threading.Event()
	stop_event.clear()
	
	
	def OnInit(self):
		print "GO_TEST_RADAR_V2.MainAppIHM.OnInit\n"
		
		try:
			self.My_task_LectTrame.start()
		except:
			print "Error: unable to start thread Task_Lect_Trame \n"
		
		#try:
		#	self.My_task_AnaTrames.start()
		#except:
		#	print "Error: unable to start thread Task_AnaTrames \n"
		#	
		try:
			self.My_task_GestionFich.start()
		except:
			print "Error: unable to start thread my_task_GestionFich \n"
			
		#try:
		#	self.My_task_TEST1.start()
		#except:
		#	print "Error: unable to start thread task_TEST1 \n"
		#	
		#try:
		#	self.My_task_TEST2.start()
		#except:
		#	print "Error: unable to start thread task_TEST2 \n"
		#	
		mainfrm = MyIHM.MaFramePrincipale(None)
		self.SetTopWindow(mainfrm)
		mainfrm.Show()
		return True

	def OnExit(self):
		print "OnExit MainAppIHM\n"
	#	Tasks_manager.OnExit
		#if (app.GetExitOnFrameDelete()):
			#self.stop_event.set()
			#print "Waiting for all the threads to finish........."
			#self.My_task_LectTrame.join()
			#self.My_task_AnaTrames.join()
			#self.My_task_GestionFich.join()
			#self.My_task_TEST1.join()
			#self.My_task_TEST2.join()

	def __del__(self):
		print "__del__ MainAppIHM\n"

	
########################  PROGRAMME PRINCIPAL #######################
if __name__ == '__main__':
	
	import sys
	
	#####  Redirection des sorties pour debuggage
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')

	#Instanciation des canaux de communication entre les taches
	queue_Test1_to_Test2 = Queue.Queue()
	queue_LectTrame_to_AnaTrames = Queue.Queue()
	
	print"\n-----------------MON MAIN------------------"
	print time.strftime("%d/%m/%Y  %H:%M:%S")

	##on instancie et on initialise l'évènement pour arreter toutes les taches.
	#stop_event = threading.Event()
	#stop_event.clear()
	#
	##Instanciation des canaux de communication entre les taches
	#queue_Test1_to_Test2 = Queue.Queue()
	#queue_LectTrame_to_AnaTrames = Queue.Queue()
	
	############### Lancement du GUI
	app = MainAppIHM(redirect = False, filename = 'stdout.log')
	app.MainLoop()

	#Apres avoir fermé la fenetre principale, on ferme les autres taches.
	#if (app.GetExitOnFrameDelete()):
	#	stop_event.set()
	#	print "Waiting for all the threads to finish........."
	#	My_task_LectTrame.join()
	#	My_task_AnaTrames.join()
	#	My_task_GestionFich.join()
	#	My_task_TEST1.join()
	#	My_task_TEST2.join()

	print time.strftime("%d/%m/%Y  %H:%M:%S")
	print"---------------- FIN DU PROGRAMME --------------------"

	#time.sleep(3)


	############### Retablissement des sorties
	#sys.stdout = sys.__stdout__
	#sys.stderr = sys.__stderr__

