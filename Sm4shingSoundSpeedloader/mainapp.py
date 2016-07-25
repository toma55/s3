import wx
import sys
import os #mkdir path.exists listdir
import shutil #copy

from collections import defaultdict
from Initialization import StageNameInfo
from Initialization import NameLookup
from Initialization import wd
from Initialization import LevelNames



#############################################################################

class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.SetSizer( bSizer1 )
        self.Layout()
        self.SetTitle("Sm4shing Sound Speedloader")
        self.panelOne = panel_one(self)
        self.panelTwo = panel_two(self)
        self.panelTwo.Hide()
        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


class panel_one ( wx.Panel ):

    def __init__( self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.TAB_TRAVERSAL )
        self.parent = parent
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        #Backgroun image
        image = wx.Image('img\maxresdefault.jpg', wx.BITMAP_TYPE_ANY)
        imageBitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(image))


        #Battlefield / Big Battlefield
        pic = wx.Image("img\Stage Icons\stage_10_battlefield_f.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(100,150))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Battlefield / Big Battlefield':self.changeLevel(evt, temp), ibutton )


        #Final Destination
        pic = wx.Image("img\Stage Icons\stage_10_end_f.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(300,150))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Final Destination':self.changeLevel(evt, temp), ibutton )


        #Town and City
        pic = wx.Image("img\Stage Icons\stage_10_village2.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(500,150))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Town and City':self.changeLevel(evt, temp), ibutton )


        #Smashville
        pic = wx.Image("img\Stage Icons\stage_10_xvillage.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(700,150))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Smashville':self.changeLevel(evt, temp), ibutton )


        #Duck Hunt
        pic = wx.Image("img\Stage Icons\stage_10_duckhunt.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(100,320))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Duck Hunt':self.changeLevel(evt, temp), ibutton )


        #Dream Land 64
        pic = wx.Image("img\Stage Icons\stage_10_pupupuland_64_f.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(300,320))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Dream Land 64':self.changeLevel(evt, temp), ibutton )


        #Lylat Cruise
        pic = wx.Image("img\Stage Icons\stage_10_xstarfox.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(500,320))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Lylat Cruise':self.changeLevel(evt, temp), ibutton )


        #Main Menu
        pic = wx.Image("img\Stage Icons\stage_10_menumusic.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        ibutton=wx.BitmapButton(imageBitmap, -1, pic, pos=(700,320))
        self.Bind(wx.EVT_BUTTON, lambda evt, temp='Main Menu':self.changeLevel(evt, temp), ibutton )



    def __del__( self ):
        pass


    def LoadPanel2Info(self, label):
        templist = self.parent.panelTwo.list

        templist.ClearAll()
        templist.InsertColumn(0, 'Level Track', width = 400) 
        templist.InsertColumn(1, 'Custom?', width = 80) 
        templist.InsertColumn(2, 'Custom Track', width = 320)
        
        for trackname in StageNameInfo[label]:
            self.parent.panelTwo.list.Append(trackname)


############Core Function##########################
    def changeLevel(self, event, label):
        self.parent.SetTitle(label)
        self.Hide()
        self.parent.panelTwo.Show()

        self.LoadPanel2Info( label)











class panel_two ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.TAB_TRAVERSAL )
     
        ############ Back Button ############   
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button2, 0, wx.ALL, 5 )
        self.SetSizer( bSizer5 )
        self.Layout()
        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.goBack )
        self.parent = parent
        

        ############  Create List ############ 
        self.list = wx.ListCtrl(self, -1, size=(800,600), style = wx.LC_REPORT)
        self.list.Center()

        self.list.Bind(wx.EVT_LEFT_DCLICK, self.LoadCustomSong_FileDialog)
        #self.list.Bind(wx.EVT_LEFT_DCLICK, self.LoadCustomSong_ChoiceDialog)


    def __del__( self ):
        pass

    #Buttons to handle all functionality
    def goBack( self, event ):
        if self.IsShown():
            self.parent.SetTitle("Sm4shing Sound Speedloader")
            self.parent.panelOne.Show()
            self.Hide()
            #load StageNameInfo into profile at working directory (wd) path
            file = open(wd + '\myfile.dat', 'w+')
            for lname in LevelNames:
                file.write('$' + lname + '\n')
                for tname in StageNameInfo[lname]:
                    file.write(tname[0] + '~@~')
                    file.write(tname[1] + '~~@')
                    file.write(tname[2] + '\n')
            file.close()



#Wii U Smash Bros 4 Music Path
# 0005000010144F00\sound\bgm

    def LoadCustomSong_FileDialog(self, event):
       
        #Get track name to be overwritten
        track = self.list.GetItemText(self.list.GetFocusedItem())
        
        #Get RAW Trake name
        rawTrack = NameLookup[track]
        

        
        ##################  User Double-Clicks a track name ##################
        wildcard = "NUS3BANK file (*.NUS3BANK)|*.NUS3BANK|"        \
                   "All files (*.*)|*.*"        
        
        #Create FileDialog for choosing NUS3BANK file
        dlg = wx.FileDialog(
            self, message="Choose a NUS3BANK file",
            defaultDir='.\NUS3BANK', 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.CHANGE_DIR
            )

        #NUS3BANK file was chosen
        if dlg.ShowModal() == wx.ID_OK:
            trackpath = dlg.GetPath()
            customtrackname = dlg.GetFilename()

            dlg.Destroy()
 
                    
            ##################  User chose a custom track ##################
            destination = wd + r'\0005000010144F00\sound\bgm\\'
            #Track us copied from A to B
            if not os.path.exists(destination):
                os.makedirs(destination)
         
            shutil.copy2(trackpath, destination + rawTrack + '.nus3bank')
            

            #Update StageNameInfo with custom track info
            level = self.parent.GetTitle()
            
            for index, trackname in enumerate(StageNameInfo[level]):
                if trackname[0] == track:
                    StageNameInfo[level][index] = (track, 'Y', customtrackname)


            self.parent.panelOne.LoadPanel2Info(level)

        #User canceled their selection
        else:
            dlg.Destroy()
       
        
    def LoadCustomSong_ChoiceDialog(self, event):

        #Get list of songs from the NUS3BANK music folder
        songlist_ext = os.listdir('.\NUS3BANK')
        #List for the text box with extension removed
        songlist = []
        for name in songlist_ext:
            songlist.append(name[:-9])



        #Create Choice Dialog
        dlg = wx.SingleChoiceDialog(
                self, 'Choose a custom track:', 'NUS3BANK Song List',
                songlist, 
                wx.CHOICEDLG_STYLE
                )

        if dlg.ShowModal() == wx.ID_OK:
            self.log.WriteText('You selected: %s\n' % dlg.GetStringSelection())

        dlg.Destroy()



        None
        







##############################################################################







#######  Main Loop ########
def main():
    app = wx.App()
    window = MainFrame(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()