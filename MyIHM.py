#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Classe IHM particularisée
#######################################################

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from GestionFich import *
import wx
import re
import os.path
import time
import IhmClass
from MyPagePreferences import *
from MyPageStatsRadar import *
from MyPageIncompatibilite import *
from MyPageFiltre import *
from MyConfirm import *
from MyPageHisto import *
from MyPageHelp import *
#from MyCloseAppConfirmPage import *
from MyChargerFichier import *

#from Tasks import queueIHMToControler, queueControlerToIHM

ONE_SECOND = 1000 #millisecond

###########################################################################
## Class MaFramePrincipale
###########################################################################

#Implementing MainFrame
class MaFramePrincipale( IhmClass.MainFrame ):
	debutLancementAppli=""

	def __init__( self, parent, queueControlerToIHM=None, queueIHMToControler=None):
		IhmClass.MainFrame.__init__( self, parent )
	
		self.queueControlerToIHM = queueControlerToIHM
		self.queueIHMToControler = queueIHMToControler
		
		#Heure et date de lancement de l'appli
		self.debutLancementAppli = self.Update_HeurePC()

		# self.RAAV_S_Info2 = wx.StaticText( self.RAAV_PanelS, wx.ID_ANY, u"RAAV_S_Info 2", wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		# 
		# self.RAAV_S_Info1 = wx.StaticText( self.RAAV_PanelS, wx.ID_ANY, u"RAAV_S_Info1", wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )

		self.RAAV_S_Info1.Centre()
		self.RANE_S_Info1.Centre()
		self.RAPS_S_Info1.Centre()
		self.RATR_S_Info1.Centre()
		self.RACH_S_Info1.Centre()
		self.RABL_S_Info1.Centre()
		self.RAPN_S_Info1.Centre()
		self.RAGB_S_Info1.Centre()
		self.RACD_S_Info1.Centre()
		self.RABE_S_Info1.Centre()
		
		self.RAAV_S_Info2.Centre()
		self.RANE_S_Info2.Centre()
		self.RAPS_S_Info2.Centre()
		self.RATR_S_Info2.Centre()
		self.RACH_S_Info2.Centre()
		self.RABL_S_Info2.Centre()
		self.RAPN_S_Info2.Centre()
		self.RAGB_S_Info2.Centre()
		self.RACD_S_Info2.Centre()
		self.RABE_S_Info2.Centre()

		self.PageStatRadar01 = PageStatsRadar(self, LabelNomRadar="avranches")
		self.PageStatRadar02 = PageStatsRadar(self, LabelNomRadar="nevers")
		self.PageStatRadar03 = PageStatsRadar(self, LabelNomRadar="palaiseau")
		self.PageStatRadar04 = PageStatsRadar(self, LabelNomRadar="tours")
		self.PageStatRadar05 = PageStatsRadar(self, LabelNomRadar="chaumont")
		self.PageStatRadar06 = PageStatsRadar(self, LabelNomRadar="boulogne")
		self.PageStatRadar07 = PageStatsRadar(self, LabelNomRadar="coubron")
		self.PageStatRadar08 = PageStatsRadar(self, LabelNomRadar="grand-ballon")
		self.PageStatRadar09 = PageStatsRadar(self, LabelNomRadar="roissy")
		self.PageStatRadar10 = PageStatsRadar(self, LabelNomRadar="bertem")
		self.PageStatRadar11 = PageStatsRadar(self, LabelNomRadar="TMA1")
		self.PageStatRadar12 = PageStatsRadar(self, LabelNomRadar="TMA2")
		self.PageStatRadar13 = PageStatsRadar(self, LabelNomRadar="TMA4")
		self.PageStatRadar14 = PageStatsRadar(self, LabelNomRadar="TMA5")
		self.PageStatRadar15 = PageStatsRadar(self, LabelNomRadar="")
		
		#Créer des timers pour exécuter les actions périodiques.
		self.timerHeurePC = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimerHeurePC, self.timerHeurePC)
		self.AffichHeurePC.SetLabel(self.Update_HeurePC())
		self.timerHeurePC.Start(ONE_SECOND)	#la valeur est en millisecondes
		
		#Timer pour mise à jour de l'affichage
		self.timerUpdateIHM = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimerUpdateIHM, self.timerUpdateIHM)
		self.timerUpdateIHM.Start(5*ONE_SECOND)	#la valeur est en millisecondes
		
		#timer de mise à jour du signal de vie
		self.timerSignalVie = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimerSignalVie, self.timerSignalVie)
		self.timerSignalVie.Start(2*ONE_SECOND)	#la valeur est en millisecondes



	def OnRun(self):
		print "HELLO FRON ONRUN MyIHM.MaFramePrincipale\n"
		pass
	
	def OnTimerHeurePC(self, event):
		self.AffichHeurePC.SetLabel(self.Update_HeurePC())
	
	def OnTimerUpdateIHM(self, event) :
		#Lecture de la file d'attente
		# if self.queueControlerToIHM.empty()== False:
		# 	try:
		# 		print"Queue is not empty \n"
		# 		Data_In_Queue = self.queueControlerToIHM.get()
		# 		print "DATA dans IHM = \n" + self.Update_HeurePC(), Data_In_Queue,"\n"
		# 	except:
		# 		print"IHM Can't read in the queue : %s \n" %(sys.exc_info()[0])
		#Analyse des données venant de la file d'attente
		
		#Mise à jour des infos dans l'IHM
		info = u"RAAV_S_Info1" + self.Update_HeurePC()
		self.RAAV_S_Info1 = wx.StaticText( self.RAAV_PanelS, wx.ID_ANY, info, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAAV_S_Info1.Centre()
	
		#Mise à jour des infos dans l'IHM
		info = u"RABL_S_Info1" + self.Update_HeurePC()
		self.RABL_S_Info1 = wx.StaticText( self.RABL_PanelS, wx.ID_ANY, info, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABL_S_Info1.Centre()
	
		#Mise à jour des infos dans l'IHM
		info = u"RAGB_S_Info1" + self.Update_HeurePC()
		self.RAGB_S_Info1 = wx.StaticText( self.RAGB_PanelS, wx.ID_ANY, info, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAGB_S_Info1.Centre()
		
		#self.ZoneAffichHisto.WriteText("HELLO HELLO HELLO HELLO HELLO HELLO \n")
		
	def OnTimerSignalVie(self, event):
		self.Signal_Vie.Play()
	
	# Virtual event handlers, overide them in your derived class
	def QuitApplication( self, event ):
		PageConfirmClose = MyConfirm(self,"Voulez vraiment quitter l'application ?")
		#Afficher et rendre la fenetre modale = aucune autre action possible en dehors de la fenetre.
		PageConfirmClose.Show()
		PageConfirmClose.MakeModal(True)
		#PageConfirmClose.CloseApp(self)
	
	def OpenIncompatibiliteCoupureRadar( self, event ):
		IncompatibiliteCoupRadarPage = PageIncompatibiliteCoupureRadar(self)
		IncompatibiliteCoupRadarPage.Show()
	
	def OpenHistoPage( self, event ):
		HistPage = PageHisto(self)
		self.queueIHMToControler.put(("histo_R",""))
		while(self.queueControlerToIHM.empty() == True):
			time.sleep(0.2)
			#print time.strftime("%d/%m/%Y  %H:%M:%S"),"   WAIT OpenHistoPage --------------- \n"
		(commande,data)=self.queueControlerToIHM.get()
		if commande == "histo_R":
		#print "DANS OpenHistoPage, Data = \n", data
			self.queueControlerToIHM.task_done()
			HistPage.ZoneAffichHisto.WriteText(data)
			HistPage.Show()
	
	def OpenPreferencePage( self, event ):
		PrefPage = PagePreferences(self)
		if PrefPage is not None :
			PrefPage.Show()
	
	def OpenHelpPage( self, event ):
		HelpPage = PageHelp(self)
		HelpPage.Show()
	
	def OpenStatsRadar_radar01( self, event ):
		self.PageStatRadar01.Show()
	
	def OpenStatsRadar_radar02( self, event ):
		self.PageStatRadar02.Show()
	
	def OpenStatsRadar_radar03( self, event ):
		self.PageStatRadar03.Show()
	
	def OpenStatsRadar_radar04( self, event ):
		self.PageStatRadar04.Show()
	
	def OpenStatsRadar_radar05( self, event ):
		self.PageStatRadar05.Show()
	
	def OpenStatsRadar_radar06( self, event ):
		self.PageStatRadar06.Show()
		
	def OpenStatsRadar_radar07( self, event ):
		self.PageStatRadar07.Show()
	
	def OpenStatsRadar_radar08( self, event ):
		self.PageStatRadar08.Show()
	
	def OpenStatsRadar_radar09( self, event ):
		self.PageStatRadar09.Show()
	
	def OpenStatsRadar_radar10( self, event ):
		self.PageStatRadar10.Show()
	
	def OpenStatsRadar_radar11( self, event ):
		self.PageStatRadar11.Show()
	
	def OpenStatsRadar_radar12( self, event ):
		self.PageStatRadar12.Show()
	
	def OpenStatsRadar_radar13( self, event ):
		self.PageStatRadar13.Show()
	
	def OpenStatsRadar_radar14( self, event ):
		self.PageStatRadar14.Show()
	
	def OpenStatsRadar_radar15( self, event ):
		self.PageStatRadar15.Show()
		
	def Update_HeurePC(self):
		#Affiche l'heure du PC
		return time.strftime("%d/%m/%Y  %H:%M:%S")
	
	def __del__(self):
		self.Close(True)
		wx.Exit()

class MainAppIHM(wx.App):
	def OnInit(self):
		print "MON IHM "
		self.mainfrm = MaFramePrincipale(None)
		
		self.SetTopWindow(self.mainfrm)
		self.mainfrm.Show()
		return True

	def OnExit(self):
		print "MON IHM EXIT"


#################################### MAIN ########################################	

if __name__ == '__main__':

	import sys

	stop_event = threading.Event()
	stop_event.clear()
	
	####  Redirection des sorties pour debuggage
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')
	
	app = MainAppIHM(redirect = True, filename = 'stdout.log')
	app.MainLoop()
	
	if (app.GetExitOnFrameDelete()):
		stop_event.set()
		print "Waiting for all the threads to finish........."
		app.mainfrm.mythread.join()
	########### Retablissement des sorties
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
	
	
	