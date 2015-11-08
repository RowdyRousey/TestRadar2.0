#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Gestion des fichiers de configuration
#######################################################

import IhmClass

##########################################################################
# Class PageFiltre
##########################################################################	

class PageFiltre ( IhmClass.PageFiltre ):
	def __init__( self, parent ):
		IhmClass.PageFiltre.__init__(self, parent)
		# charger le fichier de log 

	# Virtual event handlers, overide them in your derived class
	def PageFiltresFermer( self, event ):
		self.Close(True)
	
	def ToutCocherFiltreRadar( self, event ):
		self.ListChoixFiltreRadar.SetChecked(range(10))
			

	def ToutDecocherFiltreRadar( self, event ):
		for i in range(10):
			self.ListChoixFiltreRadar.Check(i, check=False)

	def ValiderFiltre( self, event ):
		if self.ChoixFiltreRadar.IsChecked():
			ChoixUserRadar = self.ListChoixFiltreRadar.GetCheckedStrings()
		else:
			ChoixUserRadar=()
		if self.ChoixFiltreMode.IsChecked():
			ChoixUserMode = self.ListChoixFiltreMode.GetCheckedStrings()
		else:
			ChoixUserMode=()
		self.Close(True)
		return ChoixUserRadar+ChoixUserMode