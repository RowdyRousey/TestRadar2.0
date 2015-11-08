#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
#######################################################

import IhmClass

##########################################################################
# Class PageHisto
##########################################################################

class PageHisto ( IhmClass.PageHisto ):
	def __init__( self, parent ):
		IhmClass.PageHisto.__init__( self, parent )
	# Appeler la fonction qui va lire le fichier historique et l'afficher dans la fenetre histo.	
		
	# Virtual event handlers, overide them in your derived class
	def PageHistoFermer( self, event ):
		self.Close(True)
		self.Destroy()
	
	def PageFiltreOuvrir( self, event ):
		OuvrPageFiltre = PageFiltre (self)
		OuvrPageFiltre.Show()

	def AfficherPageHisto(self, filtre):
		self.ZoneAffichHisto.WriteText("HELLO HELLO HELLO HELLO HELLO HELLO HELLO HELLO \n")
	# Appeler la fonction qui va lire le fichier historique, le formater et l'afficher dans la fenetre ad'hoc		