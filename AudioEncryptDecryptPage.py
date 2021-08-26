from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
from tkinter import messagebox as mb
import tkinter as tk
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
    lines = ['Encrypt Button - For Audio Encryption', 'Decrypt Button - For Audio Decryption']
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

#------------------------ Main Frame --------------------------#
# Main label text:

# Add Mf image file
Main_img = Image.open("AppImages1/humanstickAudio.png")
# Reszie the image using resize() method
Resize_Main_img = Main_img.resize((550,450))
M_img = ImageTk.PhotoImage(Resize_Main_img)
# Show image using label
label1 = Label( r, image = M_img,width=520,height=470,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 10, y = 62)

def EnPage():
    r.destroy()
    import AudioEncryptPage
# Add EncBtn Audio file
Enc_Btn_img = Image.open("AppImages1/endecrypt.png")
# Reszie the image using resize() method
Resize_Enc_Btn_img = Enc_Btn_img.resize((70,50))
EncB_img = ImageTk.PhotoImage(Resize_Enc_Btn_img)
EncryptB = Button(r,text="Encrypt",font= ('Helvetica 15 bold'),fg="#FFFDD0",compound= LEFT,image=EncB_img,bg=DGRAY,width=180,height=50,borderwidth=5, relief="raised",command=EnPage)
EncryptB.place(x=550, y=150)

def DePage():
    r.destroy()
    import AudioDecryptPage
# Add DecBtn Audio file
Dec_Btn_img = Image.open("AppImages1/endecrypt.png")
# Reszie the image using resize() method
Resize_Dec_Btn_img = Dec_Btn_img.resize((70,50))
DecB_img = ImageTk.PhotoImage(Resize_Dec_Btn_img)
DecryptB = Button(r,text="Decrypt",font= ('Helvetica 15 bold'),fg="#FFFDD0",compound= LEFT,image=DecB_img,bg=DGRAY, width=180,height=50,borderwidth=5, relief="raised",command=DePage)
DecryptB.place(x=550, y=380)

def HomePage():
    r.destroy()
    import HomePage
# Add BackBtn image file
Back_Btn_img = Image.open("AppImages1/back.png")
# Reszie the image using resize() method
Resize_Back_Btn_img = Back_Btn_img.resize((40,25))
BackB_img = ImageTk.PhotoImage(Resize_Back_Btn_img)
BackB = Button(r,text="Back",font= ('Helvetica 15 bold'),fg="#FFFDD0",image=BackB_img,bg=DGRAY, width=40,height=20,borderwidth=5, relief="flat",command=HomePage)
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
