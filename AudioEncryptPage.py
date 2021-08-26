from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
from tkinter import messagebox as mb
import tkinter as tk
import Steganography as sg
import os

# dictionary of colors:
color = {"nero": "#252726", "cream": "#f5f5f5", "darkorange": "#FE6101", "lightgrey": "#545454"}

#Defining the tkinter's root variable
r = tk.Tk()
r.configure(background='#242424')
#Setting up the title
r.title("Krypto")
#To show our own icon in the taskbar
r.call('wm', 'iconphoto', r._w, PhotoImage(file='AppImages1/sa.png'))

r.geometry("800x550+280+100")

#Setting up the font for our app
large_font = ('Verdana',15)

LGRAY = '#545454'              
DGRAY = '#242424'
RGRAY = '#2e2e2e' 

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="AppImages1/menu.png")
closeIcon = PhotoImage(file="AppImages1/close.png")

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        homeLabel.config(bg=color["cream"])
        topFrame.config(bg=color["cream"])
        r.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        r.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(r, bg=color["cream"])
topFrame.pack(side="top", fill=tk.X)

# Header Info label text:
def info():
    lines = ['Enter Audio Location - copy your audio.wav file location',' ','Enter Plain Text - enter text or msg to encrypt it in audio file',' ', 'Enter Key - enter key to encrypt',' ','Enter Location For New Audio - give your location for new encrypted audio file to be saved',' ','Note : Use * .wav * Extension Audio Files']
    mb.showinfo('How To Use Krypto', "\n".join(lines))
# Add Info Bulb image file
Info_img = Image.open("AppImages1/icons8-light-oncool-48.png")
# Reszie the image using resize() method
Resize_Info_img = Info_img.resize((50,35))
Inf_img = ImageTk.PhotoImage(Resize_Info_img)
# Show image using label
homeLabel = tk.Label(topFrame, text="Krypto",image = Inf_img, font="Bahnschrift 15 bold", bg=color["cream"], fg="gray17", width=180,height=45, padx=200)
homeLabel.pack(side="right")
# Bind the label 
homeLabel.bind("<Button-1>", lambda e:info())

#--------------------------------------------------------------#
#------------------------ Main Frame --------------------------#
#--------------------------------------------------------------#
# Main label text:
# Add Mf image file
Main_img = Image.open("AppImages1/hphone.png")
# Reszie the image using resize() method
Resize_Main_img = Main_img.resize((420,420))
M_img = ImageTk.PhotoImage(Resize_Main_img)
# Show image using label
label1 = Label( r, image = M_img,width=520,height=570,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 330, y = 70)

#----------------------------------------------------------------#
#--------------------- Encrypt Code -----------------------------# C:\Users\soura\Desktop\hell.wav
def EncryptAudio():
    Loc = list(IEntry.get())
    key = IKeyEntry.get()
    newLoc = list(NewImgEntry.get())
    message = ITxtEntry.get()
    for i in range(len(Loc)):
        if Loc[i] == '\\':
            Loc[i] = "/"
    Loc = "".join(Loc)
    for i in range(len(newLoc)):
        if newLoc[i] == '\\':
            newLoc[i] = "/"
    newLoc = "".join(newLoc)
    try:
        print(Loc)
        print(key)
        print(newLoc)
        print(message)
        Segno = sg.Steganography(Loc)
        Segno.Write_Audio(message,newLoc,key)
        print(Message)
        mb.showerror("Alert","Your File have been created")
    except Exception:
        mb.showerror("ERROR", "Image Location NOT Found !!!" + Exception)



#------------------- Encrypt UI --------------------#

tILoc = StringVar()
tIPlainText = StringVar()
tITextFIle = StringVar()
tIKey = StringVar()
tNewLoc = StringVar()
v1 = IntVar(None,1)

# Enter audio Location
ILoc = Label(r,text="Enter Audio Location :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ILoc.place(x=10,y=100)
IEntry = Entry(r,textvariable = tILoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
IEntry.place(x=10,y=130)

# Enter Plain Text and Text File Location
IPlain = Label(r,text="Enter Plain Text :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
IPlain.place(x=10,y=200)
ITxtEntry = Entry(r,textvariable = tIPlainText,font = large_font,width = 17,fg="gray20",borderwidth=2)
ITxtEntry.place(x=10,y=230)

# Enter Key
IKey = Label(r,text="Key :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
IKey.place(x=10,y=280)
IKeyEntry = Entry(r,textvariable = tIKey,font = large_font,width = 22,fg="gray20",borderwidth=2)
IKeyEntry.place(x=10,y=310)

# Enter a location for new audio
NewImage = Label(r,text="Enter Location For New Audio :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
NewImage.place(x=10,y=370)
NewImgEntry = Entry(r,textvariable = tNewLoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
NewImgEntry.place(x=10,y=400)

# Encrypt Button
IInsert_Button = Button(r,text="Encrypt",font= ('Helvetica 15 bold'),fg="#f5f5f5",relief="raised",bg=DGRAY,borderwidth = 5,command = EncryptAudio )
IInsert_Button.place(x=200,y=450)

#------------------- End encrypt UI --------------------#

#--------------------- End Encrypt Code -----------------------------#
#--------------------------------------------------------------------#

def ImgEnDecryptPage():
    r.destroy()
    import AudioEncryptDecryptPage
# Add BackBtn image file
Back_Btn_img = Image.open("AppImages1/back.png")
# Reszie the image using resize() method
Resize_Back_Btn_img = Back_Btn_img.resize((40,25))
BackB_img = ImageTk.PhotoImage(Resize_Back_Btn_img)
BackB = Button(r,text="Back",font= ('Helvetica 15 bold'),fg="#FFFDD0",image=BackB_img,bg=DGRAY, width=40,height=20,borderwidth=5, relief="flat",command=ImgEnDecryptPage)
BackB.place(x=746, y=50)
#r.pack()

#------------------------ End Main Frame --------------------------#

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["cream"], activebackground=color["cream"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(r, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["cream"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Home", "Image", "Audio", "About", "Feedback", "Quit"]
# Navbar Option Buttons:
def Home():
    r.destroy()
    import HomePage
def Image():
    r.destroy()
    import ImageEncryptDecryptPage
def Audio():
    r.destroy()
    import AudioEncryptDecryptPage
def About():
    r.destroy()
    import AboutPage
def FeedBack():
    r.destroy()
    import FeedbackPage
def Quit():
    r.destroy()
for i in range(1):
    tk.Button(navRoot, text=options[0],command=Home, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[1],command=Image, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[2],command=Audio, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[3],command=About, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[4],command=FeedBack, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40
    tk.Button(navRoot, text=options[5],command=Quit, font="BahnschriftLight 15 bold", bg="gray17", fg=color["cream"], activebackground="gray17", activeforeground="blue", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["cream"], activebackground=color["cream"], bd=0, command=switch)
closeBtn.place(x=250, y=10)



# window in mainloop:
r.mainloop()
