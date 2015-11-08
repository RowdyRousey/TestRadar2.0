#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Debug de l'analyse des trames
#######################################################

import AnaTrames, sys

#*********************************************************************************************************************
#******************************************   		DEBUGGAGE             ********************************************
#*********************************************************************************************************************



##********************* DebugExtractionDataRecordCat34 ************************************************************** 
##Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 34
def DebugExtractionDataRecordCat34():
	DetailChamps34 = ExtractDetailRecord34()

	##Test extraction du Data Item System Configuration and Status	
	#tata=SysCfgStatusExtractedCAT34()
	#tata.DecodDataField("8fffffff80")
	#tata.show()
	
	##Test extraction du Data Item System Processing Mode
	#tata=SysProcessingModeExtractedCAT34()
	#tata.DecodDataField("ffffffffff")
	#tata.show()

	##test Message Type
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=8)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x05\x40\x04")
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()
	#ls(MaTrame)
	
	#test Message Count Value
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=11)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x10\x01\x80\x05\x00\x00\x10\x14\x50\x36\xf8\x80\x80\xb8")
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()
	#ls(MaTrame)

	#test Generic Polar Window
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=10)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x0a\x01\x40\xff\xff\xff\xff\xff\xff\xff\xff")
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()
	#ls(MaTrame)

	##test2 Generic Polar Window
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=10)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x0d\x01\x40\xff\xdc\x30\x01\x00\x15\x20\x52")	
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()
	#ls(MaTrame)

	##test Data Filter
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=9)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x06\x01\x20\x0f")
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()

	##test 3D-Position Of Data Source
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=10)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x0d\x01\x10\xf2\x30\x05\x02\x00\x15\x20\x52")	
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()

	##test Collimation Error
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=10)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x07\x01\x08\xb2\xb5")	
	#pkts.show()
	#MaTrame= TrameAsterix3448()
	#MaTrame, DetailChamps34 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps34.show()

	pass


##*************** DebugExtractionDataRecordCat34Detail ************************************************************** 
##Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 34
def DebugExtractionDataRecordCat34Detail():
	toto=ExtractDetailRecord34()
	
	##Test extraction du Data Item System Configuration and Status	
	#tata=SysCfgStatusExtractedCAT34()
	#tata.DecodDataField("8fffffff80")
	#tata.show()

	#Test avec decodage SAC/SIC
	toto.DecodRecord34Detail("800813")

	##Test avec decodage Message Type
	#toto.DecodRecord34Detail("4005")

	##Test avec decodage Time of Day
	#toto.DecodRecord34Detail("20a5c000")

	#Test avec decodage Sector Number 
	#toto.DecodRecord34Detail("10a3")
	
	##Test avec decodage Antenna Rotation Speed
	#toto.DecodRecord34Detail("081032")

	##Test avec decodage System Configuration and Status
	#toto.DecodRecord34Detail("040fffffff")
	
	##Test avec decodage System Processing Mode
	#toto.DecodRecord34Detail("02f0ffff")

	##Test avec decodage Message Count Values
	#toto.DecodRecord34Detail("01800315ff325b4dfc")

	##Test avec decodage Generic Polar Window
	#toto.DecodRecord34Detail("01400315ff325b4dfcdd")
	
	##Test avec decodage Data Filter
	#toto.DecodRecord34Detail("0120ff")

	##Test avec decodage 3D-Position Of Data Source
	#toto.DecodRecord34Detail("0110ffffffffffffffff")

	##Test avec decodage Collimation Error
	#toto.DecodRecord34Detail("0108ffff")

	toto.show()
	pass


##*********************************** DebugExtractionDataRecordCat48 ************************************************************** 
##Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 48
def DebugExtractionDataRecordCat48():
	DetailChamps48 = AnaTrames.ExtractDetailRecord48()
	toto = AnaTrames.Cat48Record()

	#Test avec decodage SAC/SIC, DayTime, et target report descriptor
	#toto.DecodRecord48("e00812532412f353")

	#DEBUG Extraction détaillé du Data Item : Target Report Description
	#mydata = AnaTrames.TargetReportDescExtractedCAT48()
	#mydata.DecodDataField("f352")
	#mydata.show()

	#Test avec decodage SAC/SIC, DayTime, et target report descriptor
	#toto.DecodRecord48("e00812532412f353")
	
	#Test de decodage de la position mesurée en coordonnées polaires
	#toto.DecodRecord48("1052355235")

	##DEBUG Extraction détaillé du Data Item : Mode-3/A Code in Octal Representation
	#mydata = AnaTrames.ModeACodeInOctalExtractedCAT48()
	#mydata.DecodDataField("0352")
	#mydata.show()

	##Test de decodage : Mode-3/A Code in Octal Representation
	#toto.DecodRecord48("08efff")

	##Test de decodage : Flight Level in Binary Representation
	#toto.DecodRecord48("043abf")

	##Test de decodage : Radar Plot Characteristics
	#toto.DecodRecord48("02f7aa32bbccddee")

	##Test de decodage : Aircraft Adress
	#toto.DecodRecord48("0180AF1232")

	##Test de decodage : Aircraft Identification
	#toto.DecodRecord48("014032a61c0def76")
	
	##Test de decodage : Mode S MB Data
	#toto.DecodRecord48("012002aabbccddeeff11abffeeffddffccff00")

	##Test de decodage : Track Number
	#toto.DecodRecord48("01100253")
	
	##Test de decodage : Calculated Position in Cartesian Co-ordinates
	#toto.DecodRecord48("010805ff0fff")

	##Test de decodage : Calculated Track Velocity in Polar Co-ordinates
	#toto.DecodRecord48("0104ffffffff")
	
	##Test de decodage : Track Status
	#toto.DecodRecord48("0102ef20")

	##Test de decodage : Track Quality
	#toto.DecodRecord48("010180ffffffff")

	##Test de decodage : Warning/Error Conditions
	#toto.DecodRecord48("010140f0")

	##Test de decodage : Mode-3/A Code Confidence Indicator
	#toto.DecodRecord48("0101200a6b")
	
	##Test de decodage : Mode-C Code and Code Confidence Indicator
	#toto.DecodRecord48("010110405230bc")

	##Test de decodage : Height Measured by a 3D Radar
	#toto.DecodRecord48("0101083fff")
	
	##Test de decodage : Radial Doppler Speed
	#toto.DecodRecord48("010104800000")

	##Test de decodage : Communications/ACAS Capability and Flight Status
	#toto.DecodRecord48("01010246a3")

	##Test de decodage : ACAS Resolution Advisory Report
	#toto.DecodRecord48("01010180aabbccddeeffaa")
		
	##Test de decodage : Mode-1 Code in Octal Representation
	#toto.DecodRecord48("0101014000")

	##Test de decodage : Mode-2 Code in Octal Representation
	#toto.DecodRecord48("010101200fff")

	##Test de decodage : Mode-1 Code Confidence Indicator
	#toto.DecodRecord48("0101011000")

	##Test de decodage : Mode-2 Code Confidence Indicator
	#toto.DecodRecord48("010101080fff")

	##test Collimation Error
	#pkts=Dot3(dst="fd:ff:30:ff:08:13", len=10)/LLC(dsap="08", ssap="13", ctrl=3)/("\x22\x00\x07\x01\x08\xb2\xb5")	
	#pkts.show()
	#MaTrame= AnaTrames.TrameAsterix3448()
	#MaTrame, DetailChamps34, DetailChamps48 = MaTrame.AnalyseTrameAsterix(pkts)
	#DetailChamps48.show()
	
	pass


##*********************************** DebugExtractionDataRecordCat48Detail ************************************************************** 
##Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 48
def DebugExtractionDataRecordCat48Detail():
	toto=AnaTrames.ExtractDetailRecord48()

	##Test avec decodage SAC/SIC
	toto.DecodRecord48Detail("800812")

	##Test avec decodage SAC/SIC, DayTime, et target report descriptor
	#toto.DecodRecord48Detail("e00812532412f353")
	
	#Test de decodage : Measured Position in Polar Co-ordinates 
	#toto.DecodRecord48Detail("1052355235")

	##Test de decodage : Mode-3/A Code in Octal Representation
	#toto.DecodRecord48Detail("08efff")

	##Test de decodage : Flight Level in Binary Representation
	#toto.DecodRecord48Detail("043abf")

	##Test de decodage : Radar Plot Characteristics
	#toto.DecodRecord48Detail("02f7aa32bbccddee")

	##Test de decodage : Aircraft Adress
	#toto.DecodRecord48Detail("01800F1230")

	##Test de decodage : Aircraft Identification
	#toto.DecodRecord48Detail("01400464b2c775e0")
	
	##Test de decodage : Mode S MB Data
	#toto.DecodRecord48Detail("012003aabbccddeeff11abffeeffddffccff00aabbccddeeff11ab")

	##Test de decodage : Track Number
	#toto.DecodRecord48Detail("01100253")
	
	##Test de decodage : Calculated Position in Cartesian Co-ordinates
	#toto.DecodRecord48Detail("010805ff0fff")

	##Test de decodage : Calculated Track Velocity in Polar Co-ordinates
	#toto.DecodRecord48Detail("0104ffffffff")
	
	##Test de decodage : Track Status
	#toto.DecodRecord48Detail("0102ef20")

	##Test de decodage : Track Quality
	#toto.DecodRecord48Detail("010180ffffffff")

	##Test de decodage : Warning/Error Conditions
	#toto.DecodRecord48Detail("01014009")

	##Test de decodage : Mode-3/A Code Confidence Indicator
	#toto.DecodRecord48Detail("0101200a6b")
	
	##Test de decodage : Mode-C Code and Code Confidence Indicator
	#toto.DecodRecord48Detail("010110405230bc")

	##Test de decodage : Height Measured by a 3D Radar
	#toto.DecodRecord48Detail("0101083fff")
	
	##Test de decodage : Radial Doppler Speed
	#toto.DecodRecord48Detail("010104c0bbccdd02ffeeccffeeccbbaabbaabbaa")

	##Test de decodage : Communications/ACAS Capability and Flight Status
	#toto.DecodRecord48Detail("01010246a3")

	##Test de decodage : ACAS Resolution Advisory Report
	#toto.DecodRecord48Detail("01010180aabbccddeeffaa")
		
	##Test de decodage : Mode-1 Code in Octal Representation
	#toto.DecodRecord48Detail("0101014000")

	##Test de decodage : Mode-2 Code in Octal Representation
	#toto.DecodRecord48Detail("010101200fff")

	##Test de decodage : Mode-1 Code Confidence Indicator
	#toto.DecodRecord48Detail("0101011000")

	##Test de decodage : Mode-2 Code Confidence Indicator
	#toto.DecodRecord48Detail("010101080fff")

	toto.show()
	pass




#**************************************** MAIN ****************************************************************
if __name__ == '__main__':

	#####  Redirection des sorties pour debuggage	
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')
	
	#Trame_a_analyser = "TestConfiguration"
	#Trame_a_analyser = "capturePING"
	Trame_a_analyser = "captures SIRSUR"
	#Trame_a_analyser = "../Captures Reseaux/RAPN_HS"

	##########  Debuggage ##################################################
	##DEBUG Extraction détaillé du Data Record Cat 34
	#AnaTrames.DebugExtractionDataRecordCat34()

	##DEBUG Extraction détaillé du Data Record Cat 48
	#DebugExtractionDataRecordCat48()
	
	##DEBUG Extraction détaillé du Data Record Cat 34 
	#DebugExtractionDataRecordCat34Detail()

	##DEBUG Extraction détaillé du Data Record Cat 48
	DebugExtractionDataRecordCat48Detail()

	############ Retablissement des sorties
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
