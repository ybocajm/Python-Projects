from tkinter import *

# everything in kinter is a widget

root = Tk()
root.title("gui buoy")

e = Entry(root, width=100, bg="lightpink", borderwidth=200)
e.pack()
e.insert(0, "Enter new name of site: ")

#function to give button action?
def myClick():
    hello = e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# don't put () next to myClick, because it'll put the text on the screen, not
# display it after you click it
myButton = Button(root, text="Submit", padx=10, pady=10, command=myClick, fg="black", bg="lightpink").pack()
#myButton2 = Button(root, text="packersmacker", state=DISABLED, fg="#fff", bg="#000").pack()


#create an invent loop.  Loop keeps going till we end it
root.mainloop()
