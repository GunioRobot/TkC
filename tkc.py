#!/usr/bin/env python
# -*- coding: utf-8 -*-


## TkC v.0.1.0

##  Fetch code from any url and save it to file.
##  Copyright (C) 2011 sugardrunk <http://sugardrunk.devio.us>


from Tkinter import *
import tkMessageBox
import Pmw, urllib, urlparse

root = Tk()
root.option_add('*font', 'sans -11')

class Browser1(Frame):
 
   def __init__(main):
      Frame.__init__(main)
      main.pack(expand=YES, fill=BOTH)

      w, h = root.winfo_reqwidth()*1.5, root.winfo_reqheight()*3
      main.master.geometry('%dx%d' % (w, h))
      main.master.title('TkC v.0.1.0')
                         
      main.entryBar = Entry(main, fg='#333')
      main.entryBar.pack(fill=X, padx=24, pady=12)
      main.entryBar.bind('<Return>', main.getCode)

      main.contents = Pmw.ScrolledText(main)
      main.contents.pack(expand=YES, fill=BOTH, padx=6, pady=0)      

      helpButton1 = Frame(relief=GROOVE, bd=0)
      button2 = Button(helpButton1, text='ABOUT', command=main.help, bg='white', fg='#333')
      button2.pack()      
      helpButton1.pack(expand=YES, fill=BOTH, side=LEFT, pady=12)

      copyButton1 = Frame(relief=GROOVE, bd=0)
      button3 = Button(copyButton1, text='SAVE TO FILE', command=main.savefile, bg='white', fg='#333')
      button3.pack()      
      copyButton1.pack(expand=YES, fill=BOTH, side=LEFT, pady=12)

      quitButton1 = Frame(relief=GROOVE, bd=0)
      button1 = Button(quitButton1, text='QUIT', command=main.quit, bg='white', fg='#333')
      button1.pack()      
      quitButton1.pack(expand=YES, fill=BOTH, side=LEFT, pady=12)
        
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

   # define button1 command
   def quit(main):
      sys.exit()

   # define button2 command
   def help(main):
      reload(sys)
      sys.setdefaultencoding('utf-8')      
      tkMessageBox.showinfo('About', 'TkC 0.1.0''\n''Copyright (C) 2011 sugardrunk''\n''\n''Fetch code from any URL and save it to file.''\n''\n'"URL's (IRI's) with non-ascii characters not supported.")
   
   # define button3 command
   def savefile(main):
      reload(sys)
      sys.setdefaultencoding('utf-8')
      main.contents.exportfile('output.html')
      tkMessageBox.showinfo('code saved', 'code saved to output.html')                                             

Browser1().mainloop()
root.mainloop()