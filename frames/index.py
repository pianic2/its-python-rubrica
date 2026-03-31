import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="La mia app")
        panel = wx.Panel(self)

        # Aggiunta di un bottone
        btn = wx.Button(panel, label="Clicca!", pos=(50, 50))
        btn.Bind(wx.EVT_BUTTON, self.on_click)

        self.Show()

    def on_click(self, event):
        wx.MessageBox("Ciao dal bottone!", "Info")
