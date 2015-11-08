# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate
import wx.html
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.Point( -1,-1 ), size = wx.Size( 1280,1024 ), style = wx.MAXIMIZE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( 1280,1024 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 1280,1024 ) ) 
		self.m_panelMenuBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,1024 ), wx.TAB_TRAVERSAL )
		self.m_panelMenuBar.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		fgSizerMenuBar = wx.FlexGridSizer( 1, 9, 0, 0 )
		fgSizerMenuBar.AddGrowableCol( 3 )
		fgSizerMenuBar.SetFlexibleDirection( wx.BOTH )
		fgSizerMenuBar.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bpQuitApp = wx.BitmapButton( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/quit 2 icon 40x40.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW )
		fgSizerMenuBar.Add( self.m_bpQuitApp, 0, wx.ALIGN_CENTER|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, u"HEURE PC : ", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizerMenuBar.Add( self.m_staticHeurePC, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.AffichHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), 0 )
		self.AffichHeurePC.Wrap( 1 )
		self.AffichHeurePC.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.AffichHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		fgSizerMenuBar.Add( self.AffichHeurePC, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP, 5 )
		
		self.LogoTestRadar = wx.StaticBitmap( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/Logo Test Radar V2.0.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerMenuBar.Add( self.LogoTestRadar, 0, wx.ALIGN_CENTER|wx.ALL, 0 )
		
		self.Signal_Vie = wx.animate.AnimationCtrl( self.m_panelMenuBar, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.Size( -1,-1 ), wx.animate.AC_DEFAULT_STYLE )
		self.Signal_Vie.LoadFile( u"C:\\TERAMOSS\\Images\\ecg-63x45.gif" )
		fgSizerMenuBar.Add( self.Signal_Vie, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 2 )
		
		self.m_bpCoupureRadar = wx.BitmapButton( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/compatibilités coupures radars Icon.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpCoupureRadar.SetToolTipString( u"Incompatibilité des coupures radars" )
		
		fgSizerMenuBar.Add( self.m_bpCoupureRadar, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 2 )
		
		self.m_bpHisto = wx.BitmapButton( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/Histo icone 40x40.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpHisto.SetToolTipString( u"Historique" )
		
		fgSizerMenuBar.Add( self.m_bpHisto, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.m_bpFavorite = wx.BitmapButton( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/engrenage bleue 40x40.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpFavorite.SetToolTipString( u"Préférences de l'application" )
		
		fgSizerMenuBar.Add( self.m_bpFavorite, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.m_bpButtonHelp = wx.BitmapButton( self.m_panelMenuBar, wx.ID_ANY, wx.Bitmap( u"Images/Help icon 40x40.jpg", wx.BITMAP_TYPE_ANY ), wx.Point( -1,-1 ), wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_bpButtonHelp.SetToolTipString( u"Aide" )
		
		fgSizerMenuBar.Add( self.m_bpButtonHelp, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT, 2 )
		
		
		self.m_panelMenuBar.SetSizer( fgSizerMenuBar )
		self.m_panelMenuBar.Layout()
		bSizer1.Add( self.m_panelMenuBar, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel109 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel109.SetMaxSize( wx.Size( 1280,-1 ) )
		
		fgSizer127 = wx.FlexGridSizer( 1, 6, 0, 0 )
		fgSizer127.AddGrowableCol( 1 )
		fgSizer127.AddGrowableCol( 2 )
		fgSizer127.AddGrowableCol( 3 )
		fgSizer127.AddGrowableCol( 4 )
		fgSizer127.AddGrowableCol( 5 )
		fgSizer127.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer127.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText82 = wx.StaticText( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText82.Wrap( -1 )
		bSizer8.Add( self.m_staticText82, 1, wx.ALL|wx.EXPAND, 1 )
		
		self.m_staticText117 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"MODE S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )
		self.m_staticText117.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer8.Add( self.m_staticText117, 2, wx.ALIGN_CENTER|wx.SHAPED|wx.EXPAND, 0 )
		
		
		fgSizer127.Add( bSizer8, 0, wx.EXPAND, 0 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1091 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491.AddGrowableRow( 0 )
		fgSizer11491.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAAV_RadarRotatif = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491.Add( self.RAAV_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491.Wrap( -1 )
		self.m_staticText20491.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491.Add( self.m_staticText20491, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591.Wrap( -1 )
		self.m_staticText20591.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491.Add( self.m_staticText20591, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAAV_S_PeriodeRotation = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAAV_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RAAV_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491.Add( self.RAAV_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAAV_S_NbPlotsTour = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAAV_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RAAV_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491.Add( self.RAAV_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAAV_S_VoiePal = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAAV_S_VoiePal.SetMaxLength( 0 ) 
		self.RAAV_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491.Add( self.RAAV_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091.Add( fgSizer11491, 1, wx.EXPAND, 1 )
		
		self.RAAV_PanelS = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAAV_S_Info1 = wx.StaticText( self.RAAV_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAAV_S_Info1.Wrap( -1 )
		bSizer20101.Add( self.RAAV_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAAV_S_Info2 = wx.StaticText( self.RAAV_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAAV_S_Info2.Wrap( -1 )
		bSizer20101.Add( self.RAAV_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAAV_PanelS.SetSizer( bSizer20101 )
		self.RAAV_PanelS.Layout()
		bSizer20101.Fit( self.RAAV_PanelS )
		bSizer1091.Add( self.RAAV_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar01 = wx.Button( self.m_panel109, wx.ID_ANY, u"AVRANCHES", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar01.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar01.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar01.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer1091.Add( self.ButtonOpenStat_radar01, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer1091, 1, wx.EXPAND, 5 )
		
		bSizer10911 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer114911 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer114911.AddGrowableRow( 0 )
		fgSizer114911.SetFlexibleDirection( wx.VERTICAL )
		fgSizer114911.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RANE_RadarRotatif = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,60 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer114911.Add( self.RANE_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText204911 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText204911.Wrap( -1 )
		self.m_staticText204911.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText204911.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer114911.Add( self.m_staticText204911, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText205911 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText205911.Wrap( -1 )
		self.m_staticText205911.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText205911.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer114911.Add( self.m_staticText205911, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RANE_S_PeriodeRotation = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RANE_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RANE_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer114911.Add( self.RANE_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RANE_S_NbPlotsTour = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RANE_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RANE_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer114911.Add( self.RANE_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RANE_S_VoiePal = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RANE_S_VoiePal.SetMaxLength( 0 ) 
		self.RANE_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer114911.Add( self.RANE_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer10911.Add( fgSizer114911, 1, wx.EXPAND, 1 )
		
		self.RANE_PanelS = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer201011 = wx.BoxSizer( wx.VERTICAL )
		
		self.RANE_S_Info1 = wx.StaticText( self.RANE_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RANE_S_Info1.Wrap( -1 )
		bSizer201011.Add( self.RANE_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RANE_S_Info2 = wx.StaticText( self.RANE_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RANE_S_Info2.Wrap( -1 )
		bSizer201011.Add( self.RANE_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RANE_PanelS.SetSizer( bSizer201011 )
		self.RANE_PanelS.Layout()
		bSizer201011.Fit( self.RANE_PanelS )
		bSizer10911.Add( self.RANE_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar02 = wx.Button( self.m_panel109, wx.ID_ANY, u"NEVERS", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar02.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar02.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar02.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer10911.Add( self.ButtonOpenStat_radar02, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer10911, 1, wx.EXPAND, 5 )
		
		bSizer109111 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149111 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149111.AddGrowableRow( 0 )
		fgSizer1149111.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAPS_RadarRotatif = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149111.Add( self.RAPS_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049111 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049111.Wrap( -1 )
		self.m_staticText2049111.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049111.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149111.Add( self.m_staticText2049111, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059111 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059111.Wrap( -1 )
		self.m_staticText2059111.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059111.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149111.Add( self.m_staticText2059111, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAPS_S_PeriodeRotation = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPS_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RAPS_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149111.Add( self.RAPS_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPS_S_NbPlotsTour = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPS_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RAPS_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149111.Add( self.RAPS_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPS_S_VoiePal = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPS_S_VoiePal.SetMaxLength( 0 ) 
		self.RAPS_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149111.Add( self.RAPS_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109111.Add( fgSizer1149111, 1, wx.EXPAND, 1 )
		
		self.RAPS_PanelS = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010111 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAPS_S_Info1 = wx.StaticText( self.RAPS_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPS_S_Info1.Wrap( -1 )
		bSizer2010111.Add( self.RAPS_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAPS_S_Info2 = wx.StaticText( self.RAPS_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPS_S_Info2.Wrap( -1 )
		bSizer2010111.Add( self.RAPS_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAPS_PanelS.SetSizer( bSizer2010111 )
		self.RAPS_PanelS.Layout()
		bSizer2010111.Fit( self.RAPS_PanelS )
		bSizer109111.Add( self.RAPS_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar03 = wx.Button( self.m_panel109, wx.ID_ANY, u"PALAISEAU", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar03.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar03.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar03.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109111.Add( self.ButtonOpenStat_radar03, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer109111, 1, wx.EXPAND, 5 )
		
		bSizer109112 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149112 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149112.AddGrowableRow( 0 )
		fgSizer1149112.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RATR_RadarRotatif = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.Size( 60,60 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.RATR_RadarRotatif.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149112.Add( self.RATR_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049112 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049112.Wrap( -1 )
		self.m_staticText2049112.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049112.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149112.Add( self.m_staticText2049112, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059112 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059112.Wrap( -1 )
		self.m_staticText2059112.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059112.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149112.Add( self.m_staticText2059112, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RATR_S_PeriodeRotation = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RATR_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RATR_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149112.Add( self.RATR_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RATR_S_NbPlotsTour = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RATR_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RATR_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149112.Add( self.RATR_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RATR_S_VoiePal = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RATR_S_VoiePal.SetMaxLength( 0 ) 
		self.RATR_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149112.Add( self.RATR_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109112.Add( fgSizer1149112, 1, wx.EXPAND, 1 )
		
		self.RATR_PanelS = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010112 = wx.BoxSizer( wx.VERTICAL )
		
		self.RATR_S_Info1 = wx.StaticText( self.RATR_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RATR_S_Info1.Wrap( -1 )
		bSizer2010112.Add( self.RATR_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RATR_S_Info2 = wx.StaticText( self.RATR_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RATR_S_Info2.Wrap( -1 )
		bSizer2010112.Add( self.RATR_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RATR_PanelS.SetSizer( bSizer2010112 )
		self.RATR_PanelS.Layout()
		bSizer2010112.Fit( self.RATR_PanelS )
		bSizer109112.Add( self.RATR_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar04 = wx.Button( self.m_panel109, wx.ID_ANY, u"TOURS", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar04.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar04.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar04.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109112.Add( self.ButtonOpenStat_radar04, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer109112, 1, wx.EXPAND, 5 )
		
		bSizer109113 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149113 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149113.AddGrowableRow( 0 )
		fgSizer1149113.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149113.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RACH_RadarRotatif = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149113.Add( self.RACH_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049113 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"Nb Pistes\npar tour", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049113.Wrap( -1 )
		self.m_staticText2049113.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049113.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149113.Add( self.m_staticText2049113, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059113 = wx.StaticText( self.m_panel109, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059113.Wrap( -1 )
		self.m_staticText2059113.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059113.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149113.Add( self.m_staticText2059113, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RACH_S_PeriodeRotation = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACH_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RACH_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149113.Add( self.RACH_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACH_S_NbPlotsTour = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACH_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RACH_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149113.Add( self.RACH_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACH_S_VoiePal = wx.TextCtrl( self.m_panel109, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACH_S_VoiePal.SetMaxLength( 0 ) 
		self.RACH_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149113.Add( self.RACH_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109113.Add( fgSizer1149113, 1, wx.EXPAND, 1 )
		
		self.RACH_PanelS = wx.Panel( self.m_panel109, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010113 = wx.BoxSizer( wx.VERTICAL )
		
		self.RACH_S_Info1 = wx.StaticText( self.RACH_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACH_S_Info1.Wrap( -1 )
		bSizer2010113.Add( self.RACH_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RACH_S_Info2 = wx.StaticText( self.RACH_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACH_S_Info2.Wrap( -1 )
		bSizer2010113.Add( self.RACH_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RACH_PanelS.SetSizer( bSizer2010113 )
		self.RACH_PanelS.Layout()
		bSizer2010113.Fit( self.RACH_PanelS )
		bSizer109113.Add( self.RACH_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar05 = wx.Button( self.m_panel109, wx.ID_ANY, u"CHAUMONT", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar05.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar05.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar05.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109113.Add( self.ButtonOpenStat_radar05, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer109113, 1, wx.EXPAND, 5 )
		
		
		fgSizer127.Add( bSizer9, 0, wx.EXPAND, 0 )
		
		
		self.m_panel109.SetSizer( fgSizer127 )
		self.m_panel109.Layout()
		bSizer1.Add( self.m_panel109, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel1091 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel1091.SetMaxSize( wx.Size( 1280,-1 ) )
		
		fgSizer1271 = wx.FlexGridSizer( 1, 6, 0, 0 )
		fgSizer1271.AddGrowableCol( 1 )
		fgSizer1271.AddGrowableCol( 2 )
		fgSizer1271.AddGrowableCol( 3 )
		fgSizer1271.AddGrowableCol( 4 )
		fgSizer1271.AddGrowableCol( 5 )
		fgSizer1271.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer1271.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText821 = wx.StaticText( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText821.Wrap( -1 )
		bSizer81.Add( self.m_staticText821, 1, wx.ALL|wx.EXPAND, 1 )
		
		self.m_staticText1171 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"MODE S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1171.Wrap( -1 )
		self.m_staticText1171.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer81.Add( self.m_staticText1171, 2, wx.ALIGN_CENTER|wx.SHAPED|wx.EXPAND, 0 )
		
		
		fgSizer1271.Add( bSizer81, 0, wx.EXPAND, 0 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer109114 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149114 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149114.AddGrowableRow( 0 )
		fgSizer1149114.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149114.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RABL_RadarRotatif = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149114.Add( self.RABL_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049114 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049114.Wrap( -1 )
		self.m_staticText2049114.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049114.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149114.Add( self.m_staticText2049114, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059114 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059114.Wrap( -1 )
		self.m_staticText2059114.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059114.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149114.Add( self.m_staticText2059114, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RABL_S_PeriodeRotation = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RABL_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149114.Add( self.RABL_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABL_S_NbPlotsTour = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RABL_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149114.Add( self.RABL_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABL_S_VoiePal = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_VoiePal.SetMaxLength( 0 ) 
		self.RABL_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149114.Add( self.RABL_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109114.Add( fgSizer1149114, 1, wx.EXPAND, 1 )
		
		self.RABL_PanelS = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010114 = wx.BoxSizer( wx.VERTICAL )
		
		self.RABL_S_Info1 = wx.StaticText( self.RABL_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABL_S_Info1.Wrap( -1 )
		bSizer2010114.Add( self.RABL_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RABL_S_Info2 = wx.StaticText( self.RABL_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABL_S_Info2.Wrap( -1 )
		bSizer2010114.Add( self.RABL_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RABL_PanelS.SetSizer( bSizer2010114 )
		self.RABL_PanelS.Layout()
		bSizer2010114.Fit( self.RABL_PanelS )
		bSizer109114.Add( self.RABL_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar06 = wx.Button( self.m_panel1091, wx.ID_ANY, u"BOULOGNE", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar06.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar06.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar06.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109114.Add( self.ButtonOpenStat_radar06, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer91.Add( bSizer109114, 1, wx.EXPAND, 5 )
		
		bSizer109115 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149115 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149115.AddGrowableRow( 0 )
		fgSizer1149115.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149115.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAPN_RadarRotatif = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149115.Add( self.RAPN_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049115 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049115.Wrap( -1 )
		self.m_staticText2049115.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049115.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149115.Add( self.m_staticText2049115, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059115 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059115.Wrap( -1 )
		self.m_staticText2059115.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059115.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149115.Add( self.m_staticText2059115, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAPN_S_PeriodeRotation = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RAPN_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149115.Add( self.RAPN_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPN_S_NbPlotsTour = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RAPN_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149115.Add( self.RAPN_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPN_S_VoiePal = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_VoiePal.SetMaxLength( 0 ) 
		self.RAPN_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149115.Add( self.RAPN_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109115.Add( fgSizer1149115, 1, wx.EXPAND, 1 )
		
		self.RAPN_PanelS = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010115 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAPN_S_Info1 = wx.StaticText( self.RAPN_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPN_S_Info1.Wrap( -1 )
		bSizer2010115.Add( self.RAPN_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAPN_S_Info2 = wx.StaticText( self.RAPN_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPN_S_Info2.Wrap( -1 )
		bSizer2010115.Add( self.RAPN_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAPN_PanelS.SetSizer( bSizer2010115 )
		self.RAPN_PanelS.Layout()
		bSizer2010115.Fit( self.RAPN_PanelS )
		bSizer109115.Add( self.RAPN_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar07 = wx.Button( self.m_panel1091, wx.ID_ANY, u"COUBRON", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar07.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar07.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar07.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109115.Add( self.ButtonOpenStat_radar07, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer91.Add( bSizer109115, 1, wx.EXPAND, 5 )
		
		bSizer109116 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149116 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149116.AddGrowableRow( 0 )
		fgSizer1149116.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149116.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAGB_RadarRotatif = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149116.Add( self.RAGB_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049116 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049116.Wrap( -1 )
		self.m_staticText2049116.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049116.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149116.Add( self.m_staticText2049116, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059116 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059116.Wrap( -1 )
		self.m_staticText2059116.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059116.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149116.Add( self.m_staticText2059116, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAGB_S_PeriodeRotation = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RAGB_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149116.Add( self.RAGB_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAGB_S_NbPlotsTour = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RAGB_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149116.Add( self.RAGB_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAGB_S_VoiePal = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_VoiePal.SetMaxLength( 0 ) 
		self.RAGB_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149116.Add( self.RAGB_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109116.Add( fgSizer1149116, 1, wx.EXPAND, 1 )
		
		self.RAGB_PanelS = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010116 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAGB_S_Info1 = wx.StaticText( self.RAGB_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAGB_S_Info1.Wrap( -1 )
		bSizer2010116.Add( self.RAGB_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAGB_S_Info2 = wx.StaticText( self.RAGB_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAGB_S_Info2.Wrap( -1 )
		bSizer2010116.Add( self.RAGB_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAGB_PanelS.SetSizer( bSizer2010116 )
		self.RAGB_PanelS.Layout()
		bSizer2010116.Fit( self.RAGB_PanelS )
		bSizer109116.Add( self.RAGB_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar08 = wx.Button( self.m_panel1091, wx.ID_ANY, u"GRAND-BALLON", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar08.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar08.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar08.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109116.Add( self.ButtonOpenStat_radar08, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer91.Add( bSizer109116, 1, wx.EXPAND, 5 )
		
		bSizer109117 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149117 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149117.AddGrowableRow( 0 )
		fgSizer1149117.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149117.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RACD_RadarRotatif = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149117.Add( self.RACD_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049117 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049117.Wrap( -1 )
		self.m_staticText2049117.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049117.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149117.Add( self.m_staticText2049117, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059117 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059117.Wrap( -1 )
		self.m_staticText2059117.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059117.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149117.Add( self.m_staticText2059117, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RACD_S_PeriodeRotation = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RACD_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149117.Add( self.RACD_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACD_S_NbPlotsTour = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RACD_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149117.Add( self.RACD_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACD_S_VoiePal = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_VoiePal.SetMaxLength( 0 ) 
		self.RACD_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149117.Add( self.RACD_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109117.Add( fgSizer1149117, 1, wx.EXPAND, 1 )
		
		self.RACD_PanelS = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010117 = wx.BoxSizer( wx.VERTICAL )
		
		self.RACD_S_Info1 = wx.StaticText( self.RACD_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACD_S_Info1.Wrap( -1 )
		bSizer2010117.Add( self.RACD_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RACD_S_Info2 = wx.StaticText( self.RACD_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACD_S_Info2.Wrap( -1 )
		bSizer2010117.Add( self.RACD_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RACD_PanelS.SetSizer( bSizer2010117 )
		self.RACD_PanelS.Layout()
		bSizer2010117.Fit( self.RACD_PanelS )
		bSizer109117.Add( self.RACD_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar09 = wx.Button( self.m_panel1091, wx.ID_ANY, u"ROISSY", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar09.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar09.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar09.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer109117.Add( self.ButtonOpenStat_radar09, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer91.Add( bSizer109117, 1, wx.EXPAND, 5 )
		
		bSizer109118 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1149118 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer1149118.AddGrowableRow( 0 )
		fgSizer1149118.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1149118.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RABE_RadarRotatif = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer1149118.Add( self.RABE_RadarRotatif, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2049118 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2049118.Wrap( -1 )
		self.m_staticText2049118.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2049118.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer1149118.Add( self.m_staticText2049118, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText2059118 = wx.StaticText( self.m_panel1091, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText2059118.Wrap( -1 )
		self.m_staticText2059118.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText2059118.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer1149118.Add( self.m_staticText2059118, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RABE_S_PeriodeRotation = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_PeriodeRotation.SetMaxLength( 0 ) 
		self.RABE_S_PeriodeRotation.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149118.Add( self.RABE_S_PeriodeRotation, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABE_S_NbPlotsTour = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_NbPlotsTour.SetMaxLength( 0 ) 
		self.RABE_S_NbPlotsTour.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149118.Add( self.RABE_S_NbPlotsTour, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABE_S_VoiePal = wx.TextCtrl( self.m_panel1091, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_VoiePal.SetMaxLength( 0 ) 
		self.RABE_S_VoiePal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1149118.Add( self.RABE_S_VoiePal, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer109118.Add( fgSizer1149118, 1, wx.EXPAND, 1 )
		
		self.RABE_PanelS = wx.Panel( self.m_panel1091, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer2010118 = wx.BoxSizer( wx.VERTICAL )
		
		self.RABE_S_Info1 = wx.StaticText( self.RABE_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABE_S_Info1.Wrap( -1 )
		bSizer2010118.Add( self.RABE_S_Info1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RABE_S_Info2 = wx.StaticText( self.RABE_PanelS, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABE_S_Info2.Wrap( -1 )
		bSizer2010118.Add( self.RABE_S_Info2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RABE_PanelS.SetSizer( bSizer2010118 )
		self.RABE_PanelS.Layout()
		bSizer2010118.Fit( self.RABE_PanelS )
		bSizer109118.Add( self.RABE_PanelS, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar10 = wx.Button( self.m_panel1091, wx.ID_ANY, u"BERTEM", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar10.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar10.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer109118.Add( self.ButtonOpenStat_radar10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer91.Add( bSizer109118, 1, wx.EXPAND, 5 )
		
		
		fgSizer1271.Add( bSizer91, 0, wx.EXPAND, 0 )
		
		
		self.m_panel1091.SetSizer( fgSizer1271 )
		self.m_panel1091.Layout()
		bSizer1.Add( self.m_panel1091, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10911 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel10911.SetMaxSize( wx.Size( 1280,-1 ) )
		
		fgSizer12711 = wx.FlexGridSizer( 1, 6, 0, 0 )
		fgSizer12711.AddGrowableCol( 1 )
		fgSizer12711.AddGrowableCol( 2 )
		fgSizer12711.AddGrowableCol( 3 )
		fgSizer12711.AddGrowableCol( 4 )
		fgSizer12711.AddGrowableCol( 5 )
		fgSizer12711.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer12711.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		bSizer811 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer811.SetMinSize( wx.Size( 93,-1 ) ) 
		self.m_staticText8211 = wx.StaticText( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText8211.Wrap( -1 )
		bSizer811.Add( self.m_staticText8211, 1, wx.ALL|wx.EXPAND, 1 )
		
		self.m_staticText11711 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"TMA", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText11711.Wrap( -1 )
		self.m_staticText11711.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer811.Add( self.m_staticText11711, 2, wx.ALIGN_CENTER|wx.SHAPED|wx.EXPAND, 0 )
		
		
		fgSizer12711.Add( bSizer811, 0, wx.EXPAND, 0 )
		
		bSizer911 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1091141 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491141 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491141.AddGrowableRow( 0 )
		fgSizer11491141.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491141.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RABL_RadarRotatif1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491141.Add( self.RABL_RadarRotatif1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491141 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491141.Wrap( -1 )
		self.m_staticText20491141.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491141.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491141.Add( self.m_staticText20491141, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591141 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591141.Wrap( -1 )
		self.m_staticText20591141.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591141.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491141.Add( self.m_staticText20591141, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RABL_S_PeriodeRotation1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_PeriodeRotation1.SetMaxLength( 0 ) 
		self.RABL_S_PeriodeRotation1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491141.Add( self.RABL_S_PeriodeRotation1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABL_S_NbPlotsTour1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_NbPlotsTour1.SetMaxLength( 0 ) 
		self.RABL_S_NbPlotsTour1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491141.Add( self.RABL_S_NbPlotsTour1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABL_S_VoiePal1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABL_S_VoiePal1.SetMaxLength( 0 ) 
		self.RABL_S_VoiePal1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491141.Add( self.RABL_S_VoiePal1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091141.Add( fgSizer11491141, 1, wx.EXPAND, 1 )
		
		self.RABL_PanelS1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101141 = wx.BoxSizer( wx.VERTICAL )
		
		self.RABL_S_Info11 = wx.StaticText( self.RABL_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABL_S_Info11.Wrap( -1 )
		bSizer20101141.Add( self.RABL_S_Info11, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RABL_S_Info21 = wx.StaticText( self.RABL_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABL_S_Info21.Wrap( -1 )
		bSizer20101141.Add( self.RABL_S_Info21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RABL_PanelS1.SetSizer( bSizer20101141 )
		self.RABL_PanelS1.Layout()
		bSizer20101141.Fit( self.RABL_PanelS1 )
		bSizer1091141.Add( self.RABL_PanelS1, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar061 = wx.Button( self.m_panel10911, wx.ID_ANY, u"TMA1", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar061.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar061.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar061.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer1091141.Add( self.ButtonOpenStat_radar061, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer911.Add( bSizer1091141, 1, wx.EXPAND, 5 )
		
		bSizer1091151 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491151 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491151.AddGrowableRow( 0 )
		fgSizer11491151.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAPN_RadarRotatif1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491151.Add( self.RAPN_RadarRotatif1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491151 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491151.Wrap( -1 )
		self.m_staticText20491151.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491151.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491151.Add( self.m_staticText20491151, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591151 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591151.Wrap( -1 )
		self.m_staticText20591151.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591151.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491151.Add( self.m_staticText20591151, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAPN_S_PeriodeRotation1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_PeriodeRotation1.SetMaxLength( 0 ) 
		self.RAPN_S_PeriodeRotation1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491151.Add( self.RAPN_S_PeriodeRotation1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPN_S_NbPlotsTour1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_NbPlotsTour1.SetMaxLength( 0 ) 
		self.RAPN_S_NbPlotsTour1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491151.Add( self.RAPN_S_NbPlotsTour1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAPN_S_VoiePal1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAPN_S_VoiePal1.SetMaxLength( 0 ) 
		self.RAPN_S_VoiePal1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491151.Add( self.RAPN_S_VoiePal1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091151.Add( fgSizer11491151, 1, wx.EXPAND, 1 )
		
		self.RAPN_PanelS1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101151 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAPN_S_Info11 = wx.StaticText( self.RAPN_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPN_S_Info11.Wrap( -1 )
		bSizer20101151.Add( self.RAPN_S_Info11, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAPN_S_Info21 = wx.StaticText( self.RAPN_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAPN_S_Info21.Wrap( -1 )
		bSizer20101151.Add( self.RAPN_S_Info21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAPN_PanelS1.SetSizer( bSizer20101151 )
		self.RAPN_PanelS1.Layout()
		bSizer20101151.Fit( self.RAPN_PanelS1 )
		bSizer1091151.Add( self.RAPN_PanelS1, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar071 = wx.Button( self.m_panel10911, wx.ID_ANY, u"TMA2", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar071.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar071.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar071.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer1091151.Add( self.ButtonOpenStat_radar071, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer911.Add( bSizer1091151, 1, wx.EXPAND, 5 )
		
		bSizer1091161 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491161 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491161.AddGrowableRow( 0 )
		fgSizer11491161.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RAGB_RadarRotatif1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491161.Add( self.RAGB_RadarRotatif1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491161 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491161.Wrap( -1 )
		self.m_staticText20491161.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491161.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491161.Add( self.m_staticText20491161, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591161 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591161.Wrap( -1 )
		self.m_staticText20591161.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591161.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491161.Add( self.m_staticText20591161, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RAGB_S_PeriodeRotation1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_PeriodeRotation1.SetMaxLength( 0 ) 
		self.RAGB_S_PeriodeRotation1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491161.Add( self.RAGB_S_PeriodeRotation1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAGB_S_NbPlotsTour1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_NbPlotsTour1.SetMaxLength( 0 ) 
		self.RAGB_S_NbPlotsTour1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491161.Add( self.RAGB_S_NbPlotsTour1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RAGB_S_VoiePal1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RAGB_S_VoiePal1.SetMaxLength( 0 ) 
		self.RAGB_S_VoiePal1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491161.Add( self.RAGB_S_VoiePal1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091161.Add( fgSizer11491161, 1, wx.EXPAND, 1 )
		
		self.RAGB_PanelS1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101161 = wx.BoxSizer( wx.VERTICAL )
		
		self.RAGB_S_Info11 = wx.StaticText( self.RAGB_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAGB_S_Info11.Wrap( -1 )
		bSizer20101161.Add( self.RAGB_S_Info11, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RAGB_S_Info21 = wx.StaticText( self.RAGB_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RAGB_S_Info21.Wrap( -1 )
		bSizer20101161.Add( self.RAGB_S_Info21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RAGB_PanelS1.SetSizer( bSizer20101161 )
		self.RAGB_PanelS1.Layout()
		bSizer20101161.Fit( self.RAGB_PanelS1 )
		bSizer1091161.Add( self.RAGB_PanelS1, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar081 = wx.Button( self.m_panel10911, wx.ID_ANY, u"TMA4", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar081.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar081.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar081.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer1091161.Add( self.ButtonOpenStat_radar081, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer911.Add( bSizer1091161, 1, wx.EXPAND, 5 )
		
		bSizer1091171 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491171 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491171.AddGrowableRow( 0 )
		fgSizer11491171.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491171.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RACD_RadarRotatif1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491171.Add( self.RACD_RadarRotatif1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491171 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491171.Wrap( -1 )
		self.m_staticText20491171.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491171.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491171.Add( self.m_staticText20491171, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591171 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591171.Wrap( -1 )
		self.m_staticText20591171.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591171.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491171.Add( self.m_staticText20591171, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RACD_S_PeriodeRotation1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_PeriodeRotation1.SetMaxLength( 0 ) 
		self.RACD_S_PeriodeRotation1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491171.Add( self.RACD_S_PeriodeRotation1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACD_S_NbPlotsTour1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_NbPlotsTour1.SetMaxLength( 0 ) 
		self.RACD_S_NbPlotsTour1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491171.Add( self.RACD_S_NbPlotsTour1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RACD_S_VoiePal1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RACD_S_VoiePal1.SetMaxLength( 0 ) 
		self.RACD_S_VoiePal1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491171.Add( self.RACD_S_VoiePal1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091171.Add( fgSizer11491171, 1, wx.EXPAND, 1 )
		
		self.RACD_PanelS1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101171 = wx.BoxSizer( wx.VERTICAL )
		
		self.RACD_S_Info11 = wx.StaticText( self.RACD_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACD_S_Info11.Wrap( -1 )
		bSizer20101171.Add( self.RACD_S_Info11, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RACD_S_Info21 = wx.StaticText( self.RACD_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RACD_S_Info21.Wrap( -1 )
		bSizer20101171.Add( self.RACD_S_Info21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RACD_PanelS1.SetSizer( bSizer20101171 )
		self.RACD_PanelS1.Layout()
		bSizer20101171.Fit( self.RACD_PanelS1 )
		bSizer1091171.Add( self.RACD_PanelS1, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar091 = wx.Button( self.m_panel10911, wx.ID_ANY, u"TMA5", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar091.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar091.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar091.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		bSizer1091171.Add( self.ButtonOpenStat_radar091, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer911.Add( bSizer1091171, 1, wx.EXPAND, 5 )
		
		bSizer1091181 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer11491181 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer11491181.AddGrowableRow( 0 )
		fgSizer11491181.SetFlexibleDirection( wx.VERTICAL )
		fgSizer11491181.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.RABE_RadarRotatif1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,40 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer11491181.Add( self.RABE_RadarRotatif1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20491181 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"Nb Pistes\npar tour\n(Mode S)", wx.DefaultPosition, wx.Size( 60,60 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20491181.Wrap( -1 )
		self.m_staticText20491181.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20491181.SetMinSize( wx.Size( 60,60 ) )
		
		fgSizer11491181.Add( self.m_staticText20491181, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.m_staticText20591181 = wx.StaticText( self.m_panel10911, wx.ID_ANY, u"\nVOIE", wx.DefaultPosition, wx.Size( 40,40 ), wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText20591181.Wrap( -1 )
		self.m_staticText20591181.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText20591181.SetMinSize( wx.Size( 40,40 ) )
		
		fgSizer11491181.Add( self.m_staticText20591181, 2, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.RABE_S_PeriodeRotation1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_PeriodeRotation1.SetMaxLength( 0 ) 
		self.RABE_S_PeriodeRotation1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491181.Add( self.RABE_S_PeriodeRotation1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABE_S_NbPlotsTour1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_NbPlotsTour1.SetMaxLength( 0 ) 
		self.RABE_S_NbPlotsTour1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491181.Add( self.RABE_S_NbPlotsTour1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		self.RABE_S_VoiePal1 = wx.TextCtrl( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,20 ), wx.TE_READONLY|wx.STATIC_BORDER )
		self.RABE_S_VoiePal1.SetMaxLength( 0 ) 
		self.RABE_S_VoiePal1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11491181.Add( self.RABE_S_VoiePal1, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.RIGHT, 2 )
		
		
		bSizer1091181.Add( fgSizer11491181, 1, wx.EXPAND, 1 )
		
		self.RABE_PanelS1 = wx.Panel( self.m_panel10911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		bSizer20101181 = wx.BoxSizer( wx.VERTICAL )
		
		self.RABE_S_Info11 = wx.StaticText( self.RABE_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABE_S_Info11.Wrap( -1 )
		bSizer20101181.Add( self.RABE_S_Info11, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.RABE_S_Info21 = wx.StaticText( self.RABE_PanelS1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
		self.RABE_S_Info21.Wrap( -1 )
		bSizer20101181.Add( self.RABE_S_Info21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.RABE_PanelS1.SetSizer( bSizer20101181 )
		self.RABE_PanelS1.Layout()
		bSizer20101181.Fit( self.RABE_PanelS1 )
		bSizer1091181.Add( self.RABE_PanelS1, 2, wx.EXPAND |wx.ALL, 2 )
		
		self.ButtonOpenStat_radar101 = wx.Button( self.m_panel10911, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.ButtonOpenStat_radar101.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.ButtonOpenStat_radar101.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ButtonOpenStat_radar101.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer1091181.Add( self.ButtonOpenStat_radar101, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer911.Add( bSizer1091181, 1, wx.EXPAND, 5 )
		
		
		fgSizer12711.Add( bSizer911, 0, wx.EXPAND, 0 )
		
		
		self.m_panel10911.SetSizer( fgSizer12711 )
		self.m_panel10911.Layout()
		bSizer1.Add( self.m_panel10911, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpQuitApp.Bind( wx.EVT_BUTTON, self.QuitApplication )
		self.m_bpCoupureRadar.Bind( wx.EVT_BUTTON, self.OpenIncompatibiliteCoupureRadar )
		self.m_bpHisto.Bind( wx.EVT_BUTTON, self.OpenHistoPage )
		self.m_bpFavorite.Bind( wx.EVT_BUTTON, self.OpenPreferencePage )
		self.m_bpButtonHelp.Bind( wx.EVT_BUTTON, self.OpenHelpPage )
		self.ButtonOpenStat_radar01.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar01 )
		self.ButtonOpenStat_radar02.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar02 )
		self.ButtonOpenStat_radar03.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar03 )
		self.ButtonOpenStat_radar04.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar04 )
		self.ButtonOpenStat_radar05.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar05 )
		self.ButtonOpenStat_radar06.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar06 )
		self.ButtonOpenStat_radar07.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar07 )
		self.ButtonOpenStat_radar08.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar08 )
		self.ButtonOpenStat_radar09.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar09 )
		self.ButtonOpenStat_radar10.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar10 )
		self.ButtonOpenStat_radar061.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar11 )
		self.ButtonOpenStat_radar071.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar12 )
		self.ButtonOpenStat_radar081.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar13 )
		self.ButtonOpenStat_radar091.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar14 )
		self.ButtonOpenStat_radar101.Bind( wx.EVT_BUTTON, self.OpenStatsRadar_radar15 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def QuitApplication( self, event ):
		event.Skip()
	
	def OpenIncompatibiliteCoupureRadar( self, event ):
		event.Skip()
	
	def OpenHistoPage( self, event ):
		event.Skip()
	
	def OpenPreferencePage( self, event ):
		event.Skip()
	
	def OpenHelpPage( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar01( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar02( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar03( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar04( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar05( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar06( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar07( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar08( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar09( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar10( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar11( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar12( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar13( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar14( self, event ):
		event.Skip()
	
	def OpenStatsRadar_radar15( self, event ):
		event.Skip()
	

###########################################################################
## Class PageStatsRadar
###########################################################################

class PageStatsRadar ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer76 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer76.AddGrowableCol( 1 )
		fgSizer76.AddGrowableCol( 2 )
		fgSizer76.SetFlexibleDirection( wx.BOTH )
		fgSizer76.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ButtonFermerPageStatRadars = wx.Button( self, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonFermerPageStatRadars.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer76.Add( self.ButtonFermerPageStatRadars, 0, wx.EXPAND, 5 )
		
		self.Heure_Lancement_Appli = wx.TextCtrl( self, wx.ID_ANY, u"sfvsfsqdfsqdfsdfsdfsdf", wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_CENTRE|wx.TE_READONLY )
		self.Heure_Lancement_Appli.SetMaxLength( 0 ) 
		self.Heure_Lancement_Appli.SetFont( wx.Font( 12, 72, 93, 92, False, "Calibri" ) )
		self.Heure_Lancement_Appli.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.Heure_Lancement_Appli.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		fgSizer76.Add( self.Heure_Lancement_Appli, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		self.ChampAffichNomRadar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_CAPITALIZE|wx.TE_CENTRE|wx.TE_READONLY|wx.NO_BORDER )
		self.ChampAffichNomRadar.SetMaxLength( 0 ) 
		self.ChampAffichNomRadar.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		self.ChampAffichNomRadar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.ChampAffichNomRadar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		fgSizer76.Add( self.ChampAffichNomRadar, 0, wx.ALIGN_CENTER|wx.EXPAND, 5 )
		
		
		bSizer1.Add( fgSizer76, 0, wx.EXPAND, 5 )
		
		self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		self.m_notebook.SetFont( wx.Font( 18, 70, 90, 91, False, wx.EmptyString ) )
		
		self.Stat_modeS = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.Stat_modeS.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer6711111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4811111 = wx.Panel( self.Stat_modeS, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel4811111.SetBackgroundColour( wx.Colour( 204, 211, 227 ) )
		
		fgSizer2311111 = wx.FlexGridSizer( 2, 3, 0, 0 )
		fgSizer2311111.SetFlexibleDirection( wx.VERTICAL )
		fgSizer2311111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_panel5221111 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel5221111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer5521111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14421111 = wx.StaticText( self.m_panel5221111, wx.ID_ANY, u"Voie Principale", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText14421111.Wrap( -1 )
		self.m_staticText14421111.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer5521111.Add( self.m_staticText14421111, 0, wx.ALIGN_CENTER|wx.ALL, 10 )
		
		self.S_VoiePal = wx.TextCtrl( self.m_panel5221111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.S_VoiePal.SetMaxLength( 0 ) 
		self.S_VoiePal.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer5521111.Add( self.S_VoiePal, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.m_panel5221111.SetSizer( bSizer5521111 )
		self.m_panel5221111.Layout()
		bSizer5521111.Fit( self.m_panel5221111 )
		fgSizer2311111.Add( self.m_panel5221111, 0, wx.ALIGN_CENTER|wx.ALL, 15 )
		
		self.m_panel52121111 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel52121111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer55121111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText144121111 = wx.StaticText( self.m_panel52121111, wx.ID_ANY, u"Période de rotation (sec)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText144121111.Wrap( -1 )
		self.m_staticText144121111.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer55121111.Add( self.m_staticText144121111, 0, wx.ALL, 10 )
		
		self.S_PeriodeRotation = wx.TextCtrl( self.m_panel52121111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.S_PeriodeRotation.SetMaxLength( 0 ) 
		self.S_PeriodeRotation.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer55121111.Add( self.S_PeriodeRotation, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.m_panel52121111.SetSizer( bSizer55121111 )
		self.m_panel52121111.Layout()
		bSizer55121111.Fit( self.m_panel52121111 )
		fgSizer2311111.Add( self.m_panel52121111, 0, wx.ALIGN_CENTER|wx.ALL, 15 )
		
		self.m_panel521111111 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel521111111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer551111111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1441111111 = wx.StaticText( self.m_panel521111111, wx.ID_ANY, u"Heure Station", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1441111111.Wrap( -1 )
		self.m_staticText1441111111.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer551111111.Add( self.m_staticText1441111111, 0, wx.ALIGN_CENTER|wx.ALL, 10 )
		
		self.S_HeureStation = wx.TextCtrl( self.m_panel521111111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER )
		self.S_HeureStation.SetMaxLength( 0 ) 
		self.S_HeureStation.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer551111111.Add( self.S_HeureStation, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.m_panel521111111.SetSizer( bSizer551111111 )
		self.m_panel521111111.Layout()
		bSizer551111111.Fit( self.m_panel521111111 )
		fgSizer2311111.Add( self.m_panel521111111, 1, wx.ALIGN_CENTER|wx.ALL, 15 )
		
		self.m_panel7231111 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel7231111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer6231111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6531111 = wx.Panel( self.m_panel7231111, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gSizer131111 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_staticText15331111 = wx.StaticText( self.m_panel6531111, wx.ID_ANY, u"QUALITE RADAR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.NO_BORDER )
		self.m_staticText15331111.Wrap( -1 )
		self.m_staticText15331111.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer131111.Add( self.m_staticText15331111, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel6531111.SetSizer( gSizer131111 )
		self.m_panel6531111.Layout()
		gSizer131111.Fit( self.m_panel6531111 )
		bSizer6231111.Add( self.m_panel6531111, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel6631111 = wx.Panel( self.m_panel7231111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2631111 = wx.FlexGridSizer( 12, 2, 20, 0 )
		fgSizer2631111.AddGrowableCol( 0 )
		fgSizer2631111.SetFlexibleDirection( wx.BOTH )
		fgSizer2631111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText16041111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"Nbr de Plots Pistés", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16041111.Wrap( -1 )
		self.m_staticText16041111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16041111, 0, wx.EXPAND|wx.TOP, 15 )
		
		self.S_NbPlotsPistes = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_NbPlotsPistes.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_NbPlotsPistes, 0, wx.TOP, 15 )
		
		self.m_staticText160131111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"Nbr de Plots / Tour", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText160131111.Wrap( -1 )
		self.m_staticText160131111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText160131111, 0, wx.EXPAND, 0 )
		
		self.S_NbPlotsTour = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_NbPlotsTour.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_NbPlotsTour, 0, wx.ALL, 0 )
		
		self.m_staticText1601131111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% Detection", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText1601131111.Wrap( -1 )
		self.m_staticText1601131111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText1601131111, 0, wx.EXPAND, 0 )
		
		self.S_TauxDetection = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxDetection.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxDetection, 0, wx.ALL, 0 )
		
		self.m_staticText16011111111211211 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% Detection All Call", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16011111111211211.Wrap( -1 )
		self.m_staticText16011111111211211.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16011111111211211, 0, wx.EXPAND, 0 )
		
		self.S_TauxDetectAllCall = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxDetectAllCall.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxDetectAllCall, 0, 0, 0 )
		
		self.m_staticText16011111111211111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% Detection Roll Call", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16011111111211111.Wrap( -1 )
		self.m_staticText16011111111211111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16011111111211111, 0, wx.EXPAND, 0 )
		
		self.S_TauxDetectRollCall = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxDetectRollCall.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxDetectRollCall, 0, wx.ALL, 0 )
		
		self.m_staticText16011131111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% D'invalides Mode A", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16011131111.Wrap( -1 )
		self.m_staticText16011131111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16011131111, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.S_TauxInvalidModA = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxInvalidModA.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxInvalidModA, 0, wx.ALL, 0 )
		
		self.m_staticText160111131111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% D'invalides Mode C", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText160111131111.Wrap( -1 )
		self.m_staticText160111131111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText160111131111, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.S_TauxInvalidModC = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxInvalidModC.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxInvalidModC, 0, wx.ALL, 0 )
		
		self.m_staticText160111111121111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% De Doublons", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText160111111121111.Wrap( -1 )
		self.m_staticText160111111121111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText160111111121111, 0, wx.EXPAND, 0 )
		
		self.S_TauxDoublons = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxDoublons.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxDoublons, 0, 0, 0 )
		
		self.m_staticText1601111111121131 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% De Plots Douteux", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText1601111111121131.Wrap( -1 )
		self.m_staticText1601111111121131.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText1601111111121131, 0, wx.EXPAND, 0 )
		
		self.S_TauxDouteux = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxDouteux.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxDouteux, 0, wx.ALL, 0 )
		
		self.m_staticText1601111121111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% De Fantomes", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText1601111121111.Wrap( -1 )
		self.m_staticText1601111121111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText1601111121111, 0, wx.EXPAND, 0 )
		
		self.S_TauxFantomes = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_TauxFantomes.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_TauxFantomes, 0, 0, 0 )
		
		self.m_staticText16011111121111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% @ Mode S invalide", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16011111121111.Wrap( -1 )
		self.m_staticText16011111121111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16011111121111, 0, wx.EXPAND, 0 )
		
		self.S_AddrSInvalid = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_AddrSInvalid.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_AddrSInvalid, 0, 0, 0 )
		
		self.m_staticText16011111111111111 = wx.StaticText( self.m_panel6631111, wx.ID_ANY, u"% Erreur Mode S corrigée", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		self.m_staticText16011111111111111.Wrap( -1 )
		self.m_staticText16011111111111111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2631111.Add( self.m_staticText16011111111111111, 0, wx.BOTTOM|wx.EXPAND, 15 )
		
		self.S_ErreurSCorrigee = wx.TextCtrl( self.m_panel6631111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_ErreurSCorrigee.SetMaxLength( 0 ) 
		fgSizer2631111.Add( self.S_ErreurSCorrigee, 0, wx.BOTTOM, 15 )
		
		
		self.m_panel6631111.SetSizer( fgSizer2631111 )
		self.m_panel6631111.Layout()
		fgSizer2631111.Fit( self.m_panel6631111 )
		bSizer6231111.Add( self.m_panel6631111, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel7231111.SetSizer( bSizer6231111 )
		self.m_panel7231111.Layout()
		bSizer6231111.Fit( self.m_panel7231111 )
		fgSizer2311111.Add( self.m_panel7231111, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel99112 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel99112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		fgSizer50111 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer50111.AddGrowableRow( 1 )
		fgSizer50111.SetFlexibleDirection( wx.BOTH )
		fgSizer50111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel651111111 = wx.Panel( self.m_panel99112, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel651111111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		gSizer11111111 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_staticText1531111111 = wx.StaticText( self.m_panel651111111, wx.ID_ANY, u"ALARMES ET ERREURS", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.NO_BORDER )
		self.m_staticText1531111111.Wrap( -1 )
		self.m_staticText1531111111.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer11111111.Add( self.m_staticText1531111111, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel651111111.SetSizer( gSizer11111111 )
		self.m_panel651111111.Layout()
		gSizer11111111.Fit( self.m_panel651111111 )
		fgSizer50111.Add( self.m_panel651111111, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel661211111 = wx.Panel( self.m_panel99112, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel661211111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		fgSizer261211111 = wx.FlexGridSizer( 5, 2, 20, 0 )
		fgSizer261211111.AddGrowableCol( 0 )
		fgSizer261211111.SetFlexibleDirection( wx.BOTH )
		fgSizer261211111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText1602211111 = wx.StaticText( self.m_panel661211111, wx.ID_ANY, u"Nbr d'Erreurs de Decodage", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText1602211111.Wrap( -1 )
		self.m_staticText1602211111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261211111.Add( self.m_staticText1602211111, 0, wx.TOP|wx.EXPAND, 15 )
		
		self.S_ErreurDecod = wx.TextCtrl( self.m_panel661211111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_ErreurDecod.SetMaxLength( 0 ) 
		fgSizer261211111.Add( self.S_ErreurDecod, 0, wx.TOP, 15 )
		
		self.m_staticText16012211111 = wx.StaticText( self.m_panel661211111, wx.ID_ANY, u"Nbr d'Erreurs de Syntaxe", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText16012211111.Wrap( -1 )
		self.m_staticText16012211111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261211111.Add( self.m_staticText16012211111, 0, wx.EXPAND, 0 )
		
		self.S_ErreurSyntax = wx.TextCtrl( self.m_panel661211111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_ErreurSyntax.SetMaxLength( 0 ) 
		fgSizer261211111.Add( self.S_ErreurSyntax, 0, wx.ALL, 0 )
		
		self.m_staticText160112211111 = wx.StaticText( self.m_panel661211111, wx.ID_ANY, u"Nbr d'Erreurs Fin de Bloc", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText160112211111.Wrap( -1 )
		self.m_staticText160112211111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261211111.Add( self.m_staticText160112211111, 0, wx.EXPAND, 0 )
		
		self.S_ErreurFinBloc = wx.TextCtrl( self.m_panel661211111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_ErreurFinBloc.SetMaxLength( 0 ) 
		fgSizer261211111.Add( self.S_ErreurFinBloc, 0, wx.ALL, 0 )
		
		self.m_staticText1601112111111 = wx.StaticText( self.m_panel661211111, wx.ID_ANY, u"Nbr Fin de Bloc Sans Heure", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText1601112111111.Wrap( -1 )
		self.m_staticText1601112111111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261211111.Add( self.m_staticText1601112111111, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.S_ErreurBlocSansHeure = wx.TextCtrl( self.m_panel661211111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_ErreurBlocSansHeure.SetMaxLength( 0 ) 
		fgSizer261211111.Add( self.S_ErreurBlocSansHeure, 0, wx.ALL, 0 )
		
		self.m_staticText16011112111111 = wx.StaticText( self.m_panel661211111, wx.ID_ANY, u"Nbr de Fin de Bloc Absent", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText16011112111111.Wrap( -1 )
		self.m_staticText16011112111111.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261211111.Add( self.m_staticText16011112111111, 0, wx.BOTTOM|wx.EXPAND, 20 )
		
		self.S_FinBlocAbsent = wx.TextCtrl( self.m_panel661211111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_FinBlocAbsent.SetMaxLength( 0 ) 
		fgSizer261211111.Add( self.S_FinBlocAbsent, 0, wx.BOTTOM, 20 )
		
		
		self.m_panel661211111.SetSizer( fgSizer261211111 )
		self.m_panel661211111.Layout()
		fgSizer261211111.Fit( self.m_panel661211111 )
		fgSizer50111.Add( self.m_panel661211111, 1, wx.ALL, 5 )
		
		
		self.m_panel99112.SetSizer( fgSizer50111 )
		self.m_panel99112.Layout()
		fgSizer50111.Fit( self.m_panel99112 )
		fgSizer2311111.Add( self.m_panel99112, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel9911121 = wx.Panel( self.m_panel4811111, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3111121 = wx.FlexGridSizer( 2, 1, 55, 0 )
		fgSizer3111121.AddGrowableRow( 1 )
		fgSizer3111121.SetFlexibleDirection( wx.BOTH )
		fgSizer3111121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_panel72221121 = wx.Panel( self.m_panel9911121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel72221121.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer62211121 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel65221121 = wx.Panel( self.m_panel72221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gSizer1221121 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_staticText153221121 = wx.StaticText( self.m_panel65221121, wx.ID_ANY, u"ETAT STATION", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.NO_BORDER )
		self.m_staticText153221121.Wrap( -1 )
		self.m_staticText153221121.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer1221121.Add( self.m_staticText153221121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel65221121.SetSizer( gSizer1221121 )
		self.m_panel65221121.Layout()
		gSizer1221121.Fit( self.m_panel65221121 )
		bSizer62211121.Add( self.m_panel65221121, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel66221121 = wx.Panel( self.m_panel72221121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer26211121 = wx.FlexGridSizer( 6, 2, 20, 0 )
		fgSizer26211121.AddGrowableCol( 1 )
		fgSizer26211121.SetFlexibleDirection( wx.BOTH )
		fgSizer26211121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.S_PresenceInfoStation = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_PresenceInfoStation, 1, wx.ALIGN_CENTER|wx.ALL, 0 )
		
		self.m_staticText160321121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Presence du champ Info station", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160321121.Wrap( -1 )
		self.m_staticText160321121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText160321121, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		self.S_EtatStation = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_EtatStation, 1, wx.ALIGN_CENTER, 0 )
		
		self.m_staticText1603121121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Etat de la Station", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1603121121.Wrap( -1 )
		self.m_staticText1603121121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText1603121121, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		self.S_SynchroHoraireExt = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_SynchroHoraireExt, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_staticText16031121121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Synchro Horaire Externe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16031121121.Wrap( -1 )
		self.m_staticText16031121121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText16031121121, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		self.S_ConnectSTS = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_ConnectSTS, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_staticText160311121121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Connexion à STS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160311121121.Wrap( -1 )
		self.m_staticText160311121121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText160311121121, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		self.S_TauxCharge = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_TauxCharge, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_staticText1603111121121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Taux de Charge Radar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1603111121121.Wrap( -1 )
		self.m_staticText1603111121121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText1603111121121, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		self.S_PorteeRadar = wx.Panel( self.m_panel66221121, wx.ID_ANY, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer26211121.Add( self.S_PorteeRadar, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticText16031111111121 = wx.StaticText( self.m_panel66221121, wx.ID_ANY, u"Portee Radar Normale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16031111111121.Wrap( -1 )
		self.m_staticText16031111111121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer26211121.Add( self.m_staticText16031111111121, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT, 10 )
		
		
		self.m_panel66221121.SetSizer( fgSizer26211121 )
		self.m_panel66221121.Layout()
		fgSizer26211121.Fit( self.m_panel66221121 )
		bSizer62211121.Add( self.m_panel66221121, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 20 )
		
		
		self.m_panel72221121.SetSizer( bSizer62211121 )
		self.m_panel72221121.Layout()
		bSizer62211121.Fit( self.m_panel72221121 )
		fgSizer3111121.Add( self.m_panel72221121, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.RIGHT, 15 )
		
		self.m_panel722111121 = wx.Panel( self.m_panel9911121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel722111121.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		fgSizer4621 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer4621.AddGrowableRow( 1 )
		fgSizer4621.SetFlexibleDirection( wx.BOTH )
		fgSizer4621.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_panel652111121 = wx.Panel( self.m_panel722111121, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		gSizer12111121 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_staticText1532111121 = wx.StaticText( self.m_panel652111121, wx.ID_ANY, u"BALISE DE TEST", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.NO_BORDER )
		self.m_staticText1532111121.Wrap( -1 )
		self.m_staticText1532111121.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		gSizer12111121.Add( self.m_staticText1532111121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel652111121.SetSizer( gSizer12111121 )
		self.m_panel652111121.Layout()
		gSizer12111121.Fit( self.m_panel652111121 )
		fgSizer4621.Add( self.m_panel652111121, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel662111121 = wx.Panel( self.m_panel722111121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer621111121 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel661111121 = wx.Panel( self.m_panel662111121, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer261111121 = wx.FlexGridSizer( 4, 2, 20, 0 )
		fgSizer261111121.AddGrowableCol( 0 )
		fgSizer261111121.SetFlexibleDirection( wx.BOTH )
		fgSizer261111121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText1602111121 = wx.StaticText( self.m_panel661111121, wx.ID_ANY, u"Distance En NM", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText1602111121.Wrap( -1 )
		self.m_staticText1602111121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261111121.Add( self.m_staticText1602111121, 0, wx.EXPAND|wx.TOP, 15 )
		
		self.S_BaliseTSTDistance = wx.TextCtrl( self.m_panel661111121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_BaliseTSTDistance.SetMaxLength( 0 ) 
		fgSizer261111121.Add( self.S_BaliseTSTDistance, 0, wx.TOP, 15 )
		
		self.m_staticText16012111121 = wx.StaticText( self.m_panel661111121, wx.ID_ANY, u"Azimut en Degré", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText16012111121.Wrap( -1 )
		self.m_staticText16012111121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261111121.Add( self.m_staticText16012111121, 0, wx.EXPAND, 0 )
		
		self.S_AzimutDegre = wx.TextCtrl( self.m_panel661111121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_AzimutDegre.SetMaxLength( 0 ) 
		fgSizer261111121.Add( self.S_AzimutDegre, 0, wx.ALL, 0 )
		
		self.m_staticText160112121121 = wx.StaticText( self.m_panel661111121, wx.ID_ANY, u"Azimut en Epsilon (Mesurée)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText160112121121.Wrap( -1 )
		self.m_staticText160112121121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261111121.Add( self.m_staticText160112121121, 0, wx.EXPAND, 0 )
		
		self.S_AzimutEpsiMesur = wx.TextCtrl( self.m_panel661111121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_AzimutEpsiMesur.SetMaxLength( 0 ) 
		fgSizer261111121.Add( self.S_AzimutEpsiMesur, 0, wx.ALL, 0 )
		
		self.m_staticText1601121111121 = wx.StaticText( self.m_panel661111121, wx.ID_ANY, u"Azimut en Epsilon (Théorie)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.SIMPLE_BORDER )
		self.m_staticText1601121111121.Wrap( -1 )
		self.m_staticText1601121111121.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer261111121.Add( self.m_staticText1601121111121, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.S_AzimutEpsiTheo = wx.TextCtrl( self.m_panel661111121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.S_AzimutEpsiTheo.SetMaxLength( 0 ) 
		fgSizer261111121.Add( self.S_AzimutEpsiTheo, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panel661111121.SetSizer( fgSizer261111121 )
		self.m_panel661111121.Layout()
		fgSizer261111121.Fit( self.m_panel661111121 )
		bSizer621111121.Add( self.m_panel661111121, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		
		self.m_panel662111121.SetSizer( bSizer621111121 )
		self.m_panel662111121.Layout()
		bSizer621111121.Fit( self.m_panel662111121 )
		fgSizer4621.Add( self.m_panel662111121, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT|wx.TOP, 5 )
		
		
		self.m_panel722111121.SetSizer( fgSizer4621 )
		self.m_panel722111121.Layout()
		fgSizer4621.Fit( self.m_panel722111121 )
		fgSizer3111121.Add( self.m_panel722111121, 1, wx.EXPAND|wx.RIGHT, 15 )
		
		
		self.m_panel9911121.SetSizer( fgSizer3111121 )
		self.m_panel9911121.Layout()
		fgSizer3111121.Fit( self.m_panel9911121 )
		fgSizer2311111.Add( self.m_panel9911121, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4811111.SetSizer( fgSizer2311111 )
		self.m_panel4811111.Layout()
		fgSizer2311111.Fit( self.m_panel4811111 )
		bSizer6711111.Add( self.m_panel4811111, 1, wx.EXPAND, 15 )
		
		
		self.Stat_modeS.SetSizer( bSizer6711111 )
		self.Stat_modeS.Layout()
		bSizer6711111.Fit( self.Stat_modeS )
		self.m_notebook.AddPage( self.Stat_modeS, u"Stat ModeS", False )
		self.Param = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.Param.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.Param.SetBackgroundColour( wx.Colour( 204, 211, 227 ) )
		
		fgSizer13421 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer13421.SetFlexibleDirection( wx.BOTH )
		fgSizer13421.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer13511 = wx.FlexGridSizer( 15, 1, 0, 0 )
		fgSizer13511.SetFlexibleDirection( wx.BOTH )
		fgSizer13511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText674211 = wx.StaticText( self.Param, wx.ID_ANY, u"Informations Générales", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText674211.Wrap( -1 )
		self.m_staticText674211.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer13511.Add( self.m_staticText674211, 0, wx.TOP, 50 )
		
		fgSizer13721 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer13721.AddGrowableCol( 2 )
		fgSizer13721.SetFlexibleDirection( wx.BOTH )
		fgSizer13721.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText66621 = wx.StaticText( self.Param, wx.ID_ANY, u"Nom du radar", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText66621.Wrap( -1 )
		fgSizer13721.Add( self.m_staticText66621, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.NomRadar = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.NomRadar.SetMaxLength( 15 ) 
		fgSizer13721.Add( self.NomRadar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText66711 = wx.StaticText( self.Param, wx.ID_ANY, u"Acronyme", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66711.Wrap( -1 )
		fgSizer13721.Add( self.m_staticText66711, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.AcronymeRadar = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.AcronymeRadar.SetMaxLength( 4 ) 
		fgSizer13721.Add( self.AcronymeRadar, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer13721, 1, wx.EXPAND|wx.LEFT, 10 )
		
		fgSizer137112 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer137112.SetFlexibleDirection( wx.BOTH )
		fgSizer137112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText666112 = wx.StaticText( self.Param, wx.ID_ANY, u"Période de rotation (en secondes)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText666112.Wrap( -1 )
		fgSizer137112.Add( self.m_staticText666112, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.RadarPeriodeRotation = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.RadarPeriodeRotation.SetMaxLength( 2 ) 
		fgSizer137112.Add( self.RadarPeriodeRotation, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer137112, 1, wx.EXPAND|wx.LEFT, 10 )
		
		self.m_staticText67431 = wx.StaticText( self.Param, wx.ID_ANY, u"Diffusion Mode S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67431.Wrap( -1 )
		self.m_staticText67431.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer13511.Add( self.m_staticText67431, 0, wx.TOP, 50 )
		
		fgSizer13711121 = wx.FlexGridSizer( 2, 7, 0, 0 )
		fgSizer13711121.SetFlexibleDirection( wx.BOTH )
		fgSizer13711121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText66611121 = wx.StaticText( self.Param, wx.ID_ANY, u"Adresse MAC de diffusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66611121.Wrap( -1 )
		fgSizer13711121.Add( self.m_staticText66611121, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DiffModeSMACOctet1 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet1.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet1, 0, wx.ALL, 5 )
		
		self.DiffModeSMACOctet2 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet2.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet2, 0, wx.ALL, 5 )
		
		self.DiffModeSMACOctet3 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet3.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet3, 0, wx.ALL, 5 )
		
		self.DiffModeSMACOctet4 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet4.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet4, 0, wx.ALL, 5 )
		
		self.DiffModeSMACOctet5 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet5.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet5, 0, wx.ALL, 5 )
		
		self.DiffModeSMACOctet6 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSMACOctet6.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSMACOctet6, 0, wx.ALL, 5 )
		
		self.m_staticText666111111 = wx.StaticText( self.Param, wx.ID_ANY, u"Adresse LLC de diffusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText666111111.Wrap( -1 )
		fgSizer13711121.Add( self.m_staticText666111111, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DiffModeSLLC = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeSLLC.SetMaxLength( 2 ) 
		fgSizer13711121.Add( self.DiffModeSLLC, 0, wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer13711121, 1, wx.EXPAND|wx.LEFT, 10 )
		
		self.m_staticText674121 = wx.StaticText( self.Param, wx.ID_ANY, u"Diffusion Mode A/C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText674121.Wrap( -1 )
		self.m_staticText674121.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer13511.Add( self.m_staticText674121, 0, wx.TOP, 50 )
		
		fgSizer137111111 = wx.FlexGridSizer( 2, 7, 0, 0 )
		fgSizer137111111.SetFlexibleDirection( wx.BOTH )
		fgSizer137111111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText666111311 = wx.StaticText( self.Param, wx.ID_ANY, u"Adresse MAC de diffusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText666111311.Wrap( -1 )
		fgSizer137111111.Add( self.m_staticText666111311, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DiffModeACMACOctet1 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet1.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet1, 0, wx.ALL, 5 )
		
		self.DiffModeACMACOctet2 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet2.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet2, 0, wx.ALL, 5 )
		
		self.DiffModeACMACOctet3 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet3.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet3, 0, wx.ALL, 5 )
		
		self.DiffModeACMACOctet4 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet4.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet4, 0, wx.ALL, 5 )
		
		self.DiffModeACMACOctet5 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet5.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet5, 0, wx.ALL, 5 )
		
		self.DiffModeACMACOctet6 = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACMACOctet6.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACMACOctet6, 0, wx.ALL, 5 )
		
		self.m_staticText6661111211 = wx.StaticText( self.Param, wx.ID_ANY, u"Adresse LLC de diffusion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6661111211.Wrap( -1 )
		fgSizer137111111.Add( self.m_staticText6661111211, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DiffModeACLLC = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.DiffModeACLLC.SetMaxLength( 2 ) 
		fgSizer137111111.Add( self.DiffModeACLLC, 0, wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer137111111, 1, wx.EXPAND|wx.LEFT, 10 )
		
		self.m_staticText6741111 = wx.StaticText( self.Param, wx.ID_ANY, u"Balise de Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6741111.Wrap( -1 )
		self.m_staticText6741111.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer13511.Add( self.m_staticText6741111, 0, wx.TOP, 50 )
		
		fgSizer16311 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer16311.SetFlexibleDirection( wx.BOTH )
		fgSizer16311.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText69511 = wx.StaticText( self.Param, wx.ID_ANY, u"Azimut théorique (en epsilon)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69511.Wrap( -1 )
		fgSizer16311.Add( self.m_staticText69511, 1, wx.ALIGN_CENTER|wx.BOTTOM|wx.LEFT|wx.TOP, 0 )
		
		self.BaliseAzimutTheo = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaliseAzimutTheo.SetMaxLength( 4 ) 
		fgSizer16311.Add( self.BaliseAzimutTheo, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer16311, 1, wx.EXPAND|wx.LEFT, 10 )
		
		sbSizer221 = wx.StaticBoxSizer( wx.StaticBox( self.Param, wx.ID_ANY, u"Mode A/C" ), wx.HORIZONTAL )
		
		fgSizer15621 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer15621.AddGrowableCol( 2 )
		fgSizer15621.SetFlexibleDirection( wx.BOTH )
		fgSizer15621.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText69321 = wx.StaticText( self.Param, wx.ID_ANY, u"Code Mode A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69321.Wrap( -1 )
		fgSizer15621.Add( self.m_staticText69321, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.BaliseModeACModeA = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaliseModeACModeA.SetMaxLength( 4 ) 
		fgSizer15621.Add( self.BaliseModeACModeA, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticText69421 = wx.StaticText( self.Param, wx.ID_ANY, u"Mode C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69421.Wrap( -1 )
		fgSizer15621.Add( self.m_staticText69421, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 0 )
		
		self.BaliseModeACModeC = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.BaliseModeACModeC.SetMaxLength( 4 ) 
		fgSizer15621.Add( self.BaliseModeACModeC, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		sbSizer221.Add( fgSizer15621, 1, wx.EXPAND, 5 )
		
		
		fgSizer13511.Add( sbSizer221, 1, wx.EXPAND, 15 )
		
		sbSizer2111 = wx.StaticBoxSizer( wx.StaticBox( self.Param, wx.ID_ANY, u"Mode S" ), wx.HORIZONTAL )
		
		fgSizer156111 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer156111.AddGrowableCol( 2 )
		fgSizer156111.SetFlexibleDirection( wx.BOTH )
		fgSizer156111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText693121 = wx.StaticText( self.Param, wx.ID_ANY, u"Nom Mode S Balise 1 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText693121.Wrap( -1 )
		fgSizer156111.Add( self.m_staticText693121, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.Balise1ModeSNom = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Balise1ModeSNom.SetMaxLength( 8 ) 
		fgSizer156111.Add( self.Balise1ModeSNom, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticText694121 = wx.StaticText( self.Param, wx.ID_ANY, u"Mode C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText694121.Wrap( -1 )
		fgSizer156111.Add( self.m_staticText694121, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 0 )
		
		self.Balise1ModeSModeC = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.Balise1ModeSModeC.SetMaxLength( 4 ) 
		fgSizer156111.Add( self.Balise1ModeSModeC, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText6931111 = wx.StaticText( self.Param, wx.ID_ANY, u"Nom Mode S Balise 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6931111.Wrap( -1 )
		fgSizer156111.Add( self.m_staticText6931111, 0, wx.ALL, 5 )
		
		self.Balise2ModeSNom = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Balise2ModeSNom.SetMaxLength( 8 ) 
		fgSizer156111.Add( self.Balise2ModeSNom, 0, wx.ALL, 5 )
		
		self.m_staticText6941111 = wx.StaticText( self.Param, wx.ID_ANY, u"Mode C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6941111.Wrap( -1 )
		fgSizer156111.Add( self.m_staticText6941111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.Balise2ModeSModeC = wx.TextCtrl( self.Param, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.Balise2ModeSModeC.SetMaxLength( 4 ) 
		fgSizer156111.Add( self.Balise2ModeSModeC, 0, wx.ALL, 5 )
		
		
		sbSizer2111.Add( fgSizer156111, 1, wx.EXPAND, 5 )
		
		
		fgSizer13511.Add( sbSizer2111, 1, wx.EXPAND|wx.TOP, 15 )
		
		fgSizer49 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer49.AddGrowableCol( 0 )
		fgSizer49.SetFlexibleDirection( wx.BOTH )
		fgSizer49.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ButtonSauverParam = wx.Button( self.Param, wx.ID_ANY, u"Sauver", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.ButtonSauverParam, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ButtonCancelParam = wx.Button( self.Param, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer49.Add( self.ButtonCancelParam, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer13511.Add( fgSizer49, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		fgSizer13421.Add( fgSizer13511, 2, wx.ALL|wx.EXPAND, 15 )
		
		fgSizer13611 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer13611.AddGrowableRow( 0 )
		fgSizer13611.SetFlexibleDirection( wx.VERTICAL )
		fgSizer13611.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.ZoneAffichagePage = wx.StaticBitmap( self.Param, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 600,-1 ), wx.SUNKEN_BORDER )
		fgSizer13611.Add( self.ZoneAffichagePage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.ButtonChangePhoto = wx.Button( self.Param, wx.ID_ANY, u"Changer la photo", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13611.Add( self.ButtonChangePhoto, 0, wx.ALIGN_CENTER|wx.BOTTOM|wx.TOP, 10 )
		
		
		fgSizer13421.Add( fgSizer13611, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 25 )
		
		
		self.Param.SetSizer( fgSizer13421 )
		self.Param.Layout()
		fgSizer13421.Fit( self.Param )
		self.m_notebook.AddPage( self.Param, u"Paramétrage", False )
		self.CourbesStats = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.CourbesStats.Enable( False )
		self.CourbesStats.Hide()
		
		fgSizer134111 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer134111.AddGrowableCol( 0 )
		fgSizer134111.AddGrowableRow( 1 )
		fgSizer134111.SetFlexibleDirection( wx.BOTH )
		fgSizer134111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer19011 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer19011.AddGrowableCol( 0 )
		fgSizer19011.SetFlexibleDirection( wx.BOTH )
		fgSizer19011.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel49511 = wx.Panel( self.CourbesStats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel49511.SetBackgroundColour( wx.Colour( 204, 211, 227 ) )
		
		bSizer7111 = wx.BoxSizer( wx.VERTICAL )
		
		TypeCourbeAfficherChoices = [ u"Nombre de plots", u"Taux de charge par tour d'antenne", u"Taux de charge par secteur", u"Taux de charge par 3 secteurs", u"Période de rotation", u"Taux de détection All Call", u"Taux de détection Roll Call", u"Biais Radar", u"Temps d'indisponibilité" ]
		self.TypeCourbeAfficher = wx.RadioBox( self.m_panel49511, wx.ID_ANY, u"Type de courbe à afficher", wx.DefaultPosition, wx.DefaultSize, TypeCourbeAfficherChoices, 2, 0 )
		self.TypeCourbeAfficher.SetSelection( 0 )
		self.TypeCourbeAfficher.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7111.Add( self.TypeCourbeAfficher, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.m_panel49511.SetSizer( bSizer7111 )
		self.m_panel49511.Layout()
		bSizer7111.Fit( self.m_panel49511 )
		fgSizer19011.Add( self.m_panel49511, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel49611 = wx.Panel( self.CourbesStats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel49611.SetBackgroundColour( wx.Colour( 204, 211, 227 ) )
		
		fgSizer19211 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer19211.AddGrowableRow( 1 )
		fgSizer19211.SetFlexibleDirection( wx.BOTH )
		fgSizer19211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		ChoixPeriodeChoices = [ u"Par mois sur toute l'année", u"Par jour sur un mois", u"Par heure sur une journée" ]
		self.ChoixPeriode = wx.RadioBox( self.m_panel49611, wx.ID_ANY, u"Période", wx.DefaultPosition, wx.DefaultSize, ChoixPeriodeChoices, 1, wx.RA_SPECIFY_COLS )
		self.ChoixPeriode.SetSelection( 0 )
		self.ChoixPeriode.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer19211.Add( self.ChoixPeriode, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer22511 = wx.BoxSizer( wx.VERTICAL )
		
		AnneeChoices = [ u"Annee", u"2011", u"2010" ]
		self.Annee = wx.Choice( self.m_panel49611, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AnneeChoices, 0 )
		self.Annee.SetSelection( 0 )
		bSizer22511.Add( self.Annee, 0, wx.ALL, 5 )
		
		MoisChoices = [ u"Mois", u"Janvier", u"Février", u"Mars", u"Avril", u"Mai", u"Juin", u"Juillet", u"Aout", u"Septembre", u"Octobre", u"Novembre", u"Décembre" ]
		self.Mois = wx.Choice( self.m_panel49611, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, MoisChoices, 0 )
		self.Mois.SetSelection( 0 )
		bSizer22511.Add( self.Mois, 0, wx.ALL, 5 )
		
		JourChoices = [ u"Jour", u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31" ]
		self.Jour = wx.Choice( self.m_panel49611, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, JourChoices, 0 )
		self.Jour.SetSelection( 0 )
		bSizer22511.Add( self.Jour, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		fgSizer19211.Add( bSizer22511, 1, wx.EXPAND|wx.TOP, 30 )
		
		self.ButtonSaveGraphe = wx.Button( self.m_panel49611, wx.ID_ANY, u"Sauvegarder le graphe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonSaveGraphe.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer19211.Add( self.ButtonSaveGraphe, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.ButtonValidAffichCourbe = wx.Button( self.m_panel49611, wx.ID_ANY, u"Valider", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonValidAffichCourbe.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer19211.Add( self.ButtonValidAffichCourbe, 0, wx.ALL, 5 )
		
		
		self.m_panel49611.SetSizer( fgSizer19211 )
		self.m_panel49611.Layout()
		fgSizer19211.Fit( self.m_panel49611 )
		fgSizer19011.Add( self.m_panel49611, 1, wx.EXPAND, 0 )
		
		
		fgSizer134111.Add( fgSizer19011, 1, wx.EXPAND, 0 )
		
		self.PanelAffichageCourbe = wx.Panel( self.CourbesStats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.PanelAffichageCourbe.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		fgSizer134111.Add( self.PanelAffichageCourbe, 1, wx.EXPAND|wx.TOP, 5 )
		
		
		self.CourbesStats.SetSizer( fgSizer134111 )
		self.CourbesStats.Layout()
		fgSizer134111.Fit( self.CourbesStats )
		self.m_notebook.AddPage( self.CourbesStats, u"Courbes de stats", False )
		
		bSizer1.Add( self.m_notebook, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonFermerPageStatRadars.Bind( wx.EVT_BUTTON, self.FermerPageStatRadars )
		self.ButtonSauverParam.Bind( wx.EVT_BUTTON, self.SauverParam )
		self.ButtonCancelParam.Bind( wx.EVT_BUTTON, self.AnnulerParam )
		self.ButtonChangePhoto.Bind( wx.EVT_BUTTON, self.ChangerPhoto )
		self.ButtonSaveGraphe.Bind( wx.EVT_BUTTON, self.SauverGraphe )
		self.ButtonValidAffichCourbe.Bind( wx.EVT_BUTTON, self.AfficherCourbe )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FermerPageStatRadars( self, event ):
		event.Skip()
	
	def SauverParam( self, event ):
		event.Skip()
	
	def AnnulerParam( self, event ):
		event.Skip()
	
	def ChangerPhoto( self, event ):
		event.Skip()
	
	def SauverGraphe( self, event ):
		event.Skip()
	
	def AfficherCourbe( self, event ):
		event.Skip()
	

###########################################################################
## Class PageIncompatibiliteCoupureRadar
###########################################################################

class PageIncompatibiliteCoupureRadar ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 715,687 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelMenuBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,1024 ), wx.TAB_TRAVERSAL )
		self.m_panelMenuBar.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ButtonFermerCoupureRadarPage = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonFermerCoupureRadarPage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonFermerCoupureRadarPage, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, u"INCOMPATIBILITES DES COUPURES RADARS", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer85.Add( self.m_staticHeurePC, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.ButtonModifierCoupureRadarPage = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"Modifier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonModifierCoupureRadarPage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonModifierCoupureRadarPage, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panelMenuBar.SetSizer( bSizer85 )
		self.m_panelMenuBar.Layout()
		bSizer84.Add( self.m_panelMenuBar, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.ZoneAffichPageCoupureRadarPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		self.ZoneAffichagePage = wx.html.HtmlWindow( self.ZoneAffichPageCoupureRadarPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		bSizer87.Add( self.ZoneAffichagePage, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.ZoneAffichPageCoupureRadarPanel.SetSizer( bSizer87 )
		self.ZoneAffichPageCoupureRadarPanel.Layout()
		bSizer87.Fit( self.ZoneAffichPageCoupureRadarPanel )
		bSizer84.Add( self.ZoneAffichPageCoupureRadarPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonFermerCoupureRadarPage.Bind( wx.EVT_BUTTON, self.IncompatibiliteCoupuresRadarsFermer )
		self.ButtonModifierCoupureRadarPage.Bind( wx.EVT_BUTTON, self.IncompatibiliteCoupuresRadarsPageModifier )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def IncompatibiliteCoupuresRadarsFermer( self, event ):
		event.Skip()
	
	def IncompatibiliteCoupuresRadarsPageModifier( self, event ):
		event.Skip()
	

###########################################################################
## Class PagePreferences
###########################################################################

class PagePreferences ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 644,645 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel30.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ButtonFermerPreferencesPage = wx.Button( self.m_panel30, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonFermerPreferencesPage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonFermerPreferencesPage, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panel30, wx.ID_ANY, u"PREFERENCES", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer85.Add( self.m_staticHeurePC, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.ButtonSauverPreferences = wx.Button( self.m_panel30, wx.ID_ANY, u"Sauver", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonSauverPreferences.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonSauverPreferences, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panel30.SetSizer( bSizer85 )
		self.m_panel30.Layout()
		bSizer85.Fit( self.m_panel30 )
		bSizer84.Add( self.m_panel30, 0, wx.EXPAND, 5 )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer15 = wx.FlexGridSizer( 2, 4, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		
		bSizer87.Add( fgSizer15, 0, wx.EXPAND, 5 )
		
		self.m_staticText80 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"BORNES DE DECLENCHEMENT DES ALARMES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		self.m_staticText80.SetFont( wx.Font( 12, 74, 90, 92, True, wx.EmptyString ) )
		
		bSizer87.Add( self.m_staticText80, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP, 10 )
		
		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel31 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel31.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
		
		bSizer49.Add( self.m_panel31, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer16 = wx.FlexGridSizer( 7, 4, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText82 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Nbr d'erreurs de fin de bloc", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText82.Wrap( -1 )
		self.m_staticText82.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText82, 0, wx.ALL, 5 )
		
		self.m_staticText83 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )
		self.m_staticText83.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText83, 0, wx.ALL, 5 )
		
		self.m_textCtrlNbErrorFinBloc = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlNbErrorFinBloc.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlNbErrorFinBloc, 0, wx.ALL, 5 )
		
		self.m_staticText836 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText836.Wrap( -1 )
		self.m_staticText836.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText836.Enable( False )
		self.m_staticText836.Hide()
		
		fgSizer16.Add( self.m_staticText836, 0, wx.ALL, 5 )
		
		self.m_staticText821 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Nbr d'erreurs de syntaxe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText821.Wrap( -1 )
		self.m_staticText821.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText821, 0, wx.ALL, 5 )
		
		self.m_staticText831 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText831.Wrap( -1 )
		self.m_staticText831.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText831, 0, wx.ALL, 5 )
		
		self.m_textCtrlNbErrorSynt = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlNbErrorSynt.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlNbErrorSynt, 0, wx.ALL, 5 )
		
		self.m_staticText8312 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8312.Wrap( -1 )
		self.m_staticText8312.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText8312.Hide()
		
		fgSizer16.Add( self.m_staticText8312, 0, wx.ALL, 5 )
		
		self.m_staticText822 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Nbr d'absences du champ heure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText822.Wrap( -1 )
		self.m_staticText822.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText822, 0, wx.ALL, 5 )
		
		self.m_staticText832 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText832.Wrap( -1 )
		self.m_staticText832.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText832, 0, wx.ALL, 5 )
		
		self.m_textCtrlNbNoHour = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlNbNoHour.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlNbNoHour, 0, wx.ALL, 5 )
		
		self.m_staticText8313 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8313.Wrap( -1 )
		self.m_staticText8313.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText8313.Hide()
		
		fgSizer16.Add( self.m_staticText8313, 0, wx.ALL, 5 )
		
		self.m_staticText823 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Nbr d'absences du champ Top Nord", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText823.Wrap( -1 )
		self.m_staticText823.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText823, 0, wx.ALL, 5 )
		
		self.m_staticText833 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText833.Wrap( -1 )
		self.m_staticText833.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText833, 0, wx.ALL, 5 )
		
		self.m_textCtrNbNoTopNorth = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrNbNoTopNorth.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrNbNoTopNorth, 0, wx.ALL, 5 )
		
		self.m_staticText8314 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8314.Wrap( -1 )
		self.m_staticText8314.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText8314.Hide()
		
		fgSizer16.Add( self.m_staticText8314, 0, wx.ALL, 5 )
		
		self.m_staticText824 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Nbr de décalages azimutaux", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText824.Wrap( -1 )
		self.m_staticText824.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText824, 0, wx.ALL, 5 )
		
		self.m_staticText834 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText834.Wrap( -1 )
		self.m_staticText834.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText834, 0, wx.ALL, 5 )
		
		self.m_textCtrlNbDecalAzim = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlNbDecalAzim.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlNbDecalAzim, 0, wx.ALL, 5 )
		
		self.m_staticText8315 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8315.Wrap( -1 )
		self.m_staticText8315.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText8315.Hide()
		
		fgSizer16.Add( self.m_staticText8315, 0, wx.ALL, 5 )
		
		self.m_staticText74 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Tolérances de la période de rotation", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText74.Wrap( -1 )
		self.m_staticText74.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText74, 0, wx.ALL, 5 )
		
		self.m_staticText75 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )
		self.m_staticText75.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText75, 0, wx.ALL, 5 )
		
		self.m_textCtrlTolPerRot = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTolPerRot.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlTolPerRot, 0, wx.ALL, 5 )
		
		self.m_staticText76 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )
		self.m_staticText76.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText76, 0, wx.ALL, 5 )
		
		self.m_staticText77 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Tolérances du décalage azimutal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		self.m_staticText77.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText77, 0, wx.ALL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.DefaultSize, 0|wx.CLIP_CHILDREN )
		self.m_staticText78.Wrap( -1 )
		self.m_staticText78.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText78, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_textCtrlTolDecalAzim = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTolDecalAzim.SetMaxLength( 2 ) 
		fgSizer16.Add( self.m_textCtrlTolDecalAzim, 0, wx.ALL, 5 )
		
		self.m_staticText79 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Epsilon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )
		self.m_staticText79.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer16.Add( self.m_staticText79, 0, wx.ALL, 5 )
		
		
		bSizer49.Add( fgSizer16, 1, wx.ALL|wx.TOP, 5 )
		
		
		bSizer87.Add( bSizer49, 0, wx.TOP|wx.EXPAND, 10 )
		
		bSizer491 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel311 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.Size( 10,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel311.SetBackgroundColour( wx.Colour( 94, 207, 65 ) )
		
		bSizer491.Add( self.m_panel311, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer161 = wx.FlexGridSizer( 9, 4, 0, 0 )
		fgSizer161.SetFlexibleDirection( wx.BOTH )
		fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText825 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de plots fantomes", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText825.Wrap( -1 )
		self.m_staticText825.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText825, 0, wx.ALL, 5 )
		
		self.m_staticText835 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText835.Wrap( -1 )
		self.m_staticText835.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText835, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_textCtrlTxGhostPlot = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxGhostPlot.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxGhostPlot, 0, wx.ALL, 5 )
		
		self.m_staticText8351 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8351.Wrap( -1 )
		self.m_staticText8351.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8351, 0, wx.ALL, 5 )
		
		self.m_staticText8211 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de doublons", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8211.Wrap( -1 )
		self.m_staticText8211.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8211, 0, wx.ALL, 5 )
		
		self.m_staticText8311 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8311.Wrap( -1 )
		self.m_staticText8311.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8311, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxDoublon = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxDoublon.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxDoublon, 0, wx.ALL, 5 )
		
		self.m_staticText83511 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83511.Wrap( -1 )
		self.m_staticText83511.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83511, 0, wx.ALL, 5 )
		
		self.m_staticText8221 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de plots douteux", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8221.Wrap( -1 )
		self.m_staticText8221.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8221, 0, wx.ALL, 5 )
		
		self.m_staticText8321 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8321.Wrap( -1 )
		self.m_staticText8321.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8321, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxDoubtPlot = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxDoubtPlot.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxDoubtPlot, 0, wx.ALL, 5 )
		
		self.m_staticText83512 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83512.Wrap( -1 )
		self.m_staticText83512.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83512, 0, wx.ALL, 5 )
		
		self.m_staticText8231 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de Garbles Mode A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8231.Wrap( -1 )
		self.m_staticText8231.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8231, 0, wx.ALL, 5 )
		
		self.m_staticText8331 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8331.Wrap( -1 )
		self.m_staticText8331.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8331, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxGarbleModeA = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxGarbleModeA.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxGarbleModeA, 0, wx.ALL, 5 )
		
		self.m_staticText83513 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83513.Wrap( -1 )
		self.m_staticText83513.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83513, 0, wx.ALL, 5 )
		
		self.m_staticText8241 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de Garbles Mode C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8241.Wrap( -1 )
		self.m_staticText8241.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8241, 0, wx.ALL, 5 )
		
		self.m_staticText8341 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8341.Wrap( -1 )
		self.m_staticText8341.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText8341, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxGarbleModeC = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxGarbleModeC.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxGarbleModeC, 0, wx.ALL, 5 )
		
		self.m_staticText835144 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText835144.Wrap( -1 )
		self.m_staticText835144.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText835144, 0, wx.ALL, 5 )
		
		self.m_staticText82411 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux d'Invalides Mode A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82411.Wrap( -1 )
		self.m_staticText82411.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText82411, 0, wx.ALL, 5 )
		
		self.m_staticText83414 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83414.Wrap( -1 )
		self.m_staticText83414.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83414, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxInvalidesModeA = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxInvalidesModeA.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxInvalidesModeA, 0, wx.ALL, 5 )
		
		self.m_staticText83514 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83514.Wrap( -1 )
		self.m_staticText83514.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83514, 0, wx.ALL, 5 )
		
		self.m_staticText824111 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux d'Invalides Mode C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText824111.Wrap( -1 )
		self.m_staticText824111.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText824111, 0, wx.ALL, 5 )
		
		self.m_staticText83413 = wx.StaticText( self.m_panel34, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83413.Wrap( -1 )
		self.m_staticText83413.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83413, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxInvalidesModeC = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxInvalidesModeC.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxInvalidesModeC, 0, wx.ALL, 5 )
		
		self.m_staticText835142 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText835142.Wrap( -1 )
		self.m_staticText835142.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText835142, 0, wx.ALL, 5 )
		
		self.m_staticText824112 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de détection Mode A/C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText824112.Wrap( -1 )
		self.m_staticText824112.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText824112, 0, wx.ALL, 5 )
		
		self.m_staticText83411 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83411.Wrap( -1 )
		self.m_staticText83411.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83411, 0, wx.ALL, 5 )
		
		self.m_textCtrlTxDetectionModeAC = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlTxDetectionModeAC.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlTxDetectionModeAC, 0, wx.ALL, 5 )
		
		self.m_staticText835143 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText835143.Wrap( -1 )
		self.m_staticText835143.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText835143, 0, wx.ALL, 5 )
		
		self.m_staticText824113 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Taux de détection Mode S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText824113.Wrap( -1 )
		self.m_staticText824113.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText824113, 0, wx.ALL, 5 )
		
		self.m_staticText83412 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83412.Wrap( -1 )
		self.m_staticText83412.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText83412, 0, wx.ALL, 5 )
		
		self.m_textCtrlModeS = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_textCtrlModeS.SetMaxLength( 2 ) 
		fgSizer161.Add( self.m_textCtrlModeS, 0, wx.ALL, 5 )
		
		self.m_staticText835141 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText835141.Wrap( -1 )
		self.m_staticText835141.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer161.Add( self.m_staticText835141, 0, wx.ALL, 5 )
		
		
		bSizer491.Add( fgSizer161, 1, wx.ALL, 5 )
		
		
		bSizer87.Add( bSizer491, 0, wx.TOP|wx.EXPAND, 10 )
		
		
		self.m_panel34.SetSizer( bSizer87 )
		self.m_panel34.Layout()
		bSizer87.Fit( self.m_panel34 )
		bSizer84.Add( self.m_panel34, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonFermerPreferencesPage.Bind( wx.EVT_BUTTON, self.FermerPreferencesPage )
		self.ButtonSauverPreferences.Bind( wx.EVT_BUTTON, self.SauverPreferences )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FermerPreferencesPage( self, event ):
		event.Skip()
	
	def SauverPreferences( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogConfirm
###########################################################################

class DialogConfirm ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Confirmation", pos = wx.DefaultPosition, size = wx.Size( 467,147 ), style = wx.CAPTION|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText226 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Voulez vous vraiment sauvegarder les préférences dans le fichier config.ini ?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText226.Wrap( 250 )
		self.m_staticText226.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText226.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer55.Add( self.m_staticText226, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self.m_panel34, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self.m_panel34, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();
		
		bSizer55.Add( m_sdbSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( bSizer55 )
		self.m_panel34.Layout()
		bSizer55.Fit( self.m_panel34 )
		bSizer54.Add( self.m_panel34, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer54 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.CancelButtonSavePref )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.SaveOnFilePref )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CancelButtonSavePref( self, event ):
		event.Skip()
	
	def SaveOnFilePref( self, event ):
		event.Skip()
	

###########################################################################
## Class PageHelp
###########################################################################

class PageHelp ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 715,687 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelMenuBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,1024 ), wx.TAB_TRAVERSAL )
		self.m_panelMenuBar.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ButtonHelpFermer = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonHelpFermer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonHelpFermer, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, u"AIDE", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer85.Add( self.m_staticHeurePC, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.ButtonModifHelp = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"Modifier", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonModifHelp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonModifHelp, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panelMenuBar.SetSizer( bSizer85 )
		self.m_panelMenuBar.Layout()
		bSizer84.Add( self.m_panelMenuBar, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		self.ZoneAffichagePage = wx.html.HtmlWindow( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		bSizer87.Add( self.ZoneAffichagePage, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( bSizer87 )
		self.m_panel34.Layout()
		bSizer87.Fit( self.m_panel34 )
		bSizer84.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonHelpFermer.Bind( wx.EVT_BUTTON, self.HelpFermer )
		self.ButtonModifHelp.Bind( wx.EVT_BUTTON, self.PageAideModifier )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def HelpFermer( self, event ):
		event.Skip()
	
	def PageAideModifier( self, event ):
		event.Skip()
	

###########################################################################
## Class PageHisto
###########################################################################

class PageHisto ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 729,554 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelMenuBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,1024 ), wx.TAB_TRAVERSAL )
		self.m_panelMenuBar.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ButtonPageHistoFermer = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonPageHistoFermer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonPageHistoFermer, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, u"HISTORIQUE DES EVENEMENTS", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer85.Add( self.m_staticHeurePC, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.ButtonPageFiltresOuvrir = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"Filtres", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonPageFiltresOuvrir.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonPageFiltresOuvrir, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panelMenuBar.SetSizer( bSizer85 )
		self.m_panelMenuBar.Layout()
		bSizer84.Add( self.m_panelMenuBar, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer87 = wx.BoxSizer( wx.VERTICAL )
		
		self.ZoneAffichHisto = wx.richtext.RichTextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		bSizer87.Add( self.ZoneAffichHisto, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel34.SetSizer( bSizer87 )
		self.m_panel34.Layout()
		bSizer87.Fit( self.m_panel34 )
		bSizer84.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonPageHistoFermer.Bind( wx.EVT_BUTTON, self.PageHistoFermer )
		self.ButtonPageFiltresOuvrir.Bind( wx.EVT_BUTTON, self.PageFiltreOuvrir )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PageHistoFermer( self, event ):
		event.Skip()
	
	def PageFiltreOuvrir( self, event ):
		event.Skip()
	

###########################################################################
## Class PageFiltre
###########################################################################

class PageFiltre ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 410,366 ), style = wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelMenuBar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1280,1024 ), wx.TAB_TRAVERSAL )
		self.m_panelMenuBar.SetBackgroundColour( wx.Colour( 58, 110, 165 ) )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ButtonPageHistoFermer = wx.Button( self.m_panelMenuBar, wx.ID_ANY, u"FERMER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ButtonPageHistoFermer.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.ButtonPageHistoFermer, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticHeurePC = wx.StaticText( self.m_panelMenuBar, wx.ID_ANY, u"FILTRER L'HISTORIQUE", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticHeurePC.Wrap( -1 )
		self.m_staticHeurePC.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticHeurePC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer85.Add( self.m_staticHeurePC, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		
		self.m_panelMenuBar.SetSizer( bSizer85 )
		self.m_panelMenuBar.Layout()
		bSizer84.Add( self.m_panelMenuBar, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer328 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer328.AddGrowableCol( 0 )
		fgSizer328.AddGrowableCol( 1 )
		fgSizer328.SetFlexibleDirection( wx.BOTH )
		fgSizer328.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer258 = wx.BoxSizer( wx.VERTICAL )
		
		self.ChoixFiltreRadar = wx.CheckBox( self.m_panel34, wx.ID_ANY, u"Par Radar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer258.Add( self.ChoixFiltreRadar, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		ListChoixFiltreRadarChoices = [u"Avranches", u"Bertem", u"Boulognes", u"Chaumont", u"Coubron", u"Grand-Ballon", u"Nevers", u"Palaiseau", u"Tours", u"Roissy"]
		self.ListChoixFiltreRadar = wx.CheckListBox( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ListChoixFiltreRadarChoices, wx.LB_MULTIPLE|wx.LB_SORT )
		bSizer258.Add( self.ListChoixFiltreRadar, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.ButtonToutCocher = wx.Button( self.m_panel34, wx.ID_ANY, u"Tout Cocher", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer258.Add( self.ButtonToutCocher, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ButtonToutDecocher = wx.Button( self.m_panel34, wx.ID_ANY, u"Tout Décocher", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer258.Add( self.ButtonToutDecocher, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer328.Add( bSizer258, 1, wx.EXPAND, 5 )
		
		bSizer259 = wx.BoxSizer( wx.VERTICAL )
		
		self.ChoixFiltreMode = wx.CheckBox( self.m_panel34, wx.ID_ANY, u"Par Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer259.Add( self.ChoixFiltreMode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		ListChoixFiltreModeChoices = [u"Mode AC", u"Mode S"]
		self.ListChoixFiltreMode = wx.CheckListBox( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ListChoixFiltreModeChoices, wx.LB_MULTIPLE|wx.LB_SORT )
		bSizer259.Add( self.ListChoixFiltreMode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		fgSizer329 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer329.AddGrowableCol( 0 )
		fgSizer329.AddGrowableRow( 0 )
		fgSizer329.SetFlexibleDirection( wx.BOTH )
		fgSizer329.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ButtonValidFiltres = wx.Button( self.m_panel34, wx.ID_ANY, u"Valider", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer329.Add( self.ButtonValidFiltres, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer259.Add( fgSizer329, 1, wx.EXPAND, 5 )
		
		
		fgSizer328.Add( bSizer259, 1, wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( fgSizer328 )
		self.m_panel34.Layout()
		fgSizer328.Fit( self.m_panel34 )
		bSizer84.Add( self.m_panel34, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer84 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ButtonPageHistoFermer.Bind( wx.EVT_BUTTON, self.PageFiltresFermer )
		self.ButtonToutCocher.Bind( wx.EVT_BUTTON, self.ToutCocherFiltreRadar )
		self.ButtonToutDecocher.Bind( wx.EVT_BUTTON, self.ToutDecocherFiltreRadar )
		self.ButtonValidFiltres.Bind( wx.EVT_BUTTON, self.ValiderFiltre )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PageFiltresFermer( self, event ):
		event.Skip()
	
	def ToutCocherFiltreRadar( self, event ):
		event.Skip()
	
	def ToutDecocherFiltreRadar( self, event ):
		event.Skip()
	
	def ValiderFiltre( self, event ):
		event.Skip()
	

###########################################################################
## Class ChargerFichier
###########################################################################

class ChargerFichier ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ouvrir...", pos = wx.DefaultPosition, size = wx.Size( 533,129 ), style = wx.CAPTION|wx.FRAME_FLOAT_ON_PARENT|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer18 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer18.AddGrowableRow( 1 )
		fgSizer18.SetFlexibleDirection( wx.VERTICAL )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.SelectionFichier = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		fgSizer18.Add( self.SelectionFichier, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		self.m_sdbSizer3Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer3.AddButton( self.m_sdbSizer3Cancel )
		m_sdbSizer3.Realize();
		
		fgSizer18.Add( m_sdbSizer3, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.BOTTOM, 10 )
		
		
		self.SetSizer( fgSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer3Cancel.Bind( wx.EVT_BUTTON, self.ButtonCancelChargerFichier )
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.ButtonOKChargerFichier )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ButtonCancelChargerFichier( self, event ):
		event.Skip()
	
	def ButtonOKChargerFichier( self, event ):
		event.Skip()
