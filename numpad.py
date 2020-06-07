import tkinter 
import time
from tkinter.ttk import * 
from tkinter import *
root = Tk()
buttons = []
a={1,0,3}

def set_buttons():
    text = Text(root)
    u=1
    for i in range(3):
        buttons.append([])
        for j in range(3):
            buttons[i].append(Button(text=u, height=3, width=10))
            buttons[i][j].grid(row=i, column=j, sticky="nsew")
            #buttons[i][j].pack()
            u=u+1
    #buttons[2][2].config(highlightbackground='#3E4149')

    r=1
    c=1
    for i in a:
        
        if(i==1):
            c=c+1
        if(i==0):
            r=r-1
        if(i==2):
            c=c-1
        if(i==3):
            buttons[r][c].config(highlightbackground='#3E4149')
            

    
#root.geometry("%dx%d" % (1000, 1000))

set_buttons()





root.mainloop()
