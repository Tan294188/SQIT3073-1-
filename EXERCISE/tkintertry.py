from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#root.iconbitmap("location") show the icon at title behind
#command =root.quit get out
# put picture -> my=ImageTK.PhotoImage(Image.oprn(".png"))
# mylabel.grid_forgert() delete smt
root.title("try")
#textbox,e.get() to get the value,columnspan the space contain how many 
e=Entry(root,width=50,bg="white",borderwidth=10)
e.grid(row=2,column=1)
e.insert(0,"Pls insert your name")
# Creating alphabet widget
myLabel1=Label(root, text="hello world")
myLabel2=Label(root, text="My name is Tan Chee Hwa")
#setting the position
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=2)
#create function to link with button, take note if want included parameter need to put Lambda
#if nonif parameter then just put the name and x put column
def myClick():
    mylabel=Label(root,text="You have click it")
    mylabel.grid(row=4,column=1)
#golbal means can use out of function
#create button fg=colour of font, padx, pady size, .grid show position, .pack ,bg=colour backgroudn
# inside the button, let the button disabled-> state=DISABLED
#sticky=W+E, refer to scretch it to the column, anchor=W, word position, relief=SUNKEN means the button press down
btt=Button(root,text="click",padx=10,pady=10,fg="red",command=root.quit,bd=1,relief=SUNKEN)
btt.grid(row=3,column=1)
#frame=Lableframe(root, text="",padx=.pady=) show the columnn in root
#btt.grid(row=2,column=1)
#showing it on the screen
root.mainloop()


