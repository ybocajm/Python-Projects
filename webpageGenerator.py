from tkinter import *
import webbrowser


# create frame
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master 
        self.master.resizable(width=False, height=False) #can't resize popup
        self.master.geometry("{}x{}".format(800, 180)) # sets size of it
        self.master.title("Webpage Gen") # displays on title bar
        self.master.config(bg="lightgray") # background color

        self.varPageInfo = StringVar()  # variable to grab user input

        # text and buttons on popup

        self.lblenterText = Label(self.master,text = "Enter new site name: ",font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblenterText.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.txtenterText = Entry(self.master, text=self.varPageInfo, font=("Helvetica", 16), fg="black", bg="lightpink")
        self.txtenterText.grid(row= 0, column=1,padx=(30,0), pady=(30,0))

        self.btnGenerate = Button(self.master, text="Generate", width=10, height=2, command=self.GenPage)
        self.btnGenerate.grid(row=0, column=3,padx=(0,0), pady=(30,0))

        self.btnClose = Button(self.master, text="Close", width=10, height=2, command=self.cancel)
        self.btnClose.grid(row=1, column=0,padx=(0,30), pady=(30,0))

    # function to generate the webpage
    def GenPage(self):
        info = self.varPageInfo.get()
        f = open("newName.html","w")

        message = """<html>
                       <body>
                         <h1>
                           {}
                         </h1>
                       </body>
                     </html>""".format(info)
        f.write(message)
        f.close()

        webbrowser.open_new("newName.html")

    # allows user to cancel the popup, I guess without it hanging
    def cancel(self):
        self.master.destroy()

# it all starts here.   bam.
if __name__== "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    

"""
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
"""
