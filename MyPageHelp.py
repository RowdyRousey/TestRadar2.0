#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# NE PAS MODIFIER
#######################################################

import IhmClass

##########################################################################
# Class PageHelp
##########################################################################

class PageHelp ( IhmClass.PageHelp ):
	def __init__( self, parent ):
		IhmClass.PageHelp.__init__(self, parent)
		# Le chemin complet du fichier d'aide
		self.Nom_Fichier = ""
	
	# Virtual event handlers, overide them in your derived class
	def HelpFermer( self, event ):
		# Sauvegarder le nom du fichier sélectionné dans le fichier de configuration
		print "self.Nom_Fichier = ", self.Nom_Fichier
		self.Close(True)
	
	def PageAideModifier( self, event ):
		FenChargerFile = ChargerFichier(self)
		FenChargerFile.Show()
		FenChargerFile.MakeModal(True)

