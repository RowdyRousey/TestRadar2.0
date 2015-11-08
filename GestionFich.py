#!/usr/bin/env python
#-*- coding:utf-8 -*-"

#######################################################
# Projet TERAMOSS
# Initiated by : Tuan DANG
# Followed by : Clovis HAMEL
# 2011-2015 CRNA/N
# Gestion des fichiers 
#######################################################

import ConfigParser
import io

class GestionFichier():
  
    
  ###########################################################
  # Ecrire_Fichier
  # Role : Ecrire des données dans un fichier
  # Entree : Le chemin d'un fichier
  #          Des données à écrire
  #          Opt : Un mode d'ouverture, ajout par défaut
  # Sortie : IOError : Pb d'ouverture
  #          ValueError : Les données ne sont pas stringable
  ###########################################################
  def Ecrire_Fichier(MonFichier, MesDonnees, ModeOuv='a'):
    try:
      Fic = open(MonFichier, ModeOuv)
    except IOError,e:
      print "Erreur d'ouverture du fichier ", MonFichier,e,"\n"
    except ValueError,e:
      print "Les données à ecrire ne sont pas castables en string : ", MonFichier,e,"\n"
    else:
      Fic.write(str(MesDonnees)+"\n")
      Fic.close()
        
  ###########################################################
  # Lire_Fichier
  # Role : Lire les données dans un fichier
  # Entree : Le chemin d'un fichier
  # Sortie : Les données lues
  #          IOError : Pb d'ouverture
  ###########################################################
  def Lire_Fichier(Mon_fichier):
    try:
      Fic = open(Mon_fichier, 'r')
    except IOError,e:
      print "Erreur d'ouverture du fichier ", Mon_fichier,e,"\n"
    else:
      contenu = Fic.read()
      Fic.close()
      return contenu
  
  def ChargerPreferences(self,NomFichierConfig,Obj,Cle):
    cfg = ConfigParser.ConfigParser() # Appel du parser
    cfg.read(NomFichierConfig) # Lecture du fichier config
    if cfg.has_section("Preferences"):
      for i in range(0,len(Cle)):
        Obj[i].SetValue(str(cfg.get("Preferences",Cle[i])))
    else:
      EcrireLog(FILE(),LINE(),"La section Preferences n'est pas présente dans "+NomFichierConfig)
  
  def ConfigSectionMap(Config,section):
      Config = ConfigParser.ConfigParser()
      dict1 = {}
      options = Config.options(section)
      for option in options:
          try:
              dict1[option] = Config.get(section, option)
              if dict1[option] == -1:
                  DebugPrint("skip: %s" % option)
          except:
              print("exception on %s!" % option)
              dict1[option] = None
      return dict1
#**************************************** MAIN ****************************************************************

if __name__ == '__main__':

    import os, sys

    app = GestionFichier(redirect = True, filename = 'stdout.log')
##    app.Lire_Fichier_Conf()
##    print "GestionFichier"
    #Fichier_Conf = "TestConfiguration"
    #Fichier_Conf = "../Captures Reseaux/capturePING"
    #Fichier_Log = "Historique.log"

    #os.remove("stdout.log")
    sys.stdout = open("stdout.log", 'a')
    sys.stderr = open("stdout.log", 'a')
    
    #Ecrire_Fichier(Fichier_Log,"Mon message\n",'a')
    #print"Contenu Fichier Lu = \n",Lire_Fichier("Configuration")
    #Ecrire_Fichier(Fichier_Log, "AAAAAAAAAAAAAAAAA22")
    #print "Fichier lu = ", Lire_Fichier(Fichier_Log), "\n"
    

    #a=hexdump(Lire_Fichier(Fichier_Conf, 'rb'))
    #pkts=rdpcap(Fichier_Conf)
    #print pkts
    #print "OK2"
    #pac.pdfdump("mypdfdump")
    #try:
    #
    #    pkts=rdpcap(Fichier_Conf)
    #    print pkts.hexdump()
    #    print "OK2"
    ##    file_conf = open(Fichier_Conf, 'a')
    ##    file_conf.write("Hello machin bidule chouette\n")
    ##    file_conf.close()
    ##    print "Ouverture du fichier ", Fichier_Conf, " ok"
    #except ValueError:
    ##    print "Erreur d'ouverture du fichier ", Fichier_Conf
    #    print "Erreur rdpcap"
    #    
        
    #sys.stdout = sys.__stdout__
    #sys.stderr = sys.__stderr__