import wx

def click_save_button(event):
    save_file = open('MEMO.txt','w')
    save_file.write(text.GetValue())
    save_file.close()

if __name__ == '__main__':
    win = wx.App()
    frame = wx.Frame(None,-1,'memo',size=(500,400))

    panel = wx.Panel(frame,-1)
    save_button = wx.Button(panel,-1,pos=(385,10),label='SAVE')

    text = wx.TextCtrl(panel,-1,pos=(10,50),size=(450,300),style=wx.TE_MULTILINE)
    save_button.Bind(wx.EVT_BUTTON, click_save_button)
    frame.Show()
    win.MainLoop()