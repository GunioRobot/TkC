# -*- coding: utf-8 -*-


## TkC v.0.0.9

##  Fetch code from any url and save it to file
##  Copyright (C) 2011 sugardrunk <http://sugardrunk.devio.us>


from Tkinter import *
import Pmw, urllib, urlparse

root = Tk()

class Browser1(Frame):
 
   def __init__(main):
      Frame.__init__(main)
      main.pack(expand=YES, fill=BOTH)

      w, h = root.winfo_screenwidth(), root.winfo_screenheight()
      main.master.geometry('%dx%d' % (w, h))
      main.master.title('TkC v.0.0.9')
                         
      main.entryBar = Entry(main, fg='#333')
      main.entryBar.pack(fill=X, padx=24, pady=12)
      main.entryBar.bind('<Return>', main.getCode)

      main.contents = Pmw.ScrolledText(main)
      main.contents.pack(expand=YES, fill=BOTH, padx=6, pady=0)
      
      copyButton1 = Frame(relief=GROOVE, bd=0)
      button1 = Button(copyButton1, text='SAVE TO FILE', command=main.savefile, bg='white', fg='#333')
      button1.pack()
      copyButton1.pack(padx=0, pady=6)   
         
   # get code
   def getCode(main, event):
      url1 = event.widget.get()
      parseEntry = urlparse.urlparse(url1)
      main.contents.text_state=NORMAL
      if parseEntry[0] == '':
        url1 = 'http://' + url1
      try:
         urllib1 = urllib.urlopen(url1)
         main.contents.settext(urllib1.read())         
         urllib1.close()
      except IOError:
         main.contents.settext('URL NOT FOUND!')
      main.contents.text_state=DISABLED   
   
   # define button command
   def savefile(main):
      reload(sys)
      sys.setdefaultencoding('utf-8')
      main.contents.exportfile('output.html')                    

Browser1().mainloop()
root.mainloop()