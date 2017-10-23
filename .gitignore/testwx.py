import wx
import wx.lib.scrolledpanel

class GUI(wx.Frame):

    def __init__(self,parent,id,title):
        #First retrieve the screen size of the device
        screenSize = wx.DisplaySize()
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]

        #Create a frame
        wx.Frame.__init__(self,parent,id,title,size=screenSize, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        panel1 = wx.Panel(self,size=(screenWidth,28), pos=(0,0), style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FDDF99')
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,400), pos=(0,28), style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')


        button1 = wx.Button(panel2,label="Button 1",pos=(0,50),size=(450,50))
        button2 = wx.Button(panel2,label="Button 2",pos=(0,100), size=(450,50))
        button3 = wx.Button(panel2,label="Button 3",pos=(0,150),size=(450,50))
        button4 = wx.Button(panel2,label="Button 4",pos=(0,200), size=(450,50))
        button5 = wx.Button(panel2,label="Button 5",pos=(0,250),size=(450,50))
        button6 = wx.Button(panel2,label="Button 6",pos=(0,300), size=(450,50))
        button7 = wx.Button(panel2,label="Button 7",pos=(0,350), size=(450,50))
        button8 = wx.Button(panel2,label="Button 8",pos=(0,400), size=(450,50))
        button9 = wx.Button(panel2,label="Button 9",pos=(0,450),size=(450,50))
        button10 = wx.Button(panel2,label="Button 10",pos=(0,500), size=(450,50))
        button11 = wx.Button(panel2,label="Button 11",pos=(0,550),size=(450,50))
        button12 = wx.Button(panel2,label="Button 12",pos=(0,600), size=(450,50))
        button13 = wx.Button(panel2,label="Button 13",pos=(0,650),size=(450,50))
        button14 = wx.Button(panel2,label="Button 14",pos=(0,700), size=(450,50))
        button15 = wx.Button(panel2,label="Button 15",pos=(0,750), size=(450,50))
        button16 = wx.Button(panel2,label="Button 16",pos=(0,800), size=(450,50))



        bSizer = wx.BoxSizer( wx.VERTICAL )
        bSizer.Add( button1, 0, wx.ALL, 5 )
        bSizer.Add( button2, 0, wx.ALL, 5 )
        bSizer.Add( button3, 0, wx.ALL, 5 )
        bSizer.Add( button4, 0, wx.ALL, 5 )
        bSizer.Add( button5, 0, wx.ALL, 5 )
        bSizer.Add( button6, 0, wx.ALL, 5 )
        bSizer.Add( button7, 0, wx.ALL, 5 )
        bSizer.Add( button8, 0, wx.ALL, 5 )
        bSizer.Add( button9, 0, wx.ALL, 5 )
        bSizer.Add( button10, 0, wx.ALL, 5 )
        bSizer.Add( button11, 0, wx.ALL, 5 )
        bSizer.Add( button12, 0, wx.ALL, 5 )
        bSizer.Add( button13, 0, wx.ALL, 5 )
        bSizer.Add( button14, 0, wx.ALL, 5 )
        bSizer.Add( button15, 0, wx.ALL, 5 )
        bSizer.Add( button16, 0, wx.ALL, 5 )
        panel2.SetSizer( bSizer )




if __name__=='__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()
