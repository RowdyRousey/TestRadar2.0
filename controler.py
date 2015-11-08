#!/usr/bin/env python
#-*- coding:utf-8 -*-"
#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Controler
#######################################################

import sys
#from scapy.all import *



#**************************************** MAIN ****************************************************************

if __name__ == '__main__':
	
	sys.stdout = open("stdout.log", 'a')
	sys.stderr = open("stdout.log", 'a')
	
	
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__