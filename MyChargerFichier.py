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
# Class ChargerFichier
##########################################################################

class ChargerFichier ( IhmClass.ChargerFichier ):
	def __init__( self, parent ):
		IhmClass.ChargerFichier.__init__( self, parent )
		# Charger le fichier image en lisant dans le fichier de configuration

	# Virtual event handlers, overide them in your derived class
	def ButtonCancelChargerFichier( self, event ):
		self.MakeModal(False)
		self.Close(True)
		self.Destroy()
		
	def AfficheMessageDialog(self, message):
		dlg=wx.MessageDialog(self, message , caption = "Erreur",style = wx.OK )
		HitButton=dlg.ShowModal()
		if (HitButton==True):
			dlg.Close()
			dlg.Destroy()

	def ButtonOKChargerFichier( self, event ):
		# Format des fichiers valides
		HTMLextensionList = [".htm", ".html"]
		PIXextensionList = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]		
	
		# Récupère le chemin du fichier sélectionné
		Nom_Fichier = self.SelectionFichier.GetPath().lower()
	
		# Chercher qui est la fenetre parente
		FenetreParent = self.GetParent()
		# Récupérer l'extension du fichier
		extension = os.path.splitext(Nom_Fichier)[1]
		
		# Le fichier sélectionné est valide
		if ( extension in HTMLextensionList ) or (extension in PIXextensionList):
			# On veut afficher un HTML
			if isinstance (FenetreParent.ZoneAffichagePage, wx.html.HtmlWindow):
				if extension in HTMLextensionList:
					# Fermer la fenetre
					self.MakeModal(False)
					self.Close(True)
					self.Destroy()
					# charger le fichier selectionné
					FenetreParent.ZoneAffichagePage.LoadPage( str(Nom_Fichier) )
				else:
					# Le format n'est pas un HTML, on affiche une boite de dialogue de message d'erreur
					self.AfficheMessageDialog(u"Le fichier sélectionné n'est pas un fichier HTML.")
					
			# On veut afficher une image
			elif isinstance (FenetreParent.ZoneAffichagePage, wx.StaticBitmap):
				if extension in PIXextensionList:
					# Fermer la fenetre
					self.MakeModal(False)
					self.Close(True)
					self.Destroy()
					# charger le fichier selectionné
					FenetreParent.ZoneAffichagePage.SetBitmap( wx.Bitmap(Nom_Fichier) )
				else:
					# Le format n'est pas un format image, on affiche une boite de dialogue de message d'erreur
					self.AfficheMessageDialog(u"Le fichier sélectionné n'est pas un fichier image.")
	
			# Renvoyer le nom et le chemin du fichier sélectionné à la fenetre mère pour l'inscire dans le fichier de conf
			FenetreParent.Nom_Fichier = Nom_Fichier
	
		else:
			# Le format n'est pas un format image, on affiche une boite de dialogue de message d'erreur
			self.AfficheMessageDialog(u"Le format du fichier n'est pas valide.")
