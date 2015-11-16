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
# Class PageIncompatibiliteCoupureRadar
##########################################################################

class PageIncompatibiliteCoupureRadar ( IhmClass.PageIncompatibiliteCoupureRadar ):
	def __init__( self, parent ):
		IhmClass.PageIncompatibiliteCoupureRadar.__init__(self, parent)
		self.Nom_Fichier = ""
	
	# Virtual event handlers, overide them in your derived class
	def IncompatibiliteCoupuresRadarsFermer( self, event ):
		# Sauvegarder le nom du fichier sélectionné dans le fichier de configuration
		print "self.Nom_Fichier = ", self.Nom_Fichier
		self.Close(True)
		
	
	def IncompatibiliteCoupuresRadarsPageModifier( self, event ):
		LoadFichier = ChargerFichier(self)
		LoadFichier.Show()
		LoadFichier.MakeModal(True)

