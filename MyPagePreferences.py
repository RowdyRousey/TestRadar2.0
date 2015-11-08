#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
#######################################################

import IhmClass
import ConfigParser
from GestionFich import *
from MyConfirm import *



##########################################################################
# Class PagePreferences
##########################################################################

NomFichierConfig = "config.ini"

class PagePreferences ( IhmClass.PagePreferences ):
	instances = []
	def __init__( self, parent):
		if len(self.instances) == 0:
			IhmClass.PagePreferences.__init__(self, parent)
			self.instances.append(self)
			GesFic = GestionFichier()
			self.TabObjetPref = [self.m_textCtrlNbErrorFinBloc,self.m_textCtrlNbErrorSynt,self.m_textCtrlNbNoHour,self.m_textCtrNbNoTopNorth,self.m_textCtrlNbDecalAzim,self.m_textCtrlTolPerRot,self.m_textCtrlTolDecalAzim,self.m_textCtrlTxGhostPlot,self.m_textCtrlTxDoublon,self.m_textCtrlTxDoubtPlot,self.m_textCtrlTxGarbleModeA,self.m_textCtrlTxGarbleModeC,self.m_textCtrlTxInvalidesModeA,self.m_textCtrlTxInvalidesModeC,self.m_textCtrlTxDetectionModeAC,self.m_textCtrlModeS]
			self.TabCle=["NbErrorFinBloc","NbErrorSynt","NbNoHour","NbNoTopNorth","NbDecalAzim","TolPerRot","TolDecalAzim","TxGhostPlot","TxDoublon","TxDoubtPlot","TxGarbleModeA","TxGarbleModeC","TxInvalidesModeA","TxInvalidesModeC","TxDetectionModeAC","ModeS"]
			GesFic.ChargerPreferences(NomFichierConfig,self.TabObjetPref,self.TabCle)
		else:
			return None

		
	
			
	def SauverPreferences( self, event ):
		SavePagePref=MyConfirmSavePref(self, "bb")
		SavePagePref.Show()
		print "ttttttt"


	def FermerPreferencesPage( self, event ):
		self.instances.remove(self)
		self.Close(True)
		self.Destroy()
	
  
	
		

