import wx


def CreateButton(name, panelObj, pos=(0,0)):
    pic = wx.Image(name, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    ibutton=wx.BitmapButton(panelObj, -1, pic, pos)

    return ibutton


def OpenTrackList(name):
    box = wx.List