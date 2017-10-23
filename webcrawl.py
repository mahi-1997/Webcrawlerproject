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

        panel1 = wx.Panel(self,size=(screenWidth,120), pos=(0,0), style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FDDF99')
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,screenHeight-150), pos=(0,120), style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        
        x=10
        y=10
        i=0
        bSizer = wx.BoxSizer( wx.VERTICAL )
        for i in range(50):
            lb="s"+str(i)
            lb=wx.StaticText(panel2 ,-1, "Hello  ..."+str(i), (x,y))
            y=y+20
            bSizer.Add( lb, 0, wx.ALL, 10 )
            panel2.SetSizer( bSizer )
       

if __name__=='__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="WebCrawler Sim")
    frame.Show()
    app.MainLoop()
