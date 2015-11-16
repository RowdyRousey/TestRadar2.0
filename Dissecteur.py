#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# 
#######################################################
from time import *
from scapy.all import *

packetCount = 0  
def Dissection(packet):
    Enreg = str(packet.getlayer(Raw).load)
    for compteur in range(0,len(Enreg)):
      ClassAsterix = ord(Enreg[compteur])
    
      if ClassAsterix == 48:
            LongueurBloc = ord(Enreg[1])*256+ord(Enreg[2])
            SAC=ord(Enreg[6])
            SIC=ord(Enreg[7])
            NbSecondes = round((ord(Enreg[8])*65536+ord(Enreg[9])*256+ord(Enreg[10]))/128)
            Time = strftime('%Hh:%Mmin:%Ssec', gmtime(NbSecondes))
            
            Report = bin(ord(Enreg[11]))[2:]

            
            TYP =Report[0:3]
            SIM = Report[3]
            RDP = Report[4]
            SPI = Report[5]
            RAB = Report[6]
            FX = Report[7]
            RhoPosition = round((ord(Enreg[12])*256+ord(Enreg[13]))/256)
            ThetaPosition = round((ord(Enreg[14])*256+ord(Enreg[15]))*360/pow(2,16))

            #Partie Mode A a faire octet 16 et 17
            # Partie FL a faire octet 18 et 19
            # Octet 20 et 21 et 22 à faire
           
            AircraftAddr = hex(ord(Enreg[23]))[2:]+hex(ord(Enreg[24]))[2:]+hex(ord(Enreg[25]))[2:]
            
            '''
            AirCraftId_ = bin(ord(Enreg[26]))[2:]
            Aircraft=""
            for item in (bin(ord(Enreg[26]))[2:],bin(ord(Enreg[27]))[2:],bin(ord(Enreg[28]))[2:],bin(ord(Enreg[29]))[2:],bin(ord(Enreg[30]))[2:],bin(ord(Enreg[31]))[2:]):
              for i in range(0,8-len(item)):
                item="0"+item
              Aircraft=Aircraft+item
            for j in range(0,8):
              A=Aircraft[j*6:(j+1)*6]
              print int(A,2)
            '''
            
            TrackNumber = ord(Enreg[32])*256+ord(Enreg[33])
            
            XPos = (ord(Enreg[34])*256+ord(Enreg[35]))/128 #en NM
            YPos = (ord(Enreg[36])*256+ord(Enreg[37]))/128
            
            CalculatedGroundSpeed = (ord(Enreg[38])*256+ord(Enreg[39]))*0.22 #en kt
            CalculatedHeading = (ord(Enreg[40])*256+ord(Enreg[41]))*0.0055  #en degres
            
            #StatusMonoradarTrack octet 42
            #CapabilityFlightStatus octet 43 et 44
      
    if ClassAsterix == 34:
          print  "toot"
        
 
      
