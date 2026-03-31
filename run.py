import wx
from frames.index import MyFrame
from engine.editor_rubrica import EditorRubrica


if __name__ == "__main__":

    editor = EditorRubrica(data_path="./data/rubrica.csv")

    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
