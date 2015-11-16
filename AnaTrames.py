#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Analyse des trames recues
#######################################################

import datetime
from string import *
from math import trunc
from binascii import *
from scapy.all import * 

#Definition des constantes
CAT34 = 34
CAT48 = 48

# Liste des radars utilises
RADAR_ModeS={
	"fd:ff:30:ff:08:15" : "Nevers",
	"fd:ff:30:ff:08:12" : "Grand Ballon", 
	"fd:ff:30:ff:08:14" : "Boulogne", 
	"fd:ff:30:ff:08:01" : "Chaumont",
	"fd:ff:30:ff:08:13" : "Avranches",
	"fd:ff:30:ff:08:07" : "Palaiseau",
	"fd:ff:30:ff:08:09" : "Coubron",
	"fd:ff:30:ff:08:02" : "Tours",
	"fd:ff:30:ff:08:22" : "Roissy",
	"fd:ff:30:ff:06:03" : "Bertem"
}

#Obtenir le nombre d�cimal correspondant � un code de Gray donn�
#En entr�e : la chaine de caract�re du code binaire cod� avec le codage de Gray
#En sortie : le nombre d�cimal correspondant au code binaire
def gray2dec(ch):
    i=ch.find("1")
    if i<0:
        return 0
    lg=len(ch)
    k=lg-i
    n=(2**k)-(2**(k-1))
    while k>1:
        k-=1
        b=int(ch[lg-k])
        y=0
        while (2*y+b)*(2**k)-(2**(k-1))+(2**k)-1 < n:
            y+=1
        np=(2*y+b)*(2**k)-(2**(k-1))
        if np>n:
            n=np
    return n

#*********************************************************************************************************************
#********************************************  		CATEGORIE 34          ********************************************
#*********************************************************************************************************************

#***************************** SysCfgStatusExtractedCAT34  ***********************************************************
#J'extrais les items du champ : System Configuration and Status
class SysCfgStatusExtractedCAT34(Packet):
	name="Detail du Data Item : System Configuration and Status"
	fields_desc = [IntEnumField("COM_NoGo", None,{0:"System Is Operationnal", 1:"System Is Inhibited"}),
				   IntEnumField("COM_RDPC", None,{0:"RDPC-1 selected", 1:"RDPC-2 selected"}),
				   IntEnumField("COM_RDPR", None, {0:"RDPC not restarted", 1:"RDPC restarted"}),
				   IntEnumField("COM_OVL_RDP", None, {0:"Processor not overload", 1:"Processor overload"}),
				   IntEnumField("COM_OVL_XMT", None, {0:"No Overload in Transmission Subsystem", 1:"Overload in Transmission Subsystem"}),
				   IntEnumField("COM_MSC", None, {0:"Monitoring System Connected", 1:"Monitoring System Disconnected"}),
				   IntEnumField("COM_TSV", None, {0:"Time Source Is Valid", 1:"Time Source Is Not Valid"}),
				   
				   IntEnumField("PSR_ANT", None,{0:"Antenna 1", 1:"Antenna 2"}),
				   IntEnumField("PSR_CH_AB", None,{0:"No Channel selected", 1:"Channel A only selected",2:"Channel B only selected", 3:"Channel A and B selected"}),
				   IntEnumField("PSR_OVL", None, {0:"No Overload", 1:"Overload"}),
				   IntEnumField("PSR_MSC", None, {0:"Monitoring System Connected", 1:"Monitoring System Disconnected"}),

				   IntEnumField("SSR_ANT", None,{0:"Antenna 1", 1:"Antenna 2"}),
				   IntEnumField("SSR_CH_AB", None,{0:"No Channel selected", 1:"Channel A only selected",2:"Channel B only selected", 3:"Invalid combination"}),
				   IntEnumField("SSR_OVL", None, {0:"No Overload", 1:"Overload"}),
				   IntEnumField("SSR_MSC", None, {0:"Monitoring System Connected", 1:"Monitoring System Disconnected"}),

				   IntEnumField("MDS_ANT", None,{0:"Antenna 1", 1:"Antenna 2"}),
				   IntEnumField("MDS_CH_AB", None,{0:"No Channel selected", 1:"Channel A only selected",2:"Channel B only selected", 3:"Illegal combination"}),
				   IntEnumField("MDS_OVL_SUR", None, {0:"No Overload", 1:"Overload"}),
				   IntEnumField("MDS_MSC", None, {0:"Monitoring System Connected", 1:"Monitoring System Disconnected"}),
				   IntEnumField("MDS_SCF", None, {0:"Channel A in use in Surveillance Coordination Function", 1:"Channel B in use in Surveillance Coordination Function"}),
				   IntEnumField("MDS_DLF", None, {0:"Channel A in use for Data Link Function", 1:"Channel B in use for Data Link Function"}),
				   IntEnumField("MDS_OVL_SCF", None, {0:"No Overload in Surveillance Coordination Function", 1:"Overload in Surveillance Coordination Function"}),
				   IntEnumField("MDS_OVL_DLF", None, {0:"No Overload for Data Link Function", 1:"Overload for Data Link Function"}),
				   ]	
	
	#Decode l'item COM
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_COM(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.COM_NoGo = int(tmp[0])
		self.COM_RDPC = int(tmp[1])
		self.COM_RDPR = int(tmp[2])
		self.COM_OVL_RDP = int(tmp[3])
		self.COM_OVL_XMT = int(tmp[4])
		self.COM_MSC = int(tmp[5])
		self.COM_TSV = int(tmp[6])
		return self

	#Decode l'item PSR
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_PSR(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.PSR_ANT = int(tmp[0])
		self.PSR_CH_AB = int(tmp[1:3],2)
		self.PSR_OVL = int(tmp[3])
		self.PSR_MSC = int(tmp[4])
		return self

	#Decode l'item SSR
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_SSR(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.SSR_ANT = int(tmp[0])
		self.SSR_CH_AB = int(tmp[1:3],2)
		self.SSR_OVL = int(tmp[3])
		self.SSR_MSC = int(tmp[4])
		return self
	
	#Decode l'item MDS
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_MDS(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.MDS_ANT = int(tmp[0])
		self.MDS_CH_AB = int(tmp[1:3],2)
		self.MDS_OVL_SUR = int(tmp[3])
		self.MDS_MSC = int(tmp[4])
		self.MDS_SCF = int(tmp[5])
		self.MDS_DLF = int(tmp[6])
		self.MDS_OVL_SCF = int(tmp[7])
		self.MDS_OVL_DLF = int(tmp[8])
		return self
	
	#En entrée : la valeur complete du champ SysCfgStatus codé en hexa
	#En sortie : renvoie la structure de la classe remplie en conséquence
	def DecodDataField(self, Val):
		tmp=bin(int(Val[:2],16))[2:].zfill(len(Val))
		PointeurWhoAmI=0
		#le sous champ COM est présent		
		if tmp[0]== "1":
			PointeurWhoAmI+=2
			self.DecodItem_COM( Val[PointeurWhoAmI:PointeurWhoAmI+2] )
		#le sous champ PSR est présent				
		if tmp[3]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_PSR( Val[PointeurWhoAmI:PointeurWhoAmI+2] )
		#le sous champ SSR est présent				
		if tmp[4]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_SSR( Val[PointeurWhoAmI:PointeurWhoAmI+2] )
		##le sous champ MDS est présent				
		if tmp[5]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_MDS( Val[PointeurWhoAmI : PointeurWhoAmI+4] )
		return self


#**************************** SysProcessingModeExtractedCAT34 ********************************************************
#J'extrait les items du champ : System Processing Mode
class SysProcessingModeExtractedCAT34(Packet):
	name="Detail du Data Item : System Processing Mode"
	fields_desc = [IntEnumField("COM_REDRDP", None, {0:"No Reduction Active", 1:"Reduction Step 1 Active for an overload of the RDP", 2:"Reduction Step 2 Active for an overload of the RDP", 3:"Reduction Step 3 Active for an overload of the RDP", 4:"Reduction Step 4 Active for an overload of the RDP", 5:"Reduction Step 5 Active for an overload of the RDP", 6:"Reduction Step 6 Active for an overload of the RDP", 7:"Reduction Step 7 Active for an overload of the RDP"}),
				   IntEnumField("COM_REDXMT", None, {0:"No Reduction Active", 1:"Reduction Step 1 Active for an overload of the transmission subsys", 2:"Reduction Step 2 Active for an overload of the transmission subsys", 3:"Reduction Step 3 Active for an overload of the transmission subsys", 4:"Reduction Step 4 Active for an overload of the transmission subsys", 5:"Reduction Step 5 Active for an overload of the transmission subsys", 6:"Reduction Step 6 Active for an overload of the transmission subsys", 7:"Reduction Step 7 Active for an overload of the transmission subsys"}),
				   
				   IntEnumField("PSR_POL", None,{0:"PSR Linear Polarization", 1:"PSR Circular Polarization"}),
				   IntEnumField("PSR_REDRAD", None,{0:"No Reduction Active", 1:"Reduction Step 1 Active for an overload of the PSR subsys", 2:"Reduction Step 2 Active for an overload of the PSR subsys", 3:"Reduction Step 3 Active for an overload of the PSR subsys", 4:"Reduction Step 4 Active for an overload of the PSR subsys", 5:"Reduction Step 5 Active for an overload of the PSR subsys", 6:"Reduction Step 6 Active for an overload of the PSR subsys", 7:"Reduction Step 7 Active for an overload of the PSR subsys"}),
				   IntEnumField("PSR_STC", None, {0:"Sensitive Time Control Map-1 in use", 1:"Sensitive Time Control Map-2 in use", 2:"Sensitive Time Control Map-3 in use", 3:"Sensitive Time Control Map-4 in use"}),

				   IntEnumField("SSR_REDRAD", None,{0:"No Reduction Active", 1:"Reduction Step 1 Active for an overload of the SSR subsys", 2:"Reduction Step 2 Active for an overload of the SSR subsys", 3:"Reduction Step 3 Active for an overload of the SSR subsys", 4:"Reduction Step 4 Active for an overload of the SSR subsys", 5:"Reduction Step 5 Active for an overload of the SSR subsys", 6:"Reduction Step 6 Active for an overload of the SSR subsys", 7:"Reduction Step 7 Active for an overload of the SSR subsys"}),

				   IntEnumField("MDS_REDRAD", None,{0:"No Reduction Active", 1:"Reduction Step 1 Active for an overload of the Mode S subsys", 2:"Reduction Step 2 Active for an overload of the Mode S subsys", 3:"Reduction Step 3 Active for an overload of the Mode S subsys", 4:"Reduction Step 4 Active for an overload of the Mode S subsys", 5:"Reduction Step 5 Active for an overload of the Mode S subsys", 6:"Reduction Step 6 Active for an overload of the Mode S subsys", 7:"Reduction Step 7 Active for an overload of the Mode S subsys"}),
				   IntEnumField("MDS_CLU", None, {0:"Cluster Autonomous", 1:"Cluster Not Autonomous"}),
				   ]	
	
	#Decode l'item COM
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_COM(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.COM_REDRDP = int(tmp[1:4],2)
		self.COM_REDXMT = int(tmp[4:7],2)
		return self
	
	#Decode l'item PSR
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_PSR(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.PSR_POL = int(tmp[0])
		self.PSR_REDRAD = int(tmp[1:4],2)
		self.PSR_STC = int(tmp[4:6],2)
		return self
	
	#Decode l'item SSR
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_SSR(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.SSR_REDRAD = int(tmp[0:3],2)
		return self
	
	#Decode l'item MDS
	#Val est la valeur hexadecimale a decoder, en sortie, on recupere les champs ci dessus avec les valeurs correctes
	def DecodItem_MDS(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.MDS_REDRAD = int(tmp[0:3],2)
		self.MDS_CLU = int(tmp[3])
		return self
	
	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		PointeurWhoAmI=0
		#le sous champ COM est présent		
		if tmp[0]== "1":
			PointeurWhoAmI+=2
			self.DecodItem_COM( Val[PointeurWhoAmI : PointeurWhoAmI+2] )
		#le sous champ PSR est présent				
		if tmp[3]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_PSR( Val[PointeurWhoAmI : PointeurWhoAmI+2] )
		#le sous champ SSR est présent				
		if tmp[4]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_SSR( Val[PointeurWhoAmI : PointeurWhoAmI+2] )
		##le sous champ MDS est présent				
		if tmp[5]=="1":
			PointeurWhoAmI+=2
			self.DecodItem_MDS( Val[PointeurWhoAmI : PointeurWhoAmI+2] )
		return self


#**************************** ExtractDetailRecord34 ******************************************************************
class ExtractDetailRecord34(Packet):
	name="Detail du DataRecord de la trame Asterix CAT 34"
	fields_desc = [XShortField("FSPEC", None),			#2 octets max
				   FieldListField("SACSIC", None, []), 	#Liste contenant le SAC et le SIC
				   IntEnumField("MsgType", None, {1:"North Marker message", 2:"Sector crossing message", 3:"Geographical filtering message", 4:"Jamming Strobe message"}),
				   StrField("TimeDay", None),
				   IntField("SectNbr", None),
				   ShortField("AntenRotPeriod", None),
				   PacketListField("SysCfgStatus", None, SysCfgStatusExtractedCAT34),
				   PacketListField("SysProcessingMode", None, SysProcessingModeExtractedCAT34),
				   FieldListField("MsgCountVal", None, []),		#Liste contenant des compteurs de messages entre 2 tops nord
				   FieldListField("GenericPolarWindow", None, []),
				   IntEnumField("DataFilter", None, {0 :"Invalid Value", 1:"Filter for Weather data", 2:"Filter for Jamming Strobe", 3:"Filter for PSR data", 4:"Filter for SSR/Mode S data", 5:"Filter for SSR/Mode S + PSR data", 6:"Enhanced Surveillance data", 7:"Filter for PSR+Enhanced Surveillance data", 8:"Filter for PSR+Enhanced Surveillance + SSR/Mode S data not in Area of Prime Interest", 9:"Filter for PSR+Enhanced Surveillance + all SSR/Mode S data"}),
				   FieldListField("TroisDPositionDataSrc",None,[]),		#Liste de 3 entiers signés correspondant à la position 3D de l'avion
				   FieldListField("CollimationError", None, []),		#Liste contenant les écarts en portée et en azimut 
				  ]
	
	#********************************************************************************************************** 
	#Fonction qui isole le champ FSPEC du reste des données
	#En Entree : toutes les donnees de la partie DataRecord (str)
	#En Sortie : uniquement le FSPEC (str), et le nombre d'octets (int)
	def IsoleFSPEC(self, DataRecord):
		i=0
		tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(8)
		#On regarde si les champs FX sont à 1 ou non
		while ((tmp[-1:])=="1"):
			if ((i+2)>8): # On evite de dépasser la taille maximale du FSPEC = 4 octets
				break
			i += 2
			tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(len(DataRecord[i:i+2])*4)
		LastBit=(i+2)
		NbOctetFSPEC=(i+2)/2
		return DataRecord[0:LastBit], NbOctetFSPEC
	
	#********************************** RemplirFSPEC *************************************************************** 
	# Cette fonction rempli un dictionnaire associant le nom de l'item et la valeur dans le FSPEC
	# En entrée : le champ FSPEC uniquement, en chaine de caractères, et la catégorie = entier
	# En sortie : une liste de tuple
	def RemplirFSPEC(self, FSPECField):
		FSPEC34listkey = ["DataSRCID", "MsgType", "TimeDay", "SectNbr" , "AntenRotPeriod", "SysCfgStatus",
						  "SysProcessingMode", "FX", "MsgCountVal", "GenericPolarWindow",
						  "DataFilter", "TroisDPositionDataSrc", "CollimationError", "ReservedExpField",
						  "SpecialPurposeField", "FX2" ]

		#converion hexa en binaire, avec retrait des caractères 0b en debut de chaine, et remplissage en début de tableau
		FSPEClistval1 = bin(int(FSPECField, 16))[2:].zfill(len(FSPECField)*4)
		FSPEClistval2=[0]*(len(FSPEClistval1))
		#Conversion des caractères en integer
		for i in range(len(FSPEClistval1)):
			FSPEClistval2[i]=int(FSPEClistval1[i],2)
		#zip combine les 2 listes en 1 : [("DataSRCID", 1), ...]
		return dict(zip(FSPEC34listkey,FSPEClistval2))

	#*********************************** DecodRecord34Detail ************************************************************** 
	#Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 34
	#En Entrée : prend le bloc DataRecord en entier
	#En sortie : renvoie le contenu du Record + la longueur du record, FSPEC compris
	def DecodRecord34Detail(self, DataBlock):
		
		msgcounttype = { 0:"No detection", 1:"Single PSR target reports", 2:"Single SSR target reports", 3:"SSR+PSR target reports", 4:"Single All-Call target reports", 5:"Single Roll-Call target reports ", 6:"All-Call + PSR target reports", 7:"Roll-Call + PSR target reports", 8:"Filter for Weather data", 9:"Filter for Jamming Strobe", 10:"Filter for PSR data", 11:"Filter for SSR/Mode S data", 12:"Filter for SSR/Mode S+PSR data", 13:"Filter for Enhanced Surveillance data", 14:"Filter for PSR+Enhanced Surveillance", 15:"Filter for PSR+Enhanced Surveillance + SSR/Mode S data not in Area of Prime Interest", 16:"Filter for PSR+Enhanced Surveillance + all SSR/Mode S data"}
		
		#print "************************************** DECOD RECORD 34 **************************************"
		#FSPEC est un dictionnaire : {"DataSRCID" : 1, ...}
		NbOctetsFSPEC=0
		FSPEC, NbOctetsFSPEC = self.IsoleFSPEC(DataBlock)
		FSPECRempli = self.RemplirFSPEC(FSPEC)
		self.FSPEC = FSPEC
		PointeurWhereAmI = NbOctetsFSPEC*2
		#Extraction du SAC/SIC (2 octets)
		if "DataSRCID" in FSPECRempli:
			if (FSPECRempli["DataSRCID"]):
				self.SACSIC.append((DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]))
				self.SACSIC.append((DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4]))
				PointeurWhereAmI += 4
		#Extraction du champ "Message Type" (1 octet)
		if "MsgType" in FSPECRempli:
			if FSPECRempli["MsgType"]:
				tmp = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)
				if ( (tmp<5) and (tmp>0) ):		# Il n'existe que 4 types de messages differents
					self.MsgType = tmp
				PointeurWhereAmI += 2
		#Extraction de l'heure du jour (3 octets)
		if "TimeDay" in FSPECRempli:
			if FSPECRempli["TimeDay"]:
				secondes = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+6],16)/128
				if (secondes<=86400):
					self.TimeDay = str(datetime.timedelta(seconds=secondes))
				PointeurWhereAmI += 6
		#Extraction du champ "Sector Number" (1 octet)
		if "SectNbr" in FSPECRempli:
			if FSPECRempli["SectNbr"]:
				self.SectNbr = int( (int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)*(1.41/11.25)) )
				PointeurWhereAmI += 2
		#Extraction du champ "Antenna Rotation Period" (2 octets)
		if "AntenRotPeriod" in FSPECRempli:
			if FSPECRempli["AntenRotPeriod"]:
				#LSB = 2^-7 s = 1/128s
				self.AntenRotPeriod = round( float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])/128, 3)
				PointeurWhereAmI += 4
		#Extraction du champ "System Confi guration and Status" (1 octet + 5 octets extension max)
		if "SysCfgStatus" in FSPECRempli:
			if FSPECRempli["SysCfgStatus"]:
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				cpt=0 	#compte le nombre de champ a 1 du premier octet
				if tmp[0]=="1":		#presence du sous champ COM (1 octet)
					cpt+=1
				if tmp[3]=="1":		#presence du sous champ PSR (1 octet)
					cpt+=1
				if tmp[4]=="1":		#presence du sous champ SSR (1 octet)
					cpt+=1
				if tmp[5]=="1":		#présence du sous champ MDS (Mode S Sensor) = 2 octets
					cpt+=2
				tmp2 = SysCfgStatusExtractedCAT34()
				self.SysCfgStatus = tmp2.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+cpt*2])
				PointeurWhereAmI += 2 + (cpt*2)
		#Extraction du champ "System Processing Mode" (1 octet + )
		if "SysProcessingMode" in FSPECRempli:
			if FSPECRempli["SysProcessingMode"]:
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				cpt=0 	#compte le nombre de champ a 1 entre le bit 8 et le bit 4
				for i in range(6):
					if tmp[i]=="1":	#présence du sous champ
						cpt+=1
				tmp2 = SysProcessingModeExtractedCAT34()
				self.SysProcessingMode = tmp2.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+cpt*2])
				PointeurWhereAmI += 2 + (cpt*2)
		#Bit Extension
		if "FX1" in FSPECRempli:
			if (FSPECRempli["FX1"])==0:  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		#Extraction du champ "Message Count Values" (1 octet + 2*N)(N est la valeur de répétition, contenu dans le 1ier octet)
		if "MsgCountVal" in FSPECRempli:
			if FSPECRempli["MsgCountVal"]:
				N = int( DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16 )	#lit et décode le premier octet pour déterminer N
				#self.MsgCountVal = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+N*4]
				self.MsgCountVal.append(N)
				pointeurtmp=0
				for i in range(1,N+1):
					tmp = bin(int(DataBlock[PointeurWhereAmI+2 + pointeurtmp : PointeurWhereAmI+2 + pointeurtmp+4],16))[2:].zfill(16)
					self.MsgCountVal.append( (msgcounttype.get(int(tmp[0:5],2), None), int(tmp[5:16],2) ) )
					pointeurtmp+=4
				PointeurWhereAmI += 2 + (N*4)
		#Extraction du champ "Generic Polar Window" (8 octets)
		if "GenericPolarWindow" in FSPECRempli:
			if FSPECRempli["GenericPolarWindow"]:
				#Rho - Start, LSB = 1/256NM
				self.GenericPolarWindow.append(round(float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])/256, 2) )
				#Rho - End, LSB = 1/256NM
				self.GenericPolarWindow.append(round(float.fromhex(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+8])/256, 2) )
				#Theta - Start, LSB = 360°/(2^16)
				self.GenericPolarWindow.append(round(float.fromhex(DataBlock[PointeurWhereAmI+8:PointeurWhereAmI+12])*360/(2**16), 2) )
				#Theta - End, LSB = 360°/(2^16)
				self.GenericPolarWindow.append(round(float.fromhex(DataBlock[PointeurWhereAmI+12:PointeurWhereAmI+16])*360/(2**16), 2) )
				PointeurWhereAmI += 16
		#Extraction du champ "Data Filter" (1 octet)
		if "DataFilter" in FSPECRempli:
			if FSPECRempli["DataFilter"] :
				mytype = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)
				if mytype<10:
					self.DataFilter = mytype
				else:
					self.DataFilter = 0
				PointeurWhereAmI += 2
		#Extraction du champ "3D-Position of Data Source" (8 octets)
		if "TroisDPositionDataSrc" in FSPECRempli:
			if FSPECRempli["TroisDPositionDataSrc"]:
				#Signed Height of the data source in WGS84, LSB = 1 metre
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4],16))[2:].zfill(16)
				if tmp[0]=="1":
					self.TroisDPositionDataSrc.append(-int(tmp[1:],2))
				else:
					self.TroisDPositionDataSrc.append(int(tmp,2))
				#Latitude in WGS84 expressed in 2 complement (range : -90 degrees<=latitude<=90 degrees), LSB = 180/(2^23)
				tmp = bin(int(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+10],16))[2:].zfill(24)
				if tmp[0]=="1":
					latitudewgs84 = round( ~int(tmp[1:],2 )*(180 * 2**-23),3 )
					if latitudewgs84<-90:
						self.TroisDPositionDataSrc.append(-90)
					else:
						self.TroisDPositionDataSrc.append(latitudewgs84)
				else:
					latitudewgs84 = round( int(tmp,2)*(180 * (2**-23)),3 )
					if latitudewgs84>90:
						self.TroisDPositionDataSrc.append(90)
					else:
						self.TroisDPositionDataSrc.append(latitudewgs84)
				#Longitude in WGS84 expressed in 2 complement (range : -180 degrees<=latitude<= 180 degrees), LSB = 180/(2^23)
				tmp = bin(int(DataBlock[PointeurWhereAmI+10:PointeurWhereAmI+16],16))[2:].zfill(24)
				if tmp[0]=="1":
					longitudewgs84 = round( ~int(tmp[1:],2 )*(180 * 2**-23), 3)
					if longitudewgs84<-180:
						self.TroisDPositionDataSrc.append(-180)
					else:
						self.TroisDPositionDataSrc.append(longitudewgs84)
				else:
					longitudewgs84 = round( int(tmp,2)*(180 * (2**-23)), 3)
					if longitudewgs84>180:
						self.TroisDPositionDataSrc.append(180)
					else:
						self.TroisDPositionDataSrc.append(longitudewgs84)
				PointeurWhereAmI += 16
		#Extraction du champ "Collimation Error" (2 octets)
		if "CollimationError" in FSPECRempli:
			if FSPECRempli["CollimationError"]:
				#RANGE ERROR, LSB = 1/128NM
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				if tmp[0]=="1":
					self.CollimationError.append(round( (~int(tmp[1:],2))*(128**-1),3 ))
				else:
					self.CollimationError.append(round( (int(tmp,2))*(128**-1),3 ))
				#AZIMUTH ERROR , LSB = 360/2^14
				tmp = bin(int(DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4],16))[2:].zfill(8)
				if tmp[0]=="1":
					self.CollimationError.append(round( (~int(tmp[1:],2))*(360*(2**-14)),3 ))
				else:
					self.CollimationError.append(round( (int(tmp,2))*(360*(2**-14)),3 ))
				PointeurWhereAmI += 4
		##******************** Ces 2 champs ne sont pas documentés *******************************
		##Extraction du champ "Reserved Expansion Field" (1 octet + 1octet +)
		#if "ReservedExpField" in FSPECRempli:
		#	if (FSPECRempli["ReservedExpField"] ==1):
		#		#self.ReservedExpField = (DataBlock[PointeurWhereAmI:PointeurWhereAmI+6])
		#		#PointeurWhereAmI += 6
		#		pass
		##Extraction du champ "Special Purpose Field" (1 octet + 1octet + )
		#if "SpecialPurposeField" in FSPECRempli:
		#	if (FSPECRempli["SpecialPurposeField"] ==1):
		#		#self.SpecialPurposeField = (DataBlock[PointeurWhereAmI:PointeurWhereAmI+6])
		#		#PointeurWhereAmI += 6
		#		pass
		return self, PointeurWhereAmI/2


#**************************** Cat34Record ****************************************************************************
#Classe représentant le champ Record d'une trame Cat34
#XByteField = champ d'un octet
#XShortField = champ de 2 octets
#X3BytesField = champ de 3 octets
#XLongField = champ de 4 octets et +
class Cat34Record(Packet):
	name="Record Categorie 34"
	fields_desc = [XShortField("FSPEC", None),				#4 octets max
				   XByteField("SAC", None),					#1 octet
				   XByteField("SIC", None),					#1 octet
				   XShortField("MsgType", None),			#1 octet
				   X3BytesField("TimeDay",None),			#3 octets
				   XByteField("SectNbr", None),				#1 octet
				   XShortField("AntenRotPeriod", None),		#2 octets
				   XLongField("SysCfgStatus", None),		#1 octet + 5 octets extensions max
				   XLongField("SysProcessingMode", None),	#1 octet + 4 octets extensions max
				   XLongField("MsgCountVal", None),			#1 octet + 2*N octets (N est la valeur de répétition, contenu dans le 1ier octet)
				   XLongField("GenericPolarWindow", None),	#8 octets
				   XByteField("DataFilter", None),			#1 octet
				   XLongField("TroisDPositionDataSrc", None),	#8 octets
				   XShortField("CollimationError", None),	#2 octets
				   XLongField("ReservedExpField", None),	#1 octet + 1octet +
				   XLongField("SpecialPurposeField", None),	#1 octet + 1octet +
				  ]
	msgcounttype = { 0:"No detection", 1:"Single PSR target reports", 2:"Single SSR target reports", 3:"SSR+PSR target reports", 4:"Single All-Call target reports", 5:"Single Roll-Call target reports ", 6:"All-Call + PSR target reports", 7:"Roll-Call + PSR target reports", 8:"Filter for Weather data", 9:"Filter for Jamming Strobe", 10:"Filter for PSR data", 11:"Filter for SSR/Mode S data", 12:"Filter for SSR/Mode S+PSR data", 13:"Filter for Enhanced Surveillance data", 14:"Filter for PSR+Enhanced Surveillance", 15:"Filter for PSR+Enhanced Surveillance + SSR/Mode S data not in Area of Prime Interest", 16:"Filter for PSR+Enhanced Surveillance + all SSR/Mode S data"}	
	#********************************************************************************************************** 
	#Fonction qui isole le champ FSPEC du reste des données
	#En Entree : toutes les donnees de la partie DataRecord (str)
	#En Sortie : uniquement le FSPEC (str), et le nombre d'octets (int)
	def IsoleFSPEC(self, DataRecord):
		i=0
		tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(8)
		#On regarde si les champs FX sont à 1 ou non
		while ((tmp[-1:])=="1"):
			if ((i+2)>8): # On evite de dépasser la taille maximale du FSPEC = 4 octets
				break
			i += 2
			tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(len(DataRecord[i:i+2])*4)
		LastBit=(i+2)
		NbOctetFSPEC=(i+2)/2
		return DataRecord[0:LastBit], NbOctetFSPEC
	
	#********************************** RemplirFSPEC *************************************************************** 
	# Cette fonction rempli un dictionnaire associant le nom de l'item et la valeur dans le FSPEC
	# En entrée : le champ FSPEC uniquement, en chaine de caractères, et la catégorie = entier
	# En sortie : une liste de tuple
	def RemplirFSPEC(self, FSPECField):
		FSPEC34listkey = ["DataSRCID", "MsgType", "TimeDay", "SectNbr" , "AntenRotPeriod", "SysCfgStatus",
						  "SysProcessingMode", "FX", "MsgCountVal", "GenericPolarWindow",
						  "DataFilter", "TroisDPositionDataSrc", "CollimationError", "ReservedExpField",
						  "SpecialPurposeField", "FX2" ]

		#converion hexa en binaire, avec retrait des caractères 0b en debut de chaine, et remplissage en début de tableau
		FSPEClistval1 = bin(int(FSPECField, 16))[2:].zfill(len(FSPECField)*4)
		FSPEClistval2=[0]*(len(FSPEClistval1))
		#Conversion des caractères en integer
		for i in range(len(FSPEClistval1)):
			FSPEClistval2[i]=int(FSPEClistval1[i],2)
		#zip combine les 2 listes en 1 : [("DataSRCID", 1), ...]
		return dict(zip(FSPEC34listkey,FSPEClistval2))


	#*********************************** DecodRecord34 ************************************************************** 
	#Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 34
	#En Entrée : prend le bloc DataRecord en entier
	#En sortie : renvoie le contenu du Record + la longueur du record, FSPEC compris
	def DecodRecord34(self, DataBlock):
		#print "************************************** DECOD RECORD 34 **************************************"
		#FSPEC est un dictionnaire : {"DataSRCID" : 1, ...}
		NbOctetsFSPEC=0
		FSPEC, NbOctetsFSPEC = self.IsoleFSPEC(DataBlock)
		FSPECRempli = self.RemplirFSPEC(FSPEC)
		self.FSPEC = FSPEC
		PointeurWhereAmI = NbOctetsFSPEC*2
		#Extraction du SAC/SIC (2 octets)
		if "DataSRCID" in FSPECRempli:
			if (FSPECRempli["DataSRCID"]):
				self.SAC = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				self.SIC = DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du champ "Message Type" (1 octet)
		if "MsgType" in FSPECRempli:
			if FSPECRempli["MsgType"]:
				self.MsgType = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction de l'heure du jour (3 octets)
		if "TimeDay" in FSPECRempli:
			if FSPECRempli["TimeDay"]:
				self.TimeDay = DataBlock[PointeurWhereAmI:PointeurWhereAmI+6]
				PointeurWhereAmI += 6
		#Extraction du champ "Sector Number" (1 octet)
		if "SectNbr" in FSPECRempli:
			if FSPECRempli["SectNbr"] :
				self.SectNbr = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction du champ "Antenna Rotation Period" (2 octets)
		if "AntenRotPeriod" in FSPECRempli:
			if FSPECRempli["AntenRotPeriod"] :
				self.AntenRotPeriod = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du champ "System Confi guration and Status" (1 octet + 5 octets extension max)
		if "SysCfgStatus" in FSPECRempli:
			if FSPECRempli["SysCfgStatus"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				cpt=0 	#compte le nombre de champ a 1 entre le bit 8 et le bit 4
				for i in range(5):
					if tmp[i]=="1":	#présence du sous champ
						cpt+=1
				if tmp[5]=="1":	#présence du sous champ MDS (Mode S Sensor) = 2 octets
					cpt+=2
				self.SysCfgStatus = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+cpt*2]
				PointeurWhereAmI += 2 + (cpt*2)
		#Extraction du champ "System Processing Mode" (1 octet + )
		if "SysProcessingMode" in FSPECRempli:
			if FSPECRempli["SysProcessingMode"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				cpt=0 	#compte le nombre de champ a 1 entre le bit 8 et le bit 4
				for i in range(6):
					if tmp[i]=="1":	#présence du sous champ
						cpt+=1
				self.SysProcessingMode = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+cpt*2]
				PointeurWhereAmI += 2 + (cpt*2)
		#Bit Extension
		if "FX1" in FSPECRempli:
			if (FSPECRempli["FX1"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		#Extraction du champ "Message Count Values" (1 octet + 2*N)(N est la valeur de répétition, contenu dans le 1ier octet)
		if "MsgCountVal" in FSPECRempli:
			if FSPECRempli["MsgCountVal"] :
				N = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)	#lit et décode le premier octet pour déterminer N
				self.MsgCountVal = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+N*4]
				PointeurWhereAmI += 2 + (N*4)
		#Extraction du champ "Generic Polar Window" (8 octets)
		if "GenericPolarWindow" in FSPECRempli:
			if FSPECRempli["GenericPolarWindow"] :
				self.GenericPolarWindow = DataBlock[PointeurWhereAmI:PointeurWhereAmI+16]
				PointeurWhereAmI += 16
		#Extraction du champ "Data Filter" (1 octet)
		if "DataFilter" in FSPECRempli:
			if FSPECRempli["DataFilter"] :
				self.DataFilter = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction du champ "3D-Position of Data Source" (8 octets)
		if "TroisDPositionDataSrc" in FSPECRempli:
			if FSPECRempli["TroisDPositionDataSrc"] :
				self.TroisDPositionDataSrc = DataBlock[PointeurWhereAmI:PointeurWhereAmI+16]
				PointeurWhereAmI += 16
		#Extraction du champ "Collimation Error" (2 octets)
		if "CollimationError" in FSPECRempli:
			if FSPECRempli["CollimationError"] :
				self.CollimationError = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#******************** Ces 2 champs ne sont pas documentés *******************************
		#Extraction du champ "Reserved Expansion Field" (1 octet + 1octet +)
		if "ReservedExpField" in FSPECRempli:
			if FSPECRempli["ReservedExpField"] :
				#self.ReservedExpField = (DataBlock[PointeurWhereAmI:PointeurWhereAmI+6])
				#PointeurWhereAmI += 6
				pass
		#Extraction du champ "Special Purpose Field" (1 octet + 1octet + )
		if "SpecialPurposeField" in FSPECRempli:
			if FSPECRempli["SpecialPurposeField"] :
				#self.SpecialPurposeField = (DataBlock[PointeurWhereAmI:PointeurWhereAmI+6])
				#PointeurWhereAmI += 6
				pass
		return self, PointeurWhereAmI/2


#*********************************************************************************************************************
#*******************************************   		CATEGORIE 48          ********************************************
#*********************************************************************************************************************

#**************************** TargetReportDescExtractedCAT48 *********************************************************
#J'extrait les items du champ : Target Report Descriptor
class TargetReportDescExtractedCAT48(Packet):
	name="Detail du Data Item : Target Report Descriptor"
	fields_desc = [IntEnumField("TYP", None, {0:"No detection", 1:"Single PSR detection", 2:"Single SSR detection", 3:"SSR + PSR detection", 4:"Single ModeS All-Cal", 5:"Single ModeS Roll-Call", 6:"ModeS All-Call + PSR", 7:"ModeS Roll-Call +PSR"}),
				   IntEnumField("SIM", None, {0:"Actual target report", 1:"Simulated target report"}),
				   IntEnumField("RDP", None, {0:"Report from RDP Chain 1", 1:"Report from RDP Chain 2"}),
				   IntEnumField("SPI", None, {0:"Absence of SPI", 1:"Special Position Identification"}),
				   IntEnumField("RAB", None, {0:"Report from aircraft transponder", 1:"Fixed Transponder"}),
				   IntEnumField("TST", None, {0:"Real target report", 1:"Test target report"}),
				   IntEnumField("ME", None, {0:"No military emergency", 1:"Military emergency"}),
				   IntEnumField("MI", None, {0:"No military identification", 1:"Military identification"}),
				   IntEnumField("FOE_FRI", None, {0:"No Mode 4 interrogation", 1:"Friendly target", 2:"Unknown target", 3:"No reply"}),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.TYP = int(tmp[0:3],2)
		self.SIM = int(tmp[3],2)
		self.RDP = int(tmp[4],2)
		self.SPI = int(tmp[5],2)
		self.RAB = int(tmp[6],2)
		if int(tmp[7],2):
			self.TST = int(tmp[8],2)
			self.ME = int(tmp[11],2)
			self.MI = int(tmp[12],2)
			self.FOE_FRI = int(tmp[13:15],2)
		return self
	

#**************************** ModeACodeInOctalExtractedCAT48 *********************************************************
#J'extrait les items du champ : Mode-3/A Code in Octal Representation
class ModeACodeInOctalExtractedCAT48(Packet):
	name="Detail du Data Item : Mode-3/A Code in Octal Representation"
	fields_desc = [IntEnumField("Valid", None, {0:"Code Validated", 1:"Code Not Validated"}),
				   IntEnumField("Garbled", None, {0:"Default", 1:"Garbled Code"}),
				   IntEnumField("L", None, {0:"Code derived from the reply of the transponder", 1:"Code not extracted during the last scan"}),
				   StrField("CodeModeA", ""),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.Valid = int(tmp[0],2)
		self.Garbled = int(tmp[1],2)
		self.L = int(tmp[2],2)
		i=4
		while i<len(tmp):
			self.CodeModeA = self.CodeModeA +  str(int(tmp[i:i+3],2)) 
			i+=3
		return self
	

#**************************** FlightLevelBinExtractedCAT48 ***********************************************************
#J'extrait les items du champ : Flight Level in Binary Representation
class FlightLevelBinExtractedCAT48(Packet):
	name="Detail du Data Item : Flight Level in Binary Representation"
	fields_desc = [IntEnumField("Valid", None, {0:"Code Validated", 1:"Code Not Validated"}),
				   IntEnumField("Garbled", None, {0:"Default", 1:"Garbled Code"}),
				   ShortField("FlightLevel", 0),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(16)
		self.Valid = int(tmp[0],2)
		self.Garbled = int(tmp[1],2)
		self.FlightLevel = trunc(int(tmp[2:],2)*(4**-1))
		return self


#*************************** RadarPlotCaracExtractedCAT48 ************************************************************
#J'extrait les items du champ : Radar plot characteristics
class RadarPlotCaracExtractedCAT48(Packet):
	name="Detail du Data Item : Radar plot characteristics"
	fields_desc = [ShortField("SRL", None),		#SSR plot runlength
				   IntField("SRR", None),		#Number of received replies for (M)SSR
				   IntField("SAM", None),		#Amplitude of (M)SSR reply
				   ShortField("PRL", None),		#Primary plot runlength
				   IntField("PAM", None),		#Amplitude of Primary plot
				   ShortField("RPD", None),		#Difference in Range between PSR and SSR plot		   
				   ShortField("APD", None),		#Difference in Azimut between PSR and SSR plot		   
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		pointeurWhoAmI=8		#il pointe initialement au debut du 2ie octet de l'item
		if tmp[0]:			# presence du champ SRL
			#champ SRL, LSB = 360 / 2¹³ degres (0.044dg)
			self.SRL = round( int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2) * (360 * 2**-13), 3 )
			pointeurWhoAmI+=8
		if tmp[1]=="1":			# presence du champ SRR
			#champ SRR, LSB = 1
			self.SRR = int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2)
			pointeurWhoAmI+=8
		if tmp[2]=="1":			# presence du champ SAM
			#champ SAM, LSB = 1 dBm
			self.SAM = int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2)
			pointeurWhoAmI+=8
		if tmp[3]=="1":			# presence du champ PRL
			#champ PRL, LSB = 360 / 2¹³ degres (0.044dg)
			self.PRL = round( int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2) * (360 * 2**-13), 3 )
			pointeurWhoAmI+=8
		if tmp[4]=="1":			# presence du champ PRL
			#champ PAM, LSB = 1 dBm
			self.PAM = int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2)
			pointeurWhoAmI+=8
		if tmp[5]=="1":			# presence du champ PRL
			#champ RPD, LSB = 1/256 NM
			self.RPD = round( int(tmp[pointeurWhoAmI:pointeurWhoAmI+8],2) * (256**-1), 2 )
			pointeurWhoAmI+=8
		if tmp[6]=="1":			# presence du champ SRL
			#champ APD, LSB = 360 / 2^14 degres (environ = 0.02197)  ;   -360/2^7<APD<360/2^7
			if tmp[pointeurWhoAmI]=="1":
				self.APD = round( (~int(tmp[pointeurWhoAmI+1:pointeurWhoAmI+8],2)) * (360 * (2**-14)), 3 )  
				print "int(tmp[pointeurWhoAmI+1:pointeurWhoAmI+8],2) = ", int(tmp[pointeurWhoAmI+1:pointeurWhoAmI+8],2)
				if (self.APD < (-360*2**-7)):   # environ = -2.8125
					self.APD = round((-360*2**-7), 3)   ()
			else:
				self.APD = round( int(tmp[pointeurWhoAmI+1:pointeurWhoAmI+8],2) * (360 * 2**-14), 3 )
				if (self.APD > (360*2**-7)): 	# environ = +2.8125
					self.APD = round((360*2**-7), 3)
			pointeurWhoAmI+=8
		return self


#*************************** TrackStatusExtractedCAT48 ***************************************************************
#J'extrait les items du champ : Track Status
class TrackStatusExtractedCAT48(Packet):
	name="Detail du Data Item : Track Status"
	fields_desc = [IntEnumField("CNF", None, {0:"Confirmed Track", 1:"Tentative Track"}),		#Confirmed vs. Tentative Track
				   #Type of Sensor(s) maintaining Track 
				   IntEnumField("RAD", None, {0:"Combined Track", 1:"PSR Track", 2:"SSR/Mode S Track", 3:"Invalid"}),		
				   #Signals level of confidence in plot to track association process
				   IntEnumField("DOU", None, {0:"Normal confidence ", 1:"Low confidence in plot to track association"}),		
				   #Manoeuvre detection in Horizontal Sense
				   IntEnumField("MAH", None, {0:"No horizontal Manoeuvre sensed", 1:"Horizontal Manoeuvre sensed"}),
				   #Climbing / Descending Mode 
				   IntEnumField("CDM", None, {0:"Maintaining", 1:"Climbing", 2:"Descending", 3:"Invalid"}),
				   #Signal for End_of_Track
				   IntEnumField("TRE", None, {0:"Track still alive", 1:"End of track lifetime"}),		
				   #Ghost vs. true target
				   IntEnumField("GHO", None, {0:"True target track", 1:"Ghost target track"}),
				   #Track maintained with track information from neighbouring Node B on the cluster, or network
				   IntEnumField("SUP", None, {0:"No Information", 1:"Track maintained with track information"}),
				   #Type of plot coordinate transformation mechanism
				   IntEnumField("TCC", None, {0:"Tracking performed in so-called 'Radar Plane'", 1:"Slant range correction"}),
				   ]
	
	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.CNF = int(tmp[0],2)
		self.RAD = int(tmp[1:3],2)
		self.DOU = int(tmp[3],2)
		self.MAH = int(tmp[4],2)
		self.CDM = int(tmp[5:7],2)
		if tmp[7]=="1":			# Il y a une extension
			self.TRE = int(tmp[8],2)
			self.GHO = int(tmp[9],2)  
			self.SUP = int(tmp[10],2)  
			self.TCC = int(tmp[11],2)  
		return self


#*************************** ModeACodeIndicatorExtractedCAT48 ********************************************************
#J'extrait les items du champ : Mode-3/A Code Confidence Indicator
class ModeACodeIndicatorExtractedCAT48(Packet):
	name="Detail du Data Item : Mode-3/A Code Confidence Indicator"
	fields_desc = [IntEnumField("QA4", None, {0:"High quality pulse A4", 1:"Low quality pulse A4"}),	
				   IntEnumField("QA2", None, {0:"High quality pulse A2", 1:"Low quality pulse A2"}),
				   IntEnumField("QA1", None, {0:"High quality pulse A1", 1:"Low quality pulse A1"}),
				   IntEnumField("QB4", None, {0:"High quality pulse B4", 1:"Low quality pulse B4"}),
				   IntEnumField("QB2", None, {0:"High quality pulse B2", 1:"Low quality pulse B2"}),
				   IntEnumField("QB1", None, {0:"High quality pulse B1", 1:"Low quality pulse B1"}),
				   IntEnumField("QC4", None, {0:"High quality pulse C4", 1:"Low quality pulse C4"}),
				   IntEnumField("QC2", None, {0:"High quality pulse C2", 1:"Low quality pulse C2"}),
				   IntEnumField("QC1", None, {0:"High quality pulse C1", 1:"Low quality pulse C1"}),
				   IntEnumField("QD4", None, {0:"High quality pulse D4", 1:"Low quality pulse D4"}),
				   IntEnumField("QD2", None, {0:"High quality pulse D2", 1:"Low quality pulse D2"}),
				   IntEnumField("QD1", None, {0:"High quality pulse D1", 1:"Low quality pulse D1"}),
				   ]
	
	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.QA4 = int(tmp[4],2)
		self.QA2 = int(tmp[5],2)
		self.QA1 = int(tmp[6],2)
		self.QB4 = int(tmp[7],2)
		self.QB2 = int(tmp[8],2)
		self.QB1 = int(tmp[9],2)
		self.QC4 = int(tmp[10],2)
		self.QC2 = int(tmp[11],2)
		self.QC1 = int(tmp[12],2)
		self.QD4 = int(tmp[13],2)
		self.QD2 = int(tmp[14],2)
		self.QD1 = int(tmp[15],2)
		return self


#******************************** ModeCCodeIndicatorExtractedCAT48 ********************************************************
#J'extrait les items du champ : Mode-C Code and Code Confidence Indicator 
class ModeCCodeIndicatorExtractedCAT48(Packet):
	name="Detail du Data Item : Mode-C Code and Code Confidence Indicator "
	fields_desc = [IntEnumField("Valid", None, {0:"Code Validated", 1:"Code Not Validated"}),
				   IntEnumField("Garb", None, {0:"Default", 1:"Garbled code"}),
				   IntField("ModeC", None),
				   IntEnumField("QC1", None, {0:"High quality pulse C1", 1:"Low quality pulse C1"}),
				   IntEnumField("QA1", None, {0:"High quality pulse A1", 1:"Low quality pulse A1"}),
				   IntEnumField("QC2", None, {0:"High quality pulse C2", 1:"Low quality pulse C2"}),
				   IntEnumField("QA2", None, {0:"High quality pulse A2", 1:"Low quality pulse A2"}),
				   IntEnumField("QC4", None, {0:"High quality pulse C4", 1:"Low quality pulse C4"}),
				   IntEnumField("QA4", None, {0:"High quality pulse A4", 1:"Low quality pulse A4"}),	
				   IntEnumField("QB1", None, {0:"High quality pulse B1", 1:"Low quality pulse B1"}),
				   IntEnumField("QD1", None, {0:"High quality pulse D1", 1:"Low quality pulse D1"}),
				   IntEnumField("QB2", None, {0:"High quality pulse B2", 1:"Low quality pulse B2"}),
				   IntEnumField("QD2", None, {0:"High quality pulse D2", 1:"Low quality pulse D2"}),
				   IntEnumField("QB4", None, {0:"High quality pulse B4", 1:"Low quality pulse B4"}),
				   IntEnumField("QD4", None, {0:"High quality pulse D4", 1:"Low quality pulse D4"}),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.Valid = int(tmp[0],2)
		self.Garb = int(tmp[1],2)
		self.ModeC = gray2dec(tmp[4:16])
		self.QC1 = int(tmp[20],2)
		self.QA1 = int(tmp[21],2)
		self.QC2 = int(tmp[22],2)
		self.QA2 = int(tmp[23],2)
		self.QC4 = int(tmp[24],2)
		self.QA4 = int(tmp[25],2)
		self.QB1 = int(tmp[26],2)
		self.QD1 = int(tmp[27],2)
		self.QB2 = int(tmp[28],2)
		self.QD2 = int(tmp[29],2)
		self.QB4 = int(tmp[30],2)
		self.QD4 = int(tmp[31],2)
		return self


#******************************** RadialDopplerSpeedExtractedCAT48 ********************************************************
#J'extrait les items du champ : Radial Doppler Speed
class RadialDopplerSpeedExtractedCAT48(Packet):
	name="Detail du Data Item : Radial Doppler Speed"
	fields_desc = [IntEnumField("D", None, {0:"Doppler speed is valid", 1:"Doppler speed is doubtful"}),  
				   IntField("CAL", None),			#Calculated Doppler Speed
				   IntField("REP", None),			#Repetition factor
				   IntField("DOP", None),			#Doppler Speed
				   IntField("AMB", None),			#Ambiguity Range
				   IntField("FRQ", None),			#Transmitter Frequency
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		CalOK=int(tmp[0],2)
		if CalOK:       #Presence du sous champ Calculated Doppler Speed
			#Is Doppler speed valid ?
			self.D = int(tmp[8],2)
			#Calculated Doppler Speed, coded in two’s complement       LSB= 1 m/sec
			if tmp[14]=="1":	#Presence du sous champ Raw Doppler Speed
				self.CAL = ~int(tmp[15:24],2)
			else:
				self.CAL = int(tmp[15:24],2)
		if tmp[1]=="1":		# Le sous champ RDS est présent
			self.REP = int(tmp[ 8+16*CalOK : 8+16*CalOK+8 ],2)			#Repetition Factor
			self.DOP = int(tmp[ 16+16*CalOK : 16+16*CalOK+16 ],2)		#Doppler Speed   ;   LSB= 1 m/sec
			self.AMB = int(tmp[ 32+16*CalOK : 32+16*CalOK+16 ],2)		#Ambiguity Range ;   LSB= 1 m/sec
			self.FRQ = int(tmp[ 48+16*CalOK : ],2)						#Transmitter Frequency  ;  LSB= 1 Mhz
		return self


#******************************** ACASCapabilityExtractedCAT48 ************************************************************
#J'extrait les items du champ : Communications/ACAS Capability and Flight Status
class ACASCapabilityExtractedCAT48(Packet):
	name="Detail du Data Item : Communications/ACAS Capability and Flight Status"
						#Communications capability of the transponder
	fields_desc = [IntEnumField("COM", None, {0:"No communications capability (surveillance only)", 1:"Comm. A and B capability",
											  2:"Comm. A, B and Uplink ELM", 3:"Comm. A, B, Uplink ELM and Downlink ELM",
											  4:"Level 5 Transponder capability",}),
				   #Flight Status
				   IntEnumField("STAT", None, {0:"No alert, no SPI, aircraft airborne", 1:"No alert, no SPI, aircraft on ground",
											   2:"Alert, no SPI, aircraft airborne", 3:"Alert, no SPI, aircraft on ground",
											   4:"Alert, SPI, aircraft airborne or on ground", 5:"No alert, SPI, aircraft airborne or on ground"}),
				   #SI/II Transponder Capability
				   IntEnumField("SI", None, {0:"SI-Code Capable", 1:"II-Code Capable"}),
				   #Mode-S Specific Service Capability
				   IntEnumField("MSSC", None, {0:"No Mode-S Specific Service Capability", 1:"Yes Mode-S Specific Service Capability"}),
				   #Altitude reporting capability
				   IntEnumField("ARC", None, {0:"100 ft resolution", 1:"25 ft resolution"}),
				   #Aircraft identification capability
				   IntEnumField("AIC", None, {0:"No Aircraft identification capability", 1:"Yes, Aircraft identification capability"}),
				   IntField("BDS1_Bit16", None),	#BDS 1,0 bit 16 
				   IntField("BDS1_Bit3740", None), 	#BDS 1,0 bits 37/40
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		if int(tmp[:3],2)<5:
			self.COM = int(tmp[:3],2)		#Communications capability of the transponder
		if int(tmp[3:6],2)<6:
			self.STAT = int(tmp[3:6],2)		#Flight Status
		self.SI = int(tmp[6],2)				#SI/II Transponder Capability
		self.MSSC = int(tmp[8],2)			#Mode-S Specific Service Capability
		self.ARC = int(tmp[9],2)			#Altitude reporting capability
		self.AIC = int(tmp[10],2)			#Aircraft identification capability
		self.BDS1_Bit16 = int(tmp[11],2)	#BDS 1,0 bit 16 
		self.BDS1_Bit3740 = int(tmp[12:],2)	#BDS 1,0 bits 37/40
		return self


#******************************** Mode1CodeOctalExtractedCAT48 ************************************************************
#J'extrait les items du champ : Mode-1 Code in Octal Representation
class Mode1CodeOctalExtractedCAT48(Packet):
	name="Detail du Data Item : Mode-1 Code in Octal Representation"
	fields_desc = [IntEnumField("Valid", None, {0:"Code Validated", 1:"Code Not Validated"}),
				   IntEnumField("Garbled", None, {0:"Default", 1:"Garbled Code"}),
				   IntEnumField("L", None, {0:"Mode-1 Code derived from the reply of the transponder", 1:"Smoothed Mode-1 code as provided by a local tracker"}),
				   StrField("CodeMode1", ""),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.Valid = int(tmp[0],2)
		self.Garbled = int(tmp[1],2)
		self.L = int(tmp[2],2)
		self.CodeMode1 = self.CodeMode1 + str(int(tmp[3:6],2)) 
		self.CodeMode1 = self.CodeMode1 + str(int(tmp[6:],2)) 
		return self


#******************************** Mode2CodeOctalExtractedCAT48 ************************************************************
#J'extrait les items du champ : Mode-2 Code in Octal Representation
class Mode2CodeOctalExtractedCAT48(Packet):
	name="Detail du Data Item : Mode-2 Code in Octal Representation"
	fields_desc = [IntEnumField("Valid", None, {0:"Code Validated", 1:"Code Not Validated"}),
				   IntEnumField("Garbled", None, {0:"Default", 1:"Garbled Code"}),
				   IntEnumField("L", None, {0:"Mode-2 Code derived from the reply of the transponder", 1:"Smoothed Mode-2 code as provided by a local tracker"}),
				   StrField("CodeMode2", "")		#Mode-2 code in octal representation 
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.Valid = int(tmp[0],2)
		self.Garbled = int(tmp[1],2)
		self.L = int(tmp[2],2)
		i=4
		while (i<(len(tmp))):
			self.CodeMode2 = self.CodeMode2 + str(int(tmp[i:i+3],2))
			i+=3
		return self
	

#******************************** Mode1CodeIndicatorExtractedCAT48 ********************************************************
#J'extrait les items du champ : Mode-1 Code Confidence Indicator
class Mode1CodeIndicatorExtractedCAT48(Packet):
	#Confidence level for each bit of a Mode-1 reply as provided by a monopulse SSR station.
	name="Detail du Data Item : Mode-1 Code Confidence Indicator "
	fields_desc = [IntEnumField("QA4", None, {0:"High quality pulse A4", 1:"Low quality pulse A4"}),	
				   IntEnumField("QA2", None, {0:"High quality pulse A2", 1:"Low quality pulse A2"}),
				   IntEnumField("QA1", None, {0:"High quality pulse A1", 1:"Low quality pulse A1"}),
				   IntEnumField("QB2", None, {0:"High quality pulse B2", 1:"Low quality pulse B2"}),
				   IntEnumField("QB1", None, {0:"High quality pulse B1", 1:"Low quality pulse B1"}),
				   ]

	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.QA4 = int(tmp[3],2)
		self.QA2 = int(tmp[4],2)
		self.QA1 = int(tmp[5],2)
		self.QB2 = int(tmp[6],2)
		self.QB1 = int(tmp[7],2)
		return self


#******************************** ModeACodeIndicatorExtractedCAT48 ********************************************************
#J'extrait les items du champ : Mode-2 Code Confidence Indicator
class Mode2CodeIndicatorExtractedCAT48(Packet):
	#Confidence level for each bit of a Mode-2 reply as provided by a monopulse SSR station
	name="Detail du Data Item : Mode-2 Code Confidence Indicator"
	fields_desc = [IntEnumField("QA4", None, {0:"High quality pulse A4", 1:"Low quality pulse A4"}),	
				   IntEnumField("QA2", None, {0:"High quality pulse A2", 1:"Low quality pulse A2"}),
				   IntEnumField("QA1", None, {0:"High quality pulse A1", 1:"Low quality pulse A1"}),
				   IntEnumField("QB4", None, {0:"High quality pulse B4", 1:"Low quality pulse B4"}),
				   IntEnumField("QB2", None, {0:"High quality pulse B2", 1:"Low quality pulse B2"}),
				   IntEnumField("QB1", None, {0:"High quality pulse B1", 1:"Low quality pulse B1"}),
				   IntEnumField("QC4", None, {0:"High quality pulse C4", 1:"Low quality pulse C4"}),
				   IntEnumField("QC2", None, {0:"High quality pulse C2", 1:"Low quality pulse C2"}),
				   IntEnumField("QC1", None, {0:"High quality pulse C1", 1:"Low quality pulse C1"}),
				   IntEnumField("QD4", None, {0:"High quality pulse D4", 1:"Low quality pulse D4"}),
				   IntEnumField("QD2", None, {0:"High quality pulse D2", 1:"Low quality pulse D2"}),
				   IntEnumField("QD1", None, {0:"High quality pulse D1", 1:"Low quality pulse D1"}),
				   ]
	
	#Determine la présence ou non des items du DataField
	def DecodDataField(self, Val):
		tmp = bin(int(Val,16))[2:].zfill(len(Val)*4)
		self.QA4 = int(tmp[4],2)
		self.QA2 = int(tmp[5],2)
		self.QA1 = int(tmp[6],2)
		self.QB4 = int(tmp[7],2)
		self.QB2 = int(tmp[8],2)
		self.QB1 = int(tmp[9],2)
		self.QC4 = int(tmp[10],2)
		self.QC2 = int(tmp[11],2)
		self.QC1 = int(tmp[12],2)
		self.QD4 = int(tmp[13],2)
		self.QD2 = int(tmp[14],2)
		self.QD1 = int(tmp[15],2)
		return self


#******************************** ExtractDetailRecord48 *******************************************************************
class ExtractDetailRecord48(Packet):
	name="Detail du DataRecord de la trame Asterix CAT 48"
	fields_desc = [XLongField("FSPEC", None),				#4 octets max
				   FieldListField("SACSIC", None, []),		#Liste contenant le SAC et le SIC (2 octets)
				   StrField("TimeDay",None),				#3octets
				   PacketListField("TargetReportDesc", None, TargetReportDescExtractedCAT48),	#1 octet + 1 extension
				   FieldListField("PositionPolar",None, []),		#4 octets
				   PacketListField("ModeACodeInOctal", None, ModeACodeInOctalExtractedCAT48),	#2 octets
				   PacketListField("FlightLevelBin", None, FlightLevelBinExtractedCAT48),		#2 octets
				   PacketListField("RadarPlotCarac", None, RadarPlotCaracExtractedCAT48),		#1 octets + 7 ext max
				   X3BytesField("AircraftAdr",None),		#3 octets
				   StrField("AircraftID", ""),				#6 octets
				   FieldListField("ModeSData",None, []),	#1 octet + N * 8octets
				   IntField("TrackNbr", None),				#2 octets
				   FieldListField("PositionCartesian", None, []),	#4 octets
				   FieldListField("TrackVelocityPolar", None, []),	#4 octets
				   PacketListField("TrackStatus", None, TrackStatusExtractedCAT48),		#1 octet + 1 octet extension
				   FieldListField("TrackQuality", None, []),#4 octets
				   IntEnumField("WarningConditions", None, {0:"Not defined", 1:"Multipath Reply (Reflection)", 2:"Reply due to sidelobe interrogation/reception", 3:"Split plot", 4:"Second time around reply", 5:"Angel", 6:"Terrestrial vehicle", 7:"Fixed PSR plot", 8:"Slow PSR target", 9:"Low quality PSR plot", 10:"Phantom SSR plot", 11:"Non-Matching Mode-3/A Code", 12:"Mode C code / Mode S altitude code abnormal value compared to the track", 13:"Target in Clutter Area", 14:"Maximum Doppler Response in Zero Filter", 15:"Transponder anomaly detected", 16:"Duplicated or Illegal Mode S Aircraft Address", 17:"Mode S error correction applied", 18:"Undecodable Mode C code / Mode S altitude code", 19:"Birds", 20:"Flock of Birds", 21:"Mode 1 was present in original reply", 22:"Mode 2 was present in original reply"}), 
				   PacketListField("ModeACodeIndicator", None, ModeACodeIndicatorExtractedCAT48),	#2 octets
				   PacketListField("ModeCCodeIndicator", None, ModeCCodeIndicatorExtractedCAT48),	#4 octets
				   IntField("HeightMeasured3DRad", None),	#2 octets
				   PacketListField("RadialDopplerSpeed", None, RadialDopplerSpeedExtractedCAT48),	#1 octet + 9 extensions max
				   PacketListField("ACASCapability", None, ACASCapabilityExtractedCAT48),		#2 octets
				   XLongField("ACASResolution", None),		#7 octets
				   PacketListField("Mode1CodeOctal", None, Mode1CodeOctalExtractedCAT48),		#1 octet
				   PacketListField("Mode2CodeOctal", None, Mode2CodeOctalExtractedCAT48),		#2 octets
				   PacketListField("Mode1CodeIndicator", None, Mode1CodeIndicatorExtractedCAT48),	#1 octet
				   PacketListField("Mode2CodeIndicator", None, Mode2CodeIndicatorExtractedCAT48)	#2 octets
#				   XLongField("SpecialField", None),		#1 octet + 1octet +
#				   XLongField("ReservedExpansionField", None) #1 octet + 1octet +		 
				  ]
		
	#***********************************************************************************************************
	#Fonction qui isole le champ FSPEC du reste des données
	#En Entree : toutes les donnees de la partie DataRecord (str)
	#En Sortie : uniquement le FSPEC (str), et le nombre d'octets (int)
	def IsoleFSPEC(self, DataRecord):
		i=0
		tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(8)
		while (tmp[-1:]=="1"):
			if ((i+2)>8): # On evite de dépasser la taille maximale du FSPEC = 4 octets
				break
			i+=2
			tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(len(DataRecord[i:i+2])*4)
		LastBit=(i+2)
		NbOctetFSPEC=(i+2)/2
		return DataRecord[0:LastBit], NbOctetFSPEC
	
	#********************************** RemplirFSPEC **************************************************************** 
	# Cette fonction rempli un dictionnaire associant le nom de l'item et la valeur dans le FSPEC
	# En entrée : le champ FSPEC uniquement, en chaine de caractères, et la catégorie = entier
	# En sortie : une liste de tuple
	def RemplirFSPEC(self, FSPECField):
		FSPEC48listkey = ["DataSRCID", "TimeDay", "TargetReportDesc", "PositionPolar", "ModeACodeInOctal",
						  "FlightLevelBin", "RadarPlotCarac", "FX1", "AircraftAdr", "AircraftID", "ModeSData",
						  "TrackNbr", "PositionCartesian", "TrackVelocityPolar", "TrackStatus", "FX2", "TrackQuality",
						  "WarningConditions", "ModeACodeIndicator", "ModeCCodeIndicator", "HeightMeasured3DRad",
						  "RadialDopplerSpeed", "ACASCapability", "FX3", "ACASResolution", "Mode1CodeOctal",
						  "Mode2CodeOctal", "Mode1CodeIndicator", "Mode2CodeIndicator", "SpecialField",
						  "ReservedExpansionField", "FX4"]
		
		#converion hexa en binaire, avec retrait des caractères 0b en debut de chaine, et remplissage en début de tableau
		FSPEClistval1 = bin(int(FSPECField, 16))[2:].zfill(len(FSPECField)*4)
		FSPEClistval2=[0]*(len(FSPEClistval1))
		#Conversion des caractères en integer
		for i in range(len(FSPEClistval1)):
			FSPEClistval2[i]=int(FSPEClistval1[i],2)
		#zip combine les 2 listes en 1 : [("DataSRCID", 1), ...]
		return dict(zip(FSPEC48listkey,FSPEClistval2))


	#************************************ DecodRecord48EnDetail ************************************************************
	# Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 48
	# En Entrée : prend le bloc DataRecord en entier
	# En sortie : renvoie le contenu du Record + la longueur du record, FSPEC compris
	def DecodRecord48Detail(self, DataBlock):
		#print "************************************** DECOD RECORD 48 **************************************"
		#FSPEC est un dictionnaire : {"DataSRCID" : 1, ...}
		NbOctetsFSPEC=0
		FSPEC, NbOctetsFSPEC = self.IsoleFSPEC(DataBlock)
		FSPECRempli = self.RemplirFSPEC(FSPEC)
		self.FSPEC = FSPEC
		PointeurWhereAmI = NbOctetsFSPEC*2
		#Extraction du SAC/SIC (2 octets)
		if "DataSRCID" in FSPECRempli:
			if FSPECRempli["DataSRCID"] :
				self.SACSIC.append(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2])
				self.SACSIC.append(DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Extraction de l'heure du jour (3 octets)	;  LSB = 1/128 seconds 
		if FSPECRempli.has_key("TimeDay"):
			if FSPECRempli["TimeDay"]:
				secondes = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+6],16)/128
				if (secondes<=86400):
					self.TimeDay = str(datetime.timedelta(seconds=secondes))
				PointeurWhereAmI += 6
		#Extraction du Target Report Descriptor (1 octet + 1 extension)
		if 	"TargetReportDesc" in FSPECRempli:
			if FSPECRempli["TargetReportDesc"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				tmp2 = TargetReportDescExtractedCAT48()
				self.TargetReportDesc = tmp2.DecodDataField(DataBlock[PointeurWhereAmI : PointeurWhereAmI + 2 * (2**int(tmp[-1:],2))] )
				PointeurWhereAmI += 2 * (2**int(tmp[-1:],2))
		#Extraction "Measured Position in Slant Polar Coordinates" (4octets)
		if 	"PositionPolar" in FSPECRempli:
			if FSPECRempli["PositionPolar"] :
				#Detail de la mesure de la position en coordonnées polaires
				#RHO, LSB = 1/256NM
				self.PositionPolar.append( round( float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])/256, 3 ) )
				#THETA, LSB = 1/256NM
				self.PositionPolar.append( round( float.fromhex(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+8])/256, 3 ) )
				PointeurWhereAmI += 8
		#Extraction Mode-3/A Code in Octal Representation (2 octets)
		if "ModeACodeInOctal" in FSPECRempli:
			if FSPECRempli["ModeACodeInOctal"] :
				#Detail de la mesure de la position en coordonnées polaires
				tmp=ModeACodeInOctalExtractedCAT48()
				self.ModeACodeInOctal = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Extraction du Flight Level in Binary Representation (2 octets)
		if "FlightLevelBin" in FSPECRempli:
			if FSPECRempli["FlightLevelBin"] :
				#Detail du sous champ Flight Level in Binary Representation
				tmp = FlightLevelBinExtractedCAT48()
				self.FlightLevelBin = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Extraction de Radar Plot Characteristics (1 octet + 7 octets extensions au max)
		if "RadarPlotCarac" in FSPECRempli:
			if FSPECRempli["RadarPlotCarac"] :
				tmp= bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				tmp2 = RadarPlotCaracExtractedCAT48()
				NbSubField=0	# Compte le nombre de subfield de ce Data Item
				if (tmp[-1:]=="1"):
					for i in range(len(tmp)-1):
						if tmp[i]=="1":
							NbSubField += 1
					self.RadarPlotCarac = tmp2.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+NbSubField*2])
				PointeurWhereAmI += 2 + (NbSubField * 2)
		#Bit Extension
		if "FX1" in FSPECRempli:
			if (FSPECRempli["FX1"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		
		#Extraction du champ Aircraft Adress  (3 octets) , On le note en hexadecimal
		if "AircraftAdr" in FSPECRempli:
			if FSPECRempli["AircraftAdr"] :
				self.AircraftAdr = DataBlock[PointeurWhereAmI:PointeurWhereAmI+6]
				PointeurWhereAmI += 6
		#Extraction du champ Aircraft Identification	(6 octets)
		if "AircraftID" in FSPECRempli:
			if FSPECRempli["AircraftID"] :
				#Detail du sous champ Aircraft Identification : 8 caractères. Chaque caractère est codé sur 6 bits
				tmp=bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+12],16))[2:].zfill(48)
				i=0
				#A à Z codé de 1 à 26; 0 à 9 codé de 48 à 57, espace codé par 32
				while i<48:
					if int(tmp[i:i+6],2)<32:
						self.AircraftID = self.AircraftID + chr(int(tmp[i:i+6],2)+64)
					else:
						self.AircraftID = self.AircraftID + chr(int(tmp[i:i+6],2))
					i+=6
				PointeurWhereAmI += 12
		#Extraction des Data Mode S 	(9 octets) : 1 octet (N=repetition) + N*8 octets
		if "ModeSData" in FSPECRempli:
			if FSPECRempli["ModeSData"] :
				Rep = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)
				self.ModeSData.append(Rep)
				pointeur = PointeurWhereAmI+2			 #pointe sur le 1ier bit apres l'octet REP
				for i in range(Rep):
					self.ModeSData.append((DataBlock[pointeur:pointeur+14],DataBlock[pointeur+14:pointeur+16]))
					pointeur+=16
				PointeurWhereAmI += 2 + (16*Rep)
		#Extraction du champ Track Number	: longeur de 2 octets, mais codé sur 12 bits
		if "TrackNbr" in FSPECRempli:
			if FSPECRempli["TrackNbr"] :
				self.TrackNbr = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4], 16)
				PointeurWhereAmI += 4
		#Extraction du champ "Calculated Position in Cartesian Coordinates"	: 4 octets (X-component sur 2 octets, Y-component sur 2 octets)
		if "PositionCartesian" in FSPECRempli:
			if FSPECRempli["PositionCartesian"] :
				self.PositionCartesian.append( round(float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])/128,3) )
				self.PositionCartesian.append( round(float.fromhex(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+8])/128,3) )
				PointeurWhereAmI += 8
		#Extraction du champ "Calculated Track Velocity in Polar Representation" 	(4 octets)
		if "TrackVelocityPolar" in FSPECRempli:
			if FSPECRempli["TrackVelocityPolar"] :
				#CALCULATED GROUNDSPEED (max. 2 NM/s) sur 2 octets ; (LSB)   =  (2^-14) NM/s   =  approx. 0.22 kt 
				self.TrackVelocityPolar.append( round(float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])*(2**-14),3) )
				#CALCULATED HEADING sur 2 octets ; (LSB) = 360°/ 2^16 =  approx. 0.0055° 
				self.TrackVelocityPolar.append( round(float.fromhex(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+8])*(360*(2**-16)),3) )
				PointeurWhereAmI += 8
		#Extraction du champ "Track Status"	(1 octet + 1 octet extension)
		if "TrackStatus" in FSPECRempli:
			if FSPECRempli["TrackStatus"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				tmp2 = TrackStatusExtractedCAT48()
				self.TrackStatus = tmp2.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2*2**(int(tmp[-1]))])
				PointeurWhereAmI += 2*( 2**int(tmp[-1],2) )
		#Bit Extension
		if "FX2" in FSPECRempli:
			if (FSPECRempli["FX2"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		
		#Extraction du champ "Track Quality" 	(4 octets)
		if "TrackQuality" in FSPECRempli:
			if FSPECRempli["TrackQuality"] :
				#Sigma(X) : Standard Deviation on the horizontal axis of the local grid system   ;  LSB = 1/128 NM ; 0<= Sigma(X)<2 NM
				self.TrackQuality.append( round(float.fromhex(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2])/128, 3) )
				#Sigma(Y) : Standard Deviation on the vertical axis of the local grid system   ;  LSB = 1/128 NM  ; 0<= Sigma (Y)<2 NM
				self.TrackQuality.append( round(float.fromhex(DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4])/128, 3) )
				#Sigma(V) : Standard Deviation on the groundspeed within the local grid system; LSB = (2^-14) NM/s = 0.22 Kt; 0<=Sigma (V)<56.25Kt
				self.TrackQuality.append( round(float.fromhex(DataBlock[PointeurWhereAmI+4:PointeurWhereAmI+6])*0.22, 3) )
				#Sigma(H) : Standard Deviation on the heading within the local grid system ; LSB = 360/(2^12) degrees = 0.08789 degrees;  0<=sigma(H)<22.5 degrees
				self.TrackQuality.append( round(float.fromhex(DataBlock[PointeurWhereAmI+6:PointeurWhereAmI+8])*360*(2**-12), 3) )
				PointeurWhereAmI += 8
		#Extraction du champ "Warning/Errors conditions" 	(1 octet)
		if "WarningConditions" in FSPECRempli:
			if FSPECRempli["WarningConditions"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				if int(tmp[:-1],2)<=22:
					self.WarningConditions = int(tmp[:-1],2)
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-3/A Code Confidence Indicator " 	(2 octets)
		if "ModeACodeIndicator" in FSPECRempli:
			if FSPECRempli["ModeACodeIndicator"] :
				tmp = ModeACodeIndicatorExtractedCAT48()
				self.ModeACodeIndicator = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Extraction du champ "Mode-C Code and Confidence Indicator " 	(4 octets)
		if "ModeCCodeIndicator" in FSPECRempli:
			if FSPECRempli["ModeCCodeIndicator"] :
				tmp = ModeCCodeIndicatorExtractedCAT48()
				self.ModeCCodeIndicator = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+8])
				PointeurWhereAmI += 8
		#Extraction du champ "Height Measured by 3D Radar" 	(2 octets); LSB = 25ft
		if "HeightMeasured3DRad" in FSPECRempli:
			if FSPECRempli["HeightMeasured3DRad"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4],16))[2:].zfill(16)
				if tmp[2]=="1":
					self.HeightMeasured3DRad = ~int(tmp[3:],2) * 25
				else:
					self.HeightMeasured3DRad = int(tmp[3:],2) * 25
				PointeurWhereAmI += 4	
		#Extraction du champ "Radial Doppler Speed" 	(1 octet + 9 octets extension)
		if "RadialDopplerSpeed" in FSPECRempli:
			if FSPECRempli["RadialDopplerSpeed"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				tmp2 = RadialDopplerSpeedExtractedCAT48()
				self.RadialDopplerSpeed = tmp2.DecodDataField(DataBlock[ PointeurWhereAmI:PointeurWhereAmI +2+ 4*int(tmp[0]) +14*int(tmp[1]) ])
				PointeurWhereAmI += 2 + int(tmp[0])*4 + int(tmp[1])*14
		#Extraction du champ "Communications / ACAS Capability and Flight Status" 	(2 octets)
		if "ACASCapability" in FSPECRempli:
			if FSPECRempli["ACASCapability"] :
				tmp = ACASCapabilityExtractedCAT48()
				self.ACASCapability = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Bit Extension
		if "FX3" in FSPECRempli:
			if (FSPECRempli["FX3"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
			
		#Extraction du champ "ACAS Resolution Advisory Report" 	(7 octets); 56-bit message conveying Mode S Comm B message data of BDS Register 3,0
		if "ACASResolution" in FSPECRempli:
			if FSPECRempli["ACASResolution"] :
				self.ACASResolution = DataBlock[PointeurWhereAmI:PointeurWhereAmI+14]
				PointeurWhereAmI += 14
		#Extraction du champ "Mode-1 Code in Octal Representation" 	(1 octet)
		if "Mode1CodeOctal" in FSPECRempli:
			if FSPECRempli["Mode1CodeOctal"] :
				tmp = Mode1CodeOctalExtractedCAT48()
				self.Mode1CodeOctal = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2])
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-2 Code in Octal Representation" 	(2 octets)
		if "Mode2CodeOctal" in FSPECRempli:
			if FSPECRempli["Mode2CodeOctal"] :
				tmp = Mode2CodeOctalExtractedCAT48()
				self.Mode2CodeOctal = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		#Extraction du champ "Mode-1 Code Confidence Indicator" 	(1 octet)
		if "Mode1CodeIndicator" in FSPECRempli:
			if FSPECRempli["Mode1CodeIndicator"] :
				tmp = Mode1CodeIndicatorExtractedCAT48()
				self.Mode1CodeIndicator = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2])
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-2 Code Confidence Indicator" 	(2 octets)
		if "Mode2CodeIndicator" in FSPECRempli:
			if FSPECRempli["Mode2CodeIndicator"] :
				tmp = Mode2CodeIndicatorExtractedCAT48()
				self.Mode2CodeIndicator = tmp.DecodDataField(DataBlock[PointeurWhereAmI:PointeurWhereAmI+4])
				PointeurWhereAmI += 4
		
		##******************** Ces 2 champs ne sont pas documentés *******************************
		##Extraction du champ "Special Purpose Field" 	(1 octet + 1 octet extension)
		#if "SpecialField" in FSPECRempli:
		#	if (FSPECRempli["SpecialField"] ==1):
		#		self.SpecialField = 1
		#		#PointeurWhereAmI += 4
		#		pass
		##Extraction du champ "Reserved Expansion Field" 	(1 octet + 1 octet extension)
		#if "ReservedExpansionField" in FSPECRempli:
		#	if (FSPECRempli["ReservedExpansionField"] ==1):
		#		self.ReservedExpansionField = 1
		#		#PointeurWhereAmI += 4
		#		pass
		##print "FIN DECOD RECORD 48"
		return self, PointeurWhereAmI/2


#******************************** Cat48Record ********************************************************************
#Classe représentant le champ Record d'une trame Cat48
#XByteField = champ d'un octet
#XShortField = champ de 2 octets
#X3BytesField = champ de 3 octets
#XLongField = champ de 4 octets et +
class Cat48Record(Packet):
	name="Record Categorie 48"
	fields_desc = [XLongField("FSPEC", None),				#4 octets max
				   XByteField("SAC", None),					#1 octet
				   XByteField("SIC", None),					#1 octet
				   X3BytesField("TimeDay",None),			#3octets
				   XShortField("TargetReportDesc", None),	#1 octet + 1 extension
				   XLongField("PositionPolar",None),		#4 octets
				   XShortField("ModeACodeInOctal", None),	#2 octets
				   XShortField("FlightLevelBin", None),		#2 octets
				   XLongField("RadarPlotCarac", None),		#1 octets + 7 ext max
				   X3BytesField("AircraftAdr",None),		#3 octets
				   XLongField("AircraftID", None),			#6 octets
				   XLongField("ModeSData",None),			#9 octets
				   XShortField("TrackNbr", None),			#2 octets
				   XLongField("PositionCartesian", None),	#4 octets
				   XLongField("TrackVelocityPolar", None),	#4 octets
				   XShortField("TrackStatus", None),		#2 octets
				   XLongField("TrackQuality", None),		#4 octets
				   XByteField("WarningConditions", None),	#1 octet
				   XShortField("ModeACodeIndicator", None),	#2 octets
				   XLongField("ModeCCodeIndicator", None),	#4 octets
				   XShortField("HeightMeasured3DRad", None),#2 octets
				   XLongField("RadialDopplerSpeed", None),	#1 octet + 9 extensions max
				   XShortField("ACASCapability", None),		#2 octets
				   XLongField("ACASResolution", None),		#7 octets
				   XByteField("Mode1CodeOctal", None),		#1 octet
				   XShortField("Mode2CodeOctal", None),		#2 octets
				   XByteField("Mode1CodeIndicator", None),	#1 octet
				   XShortField("Mode2CodeIndicator", None),	#2 octets
				   XLongField("SpecialField", None),		#1 octet + 1octet +
				   XLongField("ReservedExpansionField", None) #1 octet + 1octet +
				   ]
	
	#********************************************************************************************************** 
	#Fonction qui isole le champ FSPEC du reste des données
	#En Entree : toutes les donnees de la partie DataRecord (str)
	#En Sortie : uniquement le FSPEC (str), et le nombre d'octets (int)
	def IsoleFSPEC(self, DataRecord):
		i=0
		tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(8)
		while ((tmp[-1:])=="1"):
			if ((i+2)>8): # On evite de dépasser la taille maximale du FSPEC = 4 octets
				break
			i+=2
			tmp = bin(int(DataRecord[i:i+2],16))[2:].zfill(len(DataRecord[i:i+2])*4)
		LastBit=(i+2)
		NbOctetFSPEC=(i+2)/2
		return DataRecord[0:LastBit], NbOctetFSPEC
	
	#********************************** RemplirFSPEC *************************************************************** 
	# Cette fonction rempli un dictionnaire associant le nom de l'item et la valeur dans le FSPEC
	# En entrée : le champ FSPEC uniquement, en chaine de caractères, et la catégorie = entier
	# En sortie : une liste de tuple
	def RemplirFSPEC(self, FSPECField):
		FSPEC48listkey = ["DataSRCID", "TimeDay", "TargetReportDesc", "PositionPolar", "ModeACodeInOctal",
						  "FlightLevelBin", "RadarPlotCarac", "FX1", "AircraftAdr", "AircraftID", "ModeSData",
						  "TrackNbr", "PositionCartesian", "TrackVelocityPolar", "TrackStatus", "FX2", "TrackQuality",
						  "WarningConditions", "ModeACodeIndicator", "ModeCCodeIndicator", "HeightMeasured3DRad",
						  "RadialDopplerSpeed", "ACASCapability", "FX3", "ACASResolution", "Mode1CodeOctal",
						  "Mode2CodeOctal", "Mode1CodeIndicator", "Mode2CodeIndicator", "SpecialField",
						  "ReservedExpansionField", "FX4"]
		
		#converion hexa en binaire, avec retrait des caractères 0b en debut de chaine, et remplissage en début de tableau
		FSPEClistval1 = bin(int(FSPECField, 16))[2:].zfill(len(FSPECField)*4)
		FSPEClistval2=[0]*(len(FSPEClistval1))
		#Conversion des caractères en integer
		for i in range(len(FSPEClistval1)):
			FSPEClistval2[i]=int(FSPEClistval1[i],16)
		#zip combine les 2 listes en 1 : [("DataSRCID", 1), ...]
		return dict(zip(FSPEC48listkey,FSPEClistval2))


	
	#************************************ DecodRecord48 ************************************************************
	# Fonction qui décortique le DataRecord d'une trame ASTERIX Cat 48
	# En Entrée : prend le bloc DataRecord en entier car on ne connait pas la longueur du DataRecord
	# En sortie : renvoie le contenu du Record + la longueur du record, FSPEC compris
	def DecodRecord48(self, DataBlock):
		#print "************************************** DECOD RECORD 48 **************************************"
		#FSPEC est un dictionnaire : {"DataSRCID" : 1, ...}
		NbOctetsFSPEC=0
		FSPEC, NbOctetsFSPEC = self.IsoleFSPEC(DataBlock)
		FSPECRempli = self.RemplirFSPEC(FSPEC)
		self.FSPEC = FSPEC
		PointeurWhereAmI = NbOctetsFSPEC*2
		#Extraction du SAC/SIC (2 octets)
		if "DataSRCID" in FSPECRempli:
			if FSPECRempli["DataSRCID"] :
				self.SAC = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				self.SIC = DataBlock[PointeurWhereAmI+2:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction de l'heure du jour (3 octets)
		if FSPECRempli.has_key("TimeDay"):
			if FSPECRempli["TimeDay"] :
				self.TimeDay = DataBlock[PointeurWhereAmI:PointeurWhereAmI+6]
				PointeurWhereAmI += 6
		#Extraction du Target Report Descriptor (1 octet + 1 extension)
		if 	"TargetReportDesc" in FSPECRempli:
			if FSPECRempli["TargetReportDesc"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				self.TargetReportDesc = DataBlock[PointeurWhereAmI : PointeurWhereAmI + 2 * (2**int(tmp[-1:],2))]
				PointeurWhereAmI += 2 * (2**int(tmp[-1:],2))
		#Extraction "Measured Position in Slant Polar Coordinates" (4octets)
		if 	"PositionPolar" in FSPECRempli:
			if FSPECRempli["PositionPolar"] :
				self.PositionPolar = DataBlock[PointeurWhereAmI:PointeurWhereAmI+8]
				PointeurWhereAmI += 8
		#Extraction Mode-3/A Code in Octal Representation (2 octets)
		if "ModeACodeInOctal" in FSPECRempli:
			if FSPECRempli["ModeACodeInOctal"] :
				self.ModeACodeInOctal = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du Flight Level in Binary Representation (2 octets)
		if "FlightLevelBin" in FSPECRempli:
			if FSPECRempli["FlightLevelBin"] :
				self.FlightLevelBin = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction de Radar Plot Characteristics (1 octet + 7 octets extensions au max)
		if "RadarPlotCarac" in FSPECRempli:
			if FSPECRempli["RadarPlotCarac"] :
				tmp= bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				NbSubField=0	# Compte le nombre de subfield de ce Data Item
				if (tmp[-1:]=="1"):
					for i in range(len(tmp)-1):
						if tmp[i]=="1":
							NbSubField += 1
					self.RadarPlotCarac = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+NbSubField*2]
				PointeurWhereAmI += 2 + (NbSubField * 2)
		#Bit Extension
		if "FX1" in FSPECRempli:
			if (FSPECRempli["FX1"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		#Extraction du champ Aircraft Adress  (3 octets)		
		if "AircraftAdr" in FSPECRempli:
			if FSPECRempli["AircraftAdr"] :
				self.AircraftAdr = DataBlock[PointeurWhereAmI:PointeurWhereAmI+6]
				PointeurWhereAmI += 6
		#Extraction du champ Aircraft Identification	(6 octets)
		if "AircraftID" in FSPECRempli:
			if FSPECRempli["AircraftID"] :
				self.AircraftID = DataBlock[PointeurWhereAmI:PointeurWhereAmI+12]
				PointeurWhereAmI += 12
		#Extraction des Data Mode S 	(9 octets)
		if "ModeSData" in FSPECRempli:
			if FSPECRempli["ModeSData"] :
				Rep = int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16)
				self.ModeSData = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2+16*Rep]
				PointeurWhereAmI += 2+ (16*Rep)
		#Extraction du champ Track Number	(2 octets)
		if "TrackNbr" in FSPECRempli:
			if FSPECRempli["TrackNbr"] :
				self.TrackNbr = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du champ "Calculated Position in Cartesian Coordinates"		(4 octets)
		if "PositionCartesian" in FSPECRempli:
			if FSPECRempli["PositionCartesian"] :
				self.PositionCartesian = DataBlock[PointeurWhereAmI:PointeurWhereAmI+8]
				PointeurWhereAmI += 8
		#Extraction du champ "Calculated Track Velocity in Polar Representation" 	(4 octets)
		if "TrackVelocityPolar" in FSPECRempli:
			if FSPECRempli["TrackVelocityPolar"] :
				self.TrackVelocityPolar = DataBlock[PointeurWhereAmI:PointeurWhereAmI+8]
				PointeurWhereAmI += 8
		#Extraction du champ "Track Status"	(1 octet + 1 octet extension)
		if "TrackStatus" in FSPECRempli:
			if FSPECRempli["TrackStatus"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				self.TrackStatus = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2*2**(int(tmp[-1]))]
				PointeurWhereAmI += 2*( 2**int(tmp[-1],2) )
		#Bit Extension
		if "FX2" in FSPECRempli:
			if (FSPECRempli["FX2"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
		
		#Extraction du champ "Track Quality" 	(4 octets)
		if "TrackQuality" in FSPECRempli:
			if FSPECRempli["TrackQuality"] :
				self.TrackQuality = DataBlock[PointeurWhereAmI:PointeurWhereAmI+8]
				PointeurWhereAmI += 8
		#Extraction du champ "Warning/Errors conditions" 	(1 octet)
		if "WarningConditions" in FSPECRempli:
			if FSPECRempli["WarningConditions"] :
				self.WarningConditions = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-3/A Code Confidence Indicator " 	(2 octets)
		if "ModeACodeIndicator" in FSPECRempli:
			if FSPECRempli["ModeACodeIndicator"] :
				self.ModeACodeIndicator = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du champ "Mode-C Code and Confidence Indicator " 	(4 octets)
		if "ModeCCodeIndicator" in FSPECRempli:
			if FSPECRempli["ModeCCodeIndicator"] :
				self.ModeCCodeIndicator = DataBlock[PointeurWhereAmI:PointeurWhereAmI+8]
				PointeurWhereAmI += 8
		#Extraction du champ "Height Measured by 3D Radar" 	(2 octets)
		if "HeightMeasured3DRad" in FSPECRempli:
			if FSPECRempli["HeightMeasured3DRad"] :
				self.HeightMeasured3DRad = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4	
		#Extraction du champ "Radial Doppler Speed" 	(1 octet + 9 octets extension)
		if "RadialDopplerSpeed" in FSPECRempli:
			if FSPECRempli["RadialDopplerSpeed"] :
				tmp = bin(int(DataBlock[PointeurWhereAmI:PointeurWhereAmI+2],16))[2:].zfill(8)
				self.TrackStatus = DataBlock[ PointeurWhereAmI : PointeurWhereAmI + 2 + 4*int(tmp[0]) + 14*int(tmp[1]) ]
				PointeurWhereAmI += 2 + int(tmp[0])*4 + int(tmp[1])*14
		#Extraction du champ "Communications / ACAS Capability and Flight Status" 	(2 octets)
		if "ACASCapability" in FSPECRempli:
			if FSPECRempli["ACASCapability"] :
				self.ACASCapability = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Bit Extension
		if "FX3" in FSPECRempli:
			if (FSPECRempli["FX3"] ==0):  #Le champ extension =0 => on a fini
				return self, PointeurWhereAmI/2
			
		#Extraction du champ "ACAS Resolution Advisory Report" 	(7 octets)
		if "ACASResolution" in FSPECRempli:
			if FSPECRempli["ACASResolution"] :
				self.ACASResolution = DataBlock[PointeurWhereAmI:PointeurWhereAmI+14]
				PointeurWhereAmI += 14
		#Extraction du champ "Mode-1 Code in Octal Representation" 	(1 octet)
		if "Mode1CodeOctal" in FSPECRempli:
			if FSPECRempli["Mode1CodeOctal"] :
				self.Mode1CodeOctal = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-2 Code in Octal Representation" 	(2 octets)
		if "Mode2CodeOctal" in FSPECRempli:
			if FSPECRempli["Mode2CodeOctal"] :
				self.Mode2CodeOctal = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#Extraction du champ "Mode-1 Code Confidence Indicator" 	(1 octet)
		if "Mode1CodeIndicator" in FSPECRempli:
			if FSPECRempli["Mode1CodeIndicator"] :
				self.Mode1CodeIndicator = DataBlock[PointeurWhereAmI:PointeurWhereAmI+2]
				PointeurWhereAmI += 2
		#Extraction du champ "Mode-2 Code Confidence Indicator" 	(2 octets)
		if "Mode2CodeIndicator" in FSPECRempli:
			if FSPECRempli["Mode2CodeIndicator"] :
				self.Mode2CodeIndicator = DataBlock[PointeurWhereAmI:PointeurWhereAmI+4]
				PointeurWhereAmI += 4
		#******************** Ces 2 champs ne sont pas documentés *******************************
		#Extraction du champ "Special Purpose Field" 	(1 octet + 1 octet extension)
		if "SpecialField" in FSPECRempli:
			if FSPECRempli["SpecialField"]:
				self.SpecialField = 1
				#PointeurWhereAmI += 4
				pass
		#Extraction du champ "Reserved Expansion Field" 	(1 octet + 1 octet extension)
		if "ReservedExpansionField" in FSPECRempli:
			if FSPECRempli["ReservedExpansionField"]:
				self.ReservedExpansionField = 1
				#PointeurWhereAmI += 4
				pass
		#print "FIN DECOD RECORD 48"
		return self, PointeurWhereAmI/2


#***************************** TrameAsterix3448 ********************************************************************
class TrameAsterix3448(Packet):
	name="Trame ASTERIX 34 48"
	fields_desc = [StrField("Radar", None),
				   IntField("Len", None),	# Longueur de la trame ASTERIX
				   IntField("Nbr_Record34",0),
				   IntField("Nbr_Record48",0),
				   #PacketListField("Record34",None, Cat34Record),
				   #PacketListField("Record48",None, Cat48Record),
				   PacketListField("Record34Detail",None, ExtractDetailRecord34),
				   PacketListField("Record48Detail",None, ExtractDetailRecord48),
				   ]

	#***************************** RadarExpediteur *****************************************************************
	#Fonction qui détermine quel radar a envoyé la trame
	def RadarExpediteur(self, AdrDst):
		for key in RADAR_ModeS:
			if key==(AdrDst):
				return RADAR_ModeS[key]

	#********************************** AnalyseTrameAsterix ******************************************************* 
	#Fonction qui analyse une trame Asterix
	#En Entrée : prend une trame ASTERIX en entier
	#En sortie : on récupère les informations de la trame : le radar de provenance, la longueur de la trame, et les
	#			infos de chaque "Record" de chaque catégorie (34 et 48)
	def AnalyseTrameAsterix(self, TrameBrute):
		AdrDst = TrameBrute.dst
		RadarOK = self.RadarExpediteur(AdrDst)
		LongueurTrameAsterix=0
		MyRecord34 = []
		MyRecord48 = []
		MyRecord34Detail = []
		MyRecord48Detail = []
		if (RadarOK !=None):
			# Si la trame recue provient d'un radar Mode S connu.		
			# Longueur totale de la trame recue, en dehors de l'en-tete (AdrMACDst, AdrMACSrc, Len)
			LongueurTrameAsterix = int(float.fromhex(hex(TrameBrute.len)))
			# On détermine si la trame est une trame ASTERIX ou pas
			if (int(float.fromhex(hex(TrameBrute.ctrl)))==3):
				#RawData = 3 octets LLC + Asterix DataBlock
				#hexlify converti les RawData en chaine de caracteres
				#DataBlock = (Cat, Len, Record-1, Record-2....Record-N)
				DataBlock = hexlify(TrameBrute.load)
				LongueurDataBlock = 0
				PointeurWhereAmIInRawData = 0 #Le pointeur pointe sur le 1ier bit du DataBlock (Cat)
				while (PointeurWhereAmIInRawData < ((LongueurTrameAsterix*2)-6)):
					#Determiner la categorie
					#print "----------------------------------- DATA BLOCK -----------------------------------"
					PointeurWhereAmIInDataBlock = 0 		#Le pointeur pointe sur le 1ier bit du DataBlock
					Cat = int(DataBlock[PointeurWhereAmIInRawData : PointeurWhereAmIInRawData+2],16)
					LongueurDataBlock = int(DataBlock[PointeurWhereAmIInRawData+2 : PointeurWhereAmIInRawData+6],16)
					PointeurWhereAmIInDataBlock += 6		# Pointe sur le 1ie bit du 1ier Record du DataBlock
					PointeurWhereAmIInRawData += PointeurWhereAmIInDataBlock
					if (Cat==CAT48):
						#print "Cat = 48"
						tmp = Cat48Record()
						while (PointeurWhereAmIInDataBlock < (LongueurDataBlock*2)):
							tmpDetail = ExtractDetailRecord48()
							tmp, LongueurRecord = tmp.DecodRecord48(DataBlock[PointeurWhereAmIInRawData:])
							tmpDetail, toto = tmpDetail.DecodRecord48Detail(DataBlock[PointeurWhereAmIInRawData:])
							MyRecord48Detail.append(tmpDetail)
							MyRecord48.append(tmp)					# On stocke le résultat dans une liste
							PointeurWhereAmIInDataBlock += LongueurRecord*2
							PointeurWhereAmIInRawData += LongueurRecord*2
					elif (Cat==CAT34):
						#print "Cat = 34"
						tmp = Cat34Record()
						while (PointeurWhereAmIInDataBlock < (LongueurDataBlock*2)):
							tmpDetail = ExtractDetailRecord34()
							tmp, LongueurRecord = tmp.DecodRecord34(DataBlock[PointeurWhereAmIInRawData:])
							tmpDetail, toto = tmpDetail.DecodRecord34Detail(DataBlock[PointeurWhereAmIInRawData:])
							MyRecord34.append(tmp)					# On stocke le résultat dans une liste
							MyRecord34Detail.append(tmpDetail)
							PointeurWhereAmIInDataBlock += LongueurRecord*2
							PointeurWhereAmIInRawData += LongueurRecord*2
		#Mise a jour des infos récoltées
		self.Radar = RadarOK
		self.Len = LongueurTrameAsterix
		self.Record34 = MyRecord34
		self.Record48 = MyRecord48
		self.Record34Detail = MyRecord34Detail
		self.Record48Detail = MyRecord48Detail
		self.Nbr_Record34 = len(MyRecord34)
		self.Nbr_Record48 = len(MyRecord48)
		
		return 	self

# Lecture des trames dans un fichier. Retourne les trames lues.
def LectTrames(Trame_a_analyser):
		
	#Si N=0, lecture du fichier en integralite
	#Si offline=None; Sniff le reseau
	#Si offline="nom d'un fichier"; lecture dans le fichier

	N=2
	try:
		#Lire N trames dans le fichier dump
		pkts = sniff(count=N, offline=Trame_a_analyser)
		#print "dans Anatrames.py; Def LecTrames\n"
		#print "pkts = ", pkts
		
	except ValueError:
		print "Erreur du Sniffeur"
	return pkts

#Analyse les trames recues. En extrait les infos.
def MainAppAnaTrames(trameAAnalyser):
	
	maTrame = TrameAsterix3448()
	#print "Dans AnaTrames.py; def MainAppAnaTrames\n"
	#print "trameAAnalyser = ", trameAAnalyser, "\n"
	#print "len(trameAAnalyser) = ", len(trameAAnalyser), "\n"
	
	for i in range(len(trameAAnalyser)):
		#print "################ Trame = %d  ################" %i
		#print "i = ", i, "\n"
		#print "trameAAnalyser[i] = ", trameAAnalyser[i], "\n"

		maTrame = maTrame.AnalyseTrameAsterix(trameAAnalyser[i])

		#print"maTrame.Nbr_Record34 = ",maTrame.Nbr_Record34,"\n"
		#print"maTrame.Nbr_Record48 = ",maTrame.Nbr_Record48,"\n"
		#print"maTrame.radar = ", maTrame.Radar,"\n"
		#if maTrame.Radar !=None:
		#	maTrame.show()
		#maTrame.show()
			#pass
		#if (maTrame.Record34 or maTrame.Record48):
		#	cpt+=1

	#print "Nbr de trames ASTERIX CAT 34 et/ou 48 = ", cpt
	#print "cpt = %d", cpt
	
	#Verification du temps d'exécution pour analyser N trames
	#fin=datetime.datetime.now()
	#print "time total = %s \n" %(fin-debut)
	
	return maTrame
	

#**************************************** MAIN ****************************************************************
if __name__ == '__main__':

	import sys, os

	#####  Redirection des sorties pour debuggage
	os.remove("stdout.log")
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')
	
	#Trame_a_analyser = "TestConfiguration"
	#Trame_a_analyser = "capturePING"
	#Trame_a_analyser = "captures SIRSUR"
	Trame_a_analyser = None
	#Trame_a_analyser = "../Captures Reseaux/RAPN_HS"

	
	MainAppAnaTrames(LectTrames(Trame_a_analyser))
	print "FIN ANATRAMES"
	############ Retablissement des sorties
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__

