#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
#######################################################

import IhmClass
import wx
import os, fnmatch

##########################################################################
# Class MyDialogConfirm
##########################################################################

class MyConfirm ( IhmClass.DialogConfirm ):
	def __init__ ( self, parent,Message ):
		IhmClass.DialogConfirm.__init__(self, parent)
		self.m_staticText226.SetLabel(Message)
		self.Bind(wx.EVT_CLOSE, self.CloseApp)

	# Virtual event handlers, overide them in your derived class
	def CancelButtonSavePref( self, event ):
		self.Close(True)
		
	def SaveOnFilePref( self, event ):
	# Envoyer les infos à la tache "Gestion des fichiers" en lui indiquant quel fichier ouvrir et comment.
	# en l'occurence ici, c'est le fichier preference.txt, ouvert en écriture et pas en "append"
		#MaFramePrincipale.queueToControler.put("DATA in queueIHMToControler")
		self.Close(True)
	
	#def CloseDialogBox( self, event ):
		# self.MakeModal(False)
		# self.Close(True)
		# self.Destroy()
		#event.Skip()
	
	# l'utilisateur a cliqué OK pour quitter l'application
	def CloseApp( self, event ):
		# Il faut arreter les timers proprement
		try:
			self.GetParent().timerHeurePC.Stop()
		except:
			print "TimerHeurePC can't STOP"
		try:
			self.GetParent().timerSignalVie.Stop()
		except:
			print "TimerSignalVie can't STOP"
		try:
			self.GetParent().timerUpdateIHM.Stop()
		except:
			print "timerUpdateIHM can't STOP"			
		
		self.Close(True)
		self.Destroy()
		# On détruit la fenetre parent
		self.GetParent().Destroy()

		#event.Skip() 



class MyConfirmSavePref ( IhmClass.DialogConfirm ):
	def __init__ ( self, parent,message ):
		IhmClass.DialogConfirm.__init__(self, parent)
		self.m_staticText226.SetLabel(message)
	# Virtual event handlers, overide them in your derived class
	def CancelButtonSavePref( self, event ):
		self.Close(True)
		
	def SaveOnFilePref( self, event ):
	#Envoyer les infos à la tache "Gestion des fichiers" en lui indiquant quel fichier ouvrir et comment.
	#en l'occurence ici, c'est le fichier preference.txt, ouvert en écriture et pas en "append"
		#MaFramePrincipale.queueToControler.put("DATA in queueIHMToControler")
		self.Close(True)