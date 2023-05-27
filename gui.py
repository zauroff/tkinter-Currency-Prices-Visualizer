from tkinter import *
from pandastable import Table
import live_data
import time

class Gui(Frame):
    
        def __init__(self, parent = None):
            self.parent = parent
            Frame.__init__(self)
            self.scrape = live_data.Scrape()
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title("Currency Prices")
            self.frame = Frame(self.main)
            self.frame.pack(fill=BOTH,expand=1)  
            self.pt = Table(self.frame, dataframe=self.scrape.fetch(), showtoolbar=True, showstatusbar=True)
            self.pt.show()
        
        def refresh(self):
            self.pt.model.df = self.scrape.fetch()
            self.pt.redraw()
            self.after(10000, self.refresh)
            
        def run(self):
            self.refresh()
            self.mainloop()
            
        def quit(self):
            self.quit()

app = Gui()
app.run()
