#!/usr/bin/env python
#-*- coding:utf-8 -*-"

#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Journalisation des erreurs
#######################################################

import datetime
import os
import inspect 

# ###############################################################
# EcrireLog
# Ecriture de message dans un fichier quotidien de journalisation
# En entr�e : Le fichier concern� par le message
#             La ligne concern�e dans le fichier
#             Le message � �crire
# En sortie : Rien
# ###############################################################

def EcrireLog(Fichier,Ligne,MessageJournalisation):
  PATH_LOG=".\Log\\"
  Horodatage = DateCourante()
  
  if not (os.path.exists(PATH_LOG)):    
    os.mkdir(PATH_LOG)
    
  NomFichier = PATH_LOG+str(Horodatage[2])+str(Horodatage[1])+str(Horodatage[0])+".log"
  MessageJournalisation2=str(Horodatage[3])+':'+str(Horodatage[4])+':'+str(Horodatage[5])+" - File : "+str(Fichier)+" - Ligne : "+str(Ligne)+" - "+str(MessageJournalisation)+"\n";
 
  try:
    FIC = open(NomFichier, "a")
  except IOError,e:
    print "Erreur d'ouverture du fichier ", NomFichier,e,"\n"
  else:
    FIC.write(MessageJournalisation2)
    FIC.close()
    ERROR = 1

# ###############################################################
# LINE
# Renvoie la ligne du fichier lors de l'appel de fonction
# ###############################################################
def LINE():
    return inspect.currentframe().f_back.f_lineno

# ###############################################################
# FILE
# Renvoie le nom complet du fichier lors de l'appel de fonction
# ###############################################################
def FILE():
    return os.path.basename(inspect.currentframe().f_back.f_code.co_filename)

####################################################
# DateCourante
# R�le : Retourne l'horodatage courant
# Entr�e : Rien
# Sortie : (Jour,Mois,Ann�e,Heure,Minutes,Secondes)
####################################################
def DateCourante():
    import time
    horodatage=time.strftime("%d %m %Y %H %M %S")
    Horo_ = horodatage.split(" ")
    return (Horo_[0],Horo_[1],Horo_[2],Horo_[3],Horo_[4],Horo_[5])
