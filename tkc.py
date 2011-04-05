# -*- coding: utf-8 -*-


## TkC v.0.0.7

## AUTHOR: sugardrunk
## URL: http://sugardrunk.devio.us

from Tkinter import *
import Pmw, tkFileDialog, urllib, urlparse

root = Tk()

# class Browser1 starting
class Browser1(Frame):
 
   def __init__(self):
      Frame.__init__(self)
      self.pack(expand=YES, fill=BOTH)
      w, h = root.winfo_screenwidth(), root.winfo_screenheight()
      self.master.geometry('%dx%d' % (w, h))
      self.master.title('TkC v.0.0.7')
                   
      self.address = Entry(self)
      self.address.pack(fill=X, padx=24, pady=12)
      self.address.bind('<Return>', self.getCode)

      self.contents = Pmw.ScrolledText(self, text_state=DISABLED)
      self.contents.pack(expand=YES, fill=BOTH, padx=6, pady=0)

      copyButton = Frame(relief=GROOVE, bd=0)
      Button1 = Button(copyButton, text='SAVE TO FILE', command=self.asksaveasfilename)
      Button1.pack()
      copyButton.pack(padx=0, pady=6)   
         
   # get + parse
   def getCode(self, event):
      page1 = event.widget.get()
      parse1 = urlparse.urlparse(page1)
      self.contents.text_state=NORMAL
      if parse1[0] == "":
        page1 = 'http://' + page1
      try:
         urllib1 = urllib.urlopen(page1)
         self.contents.settext(urllib1.read()) 
         urllib1.close()
      except IOError:
         self.contents.settext('URL NOT FOUND!')
      self.contents.text_state=DISABLED
   
   # define button command
   def asksaveasfilename(self):
      filename = tkFileDialog.asksaveasfilename()
      if filename:
        return open(filename, 'w')        

# class Browser1 ending
Browser1().mainloop()
