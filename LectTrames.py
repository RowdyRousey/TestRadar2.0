#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Lecture des trames 
#######################################################
from scapy.all import *
import wx
import socket

PACKET_LENGTH = 2048

def Sniff_Reseau(where_to_sniff=None, N=1):
	###########		This method is used to read data in a file
	
	#where_to_sniff = None ; Sniff le reseau
	#where_to_sniff = "nom dun fichier" ; Lecture dans le fichier
	
	try:
		#Lire N trames
		pkts=None
		print"Dans la fonction Sniff_Reseau du fichier LectTrames.py\n"
		print"where_to_sniff = ",where_to_sniff, "        N = ",N, "      pkts = ", pkts
		try:
			print "Dans le TRY de LectTrames.py et Sniff_Reseau\n"
			pkts = sniff(count=N, offline=where_to_sniff)
			print"PKTS = ",pkts,"\n"
		except:
			print "ERROR SNIFF\n"
		print"Apres le SNIFF de la fonction Sniff_Reseau du fichier LectTrames.py\n"
	except ValueError:
		print "Erreur du Sniffeur"
	return pkts
		

def Sniff_Reseau_Win():
	###########    this method works only for Windows OS
	
	HOST = socket.gethostbyname(socket.gethostname())
	try:
		mysocket = socket.socket(socket.AF_INET, socket.SOCK_RAW)
		#mysocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
	except socket.error as msg:
		print"ERROR creation Socket = ", msg,"\n"
	
	mysocket.bind((HOST, 0))

	# Include IP headers
	#mysocket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	
	# receive all packages
	mysocket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	
	# receive a package
	data=mysocket.recvfrom(PACKET_LENGTH)
	
	# disabled promiscuous mode
	mysocket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
	
	mysocket.close()
	return data	
		
#**************************************** MAIN ****************************************************************
if __name__ == '__main__':

	import sys, time, os
	
	#####  Redirection des sorties pour debuggage	
	os.remove("stdout.log")
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')

	print"\n-----------------MON MAIN------------------"
	print time.strftime("%d/%m/%Y  %H:%M:%S")
	
	#Trame_a_analyser = "TestConfiguration"
	Trame_a_analyser = "capturePING"
	#Trame_a_analyser = "captures SIRSUR"
	#Trame_a_analyser = "../Captures Reseaux/RAPN_HS"
	#Trame_a_analyser = None
	
	#Nombre de paquet à sniffer
	N=3
	
	############## Test des fonctions définies plus haut
	if Trame_a_analyser==None:
		print "DATA sniffed = ",Sniff_Reseau_Win(),"\n"
	else:
		data=Sniff_Reseau(Trame_a_analyser,N)
		data.show()
		print "\nDATA = ", data,"\n"
	print"FIN SNIFF\n"

	print"---------------- FIN DU PROGRAMME --------------------\n"

	############ Retablissement des sorties
	#sys.stdout = sys.__stdout__
	#sys.stderr = sys.__stderr__
	
	