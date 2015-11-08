#! /usr/bin/python
# -*- coding: utf-8 -*-

from Header import * 
from datetime import *

####################################################
# DateCourante
# Rôle : Retourne l'horodatage courant
# Entrée : Rien
# Sortie : (Jour,Mois,Année,Heure,Minutes,Secondes)
####################################################
def DateCourante():
    import time
    horodatage=time.strftime("%d %m %Y %H %M %S")
    Horo_ = horodatage.split(" ")
    return (Horo_[0],Horo_[1],Horo_[2],Horo_[3],Horo_[4],Horo_[5])

####################################################################################
# Horodater
# Rôle : Retourne une chaine de caractère comportant l'horodatage courant
# Entrée : Rien
# Sortie : Jour-Mois-Année Heure-Minutes-Secondes
####################################################################################
def Horodater():
    Horodatage=DateCourante()
    return str(Horodatage[0])+"-"+str(Horodatage[1])+"-"+str(Horodatage[2])+" "+str(Horodatage[3])+":"+str(Horodatage[4])+":"+str(Horodatage[5])

####################################################################################
# DateBNF
# Rôle : Retourne une date au format BNF
# Entrée : Rien
# Sortie : La date au format BNF
####################################################################################
def DateBNF(date_format_bnf):
	return (date_format_bnf[4:6],date_format_bnf[2:4],date_format_bnf[0:2])
  
####################################################################################
# DateNumeroJourAnnee
# Rôle : Donne la date d=[j,m,a] qui est le nième jour de l'année a
# Entrée : n et a 
# Sortie : La date d=[j,m,a]
#################################################################################### 
def DateNumeroJourAnnee(n,a):
  """Donne la date d=[j,m,a] qui est le nième jour de l'année a"""
  if ((a%4==0 and a%100!=0) or a%400==0):  # bissextile?
    jm = (0,31,60,91,121,152,182,213,244,274,305,335,366)
  else:
    jm = (0,31,59,90,120,151,181,212,243,273,304,334,365)
  for m in range(1,13):
    if jm[m]>=n:
      return [n-jm[m-1], m, a]

####################################################################################
# ExtraireDate
# Rôle : Extrait la date du fichier contenu dans l'en-tête
# Entrée : Un buffer de données 
# Sortie : [Jour,Mois,Année]
####################################################################################
def ExtraireDate(Donnees):
  # Extraction de l'en-tête du fichier
  EnTeteFichier = Donnees[0:LONG_HEAD_BUFFER] 
  Annee = 1900 + ord(EnTeteFichier[1:2])
  Jour = ord(EnTeteFichier[2:3])*256+ord(EnTeteFichier[3:4])
      
  [Day,Month,Year]=DateNumeroJourAnnee(Jour,Annee)
  if Day<9:
    Day = '0'+str(Day)
    if Month<9:
      Month = '0'+str(Month)
  return [Day,Month,Year]

####################################################################################
# CalculDateCA
# Rôle : Calcule la date de la CA
# Entrée : Actuel, Ancien ou Futur
# Sortie : [Jour,Mois,Année]
####################################################################################
def CalculDateCA(when):
  if when=="actuel":
    Date = CalculDateCAActuel()
    return (Date.day,Date.month,Date.year)
  elif when == "ancien":
    Date = CalculDateCAAncien()
    return (Date.day,Date.month,Date.year)
  elif when == "futur":
    Date = CalculDateCAFutur()
    return (Date.day,Date.month,Date.year)
  else :
    print ""
    #Gerer le cas d'erreur

####################################################################################
# CalculDateCAXXXX
# Rôle : Fonctions d'appui au calcul de la CA
# Entrée : Rien
# Sortie : Un objet Date
####################################################################################
def CalculDateCAActuel(): 
  maintenant = datetime.now()
  CaReference=datetime(2015, 8, 20)
  DiffTodayCA=maintenant-CaReference
  CAActuelle=maintenant-timedelta(days=abs(DiffTodayCA.days)%28)
  return CAActuelle
def CalculDateCAAncien(): 
  return CalculDateCAActuel()-timedelta(days=28)
def CalculDateCAFutur(): 
  return CalculDateCAActuel()+timedelta(days=28)
  

