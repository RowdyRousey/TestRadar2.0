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
# Class PageStatsRadar (Dialog Box)
##########################################################################

class PageStatsRadar ( IhmClass.PageStatsRadar ):
	def __init__( self, parent, LabelNomRadar):
		IhmClass.PageStatsRadar.__init__(self, parent)
		self.ChampAffichNomRadar.ChangeValue( LabelNomRadar.upper() )
		self.affich_heure_lancement_appli()
	
# Virtual event handlers, overide them in your derived class

	def affich_heure_lancement_appli(self):
		print "debutLancementAppli = ", self.GetParent().debutLancementAppli
		DebutLancementAppli = self.GetParent().debutLancementAppli
		self.Heure_Lancement_Appli.ChangeValue(u"L'application a été lancé le " + self.GetParent().debutLancementAppli)
		pass

	def FermerPageStatRadars( self, event ):
		self.Show(False)
	
	def AnnulerParam( self, event ):
	#Recharger les paramètres de conf
		event.Skip()
	
	def SauverParam( self, event ):
	# Envoyer les paramètres a sauvegarder dans le fichier de conf
		event.Skip()
	
	def ChangerPhoto( self, event ):
		LoadFichier = ChargerFichier(self)
		LoadFichier.Show()
		LoadFichier.MakeModal(True)

	def SauverGraphe( self, event ):
		event.Skip()
	
	def AfficherCourbe( self, event ):
		event.Skip()
