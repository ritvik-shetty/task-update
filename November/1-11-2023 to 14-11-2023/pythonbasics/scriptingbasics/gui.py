from tkinter import *

root=Tk()
frame=Frame(root)

labelText=StringVar()
label=Label(frame,textvariable=labelText)
labelText.set("This is a label")

button=Button(frame,text="Click Me")

label.pack()
button.pack()
frame.pack()

root.mainloop() # GUI Runs till the user presses to end