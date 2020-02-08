import wx
import wx.lib.agw.balloontip as BT

class MyFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, -1, "BalloonTip Demo")

        panel = wx.Panel(self)

        # Let's suppose that in your application you have a wx.TextCtrl defined as:
        mytextctrl = wx.TextCtrl(panel, -1, "I am a textctrl", pos=(100, 100))

        # You can define your BalloonTip as follows:
        tipballoon = BT.BalloonTip(topicon=None, toptitle="textctrl",
                                   message="this is a textctrl",
                                   shape=BT.BT_ROUNDED,
                                   tipstyle=BT.BT_LEAVE)

        # Set the BalloonTip target
        tipballoon.SetTarget(mytextctrl)
        # Set the BalloonTip background colour
        tipballoon.SetBalloonColour(wx.WHITE)
        # Set the font for the balloon title
        tipballoon.SetTitleFont(wx.Font(9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False))
        # Set the colour for the balloon title
        tipballoon.SetTitleColour(wx.BLACK)
        # Leave the message font as default
        tipballoon.SetMessageFont()
        # Set the message (tip) foreground colour
        tipballoon.SetMessageColour(wx.LIGHT_GREY)
        # Set the start delay for the BalloonTip
        tipballoon.SetStartDelay(1000)
        # Set the time after which the BalloonTip is destroyed
        tipballoon.SetEndDelay(3000)

# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()