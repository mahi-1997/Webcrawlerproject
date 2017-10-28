#Program to populate table i.e. grid
import wx
 
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "List Control Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.index = 0
 
        self.list_ctrl = wx.ListCtrl(panel, size=(-1,600),
                         style=wx.LC_REPORT
                         |wx.BORDER_SUNKEN
                         )
        self.list_ctrl.InsertColumn(0, 'parent url', width=560)
        self.list_ctrl.InsertColumn(1, 'linked url', width=560)
        self.list_ctrl.InsertColumn(2, 'time', width=165)
 
        btn = wx.Button(panel, label="Add Line")
        #btn2 = wx.Button(panel, label="Get Data")
        btn3 = wx.Button(panel, label="Crawl")
        btn.Bind(wx.EVT_BUTTON, self.add_line)
        #btn2.Bind(wx.EVT_BUTTON, self.get_data)
        btn3.Bind(wx.EVT_BUTTON, self.refresh_data)

        #############################################
        #self.button = wx.Button(panel1, label="Crawl")
        self.lblname = wx.StaticText(panel, label="URL:")
        self.editname = wx.TextCtrl(panel, size=(600, -1))
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer1.AddStretchSpacer(250) 
        bSizer1.Add( self.lblname, 0, wx.ALIGN_RIGHT, 20)
        bSizer1.Add( self.editname, 0, wx.ALIGN_RIGHT, 20)
        bSizer1.Add( btn3, 0, wx.ALIGN_RIGHT, 20)
        #panel.SetSizer(bSizer1)
        #############################################
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(bSizer1, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        #sizer.Add(btn2, 0, wx.ALL|wx.CENTER, 5)
        #sizer.Add(btn3, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
    def add_line(self, event):
        line = "Line %s" % self.index
        self.list_ctrl.InsertStringItem(self.index, line)
        self.list_ctrl.SetStringItem(self.index, 1, "01/19/2010")
        self.list_ctrl.SetStringItem(self.index, 2, "USA")
        self.index += 1
 
    def get_data(self, event):
        count = self.list_ctrl.GetItemCount()
        cols = self.list_ctrl.GetColumnCount()
        for row in range(count):
            for col in range(cols):
                item = self.list_ctrl.GetItem(itemId=row, col=col)
                print(item.GetText())
    ######################################
    def refresh_data(self, event):
        print(self.editname.GetValue())

        while(self.index!=0):
            self.list_ctrl.DeleteItem(self.index-1)
            self.index -=1
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()