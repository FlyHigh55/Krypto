from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
from tkinter import messagebox as mb
import tkinter as tk
import os
import smtplib
import webbrowser

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
    lines = ['Developed By', 'Sourav & Atul']
    mb.showinfo('Krypto', "\n".join(lines))
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
# Image 1 text:
# Add Mf image file
Main_img = Image.open("AppImages1/hearth.png")
# Reszie the image using resize() method
Resize_Main_img = Main_img.resize((370,440))
M_img = ImageTk.PhotoImage(Resize_Main_img)
# Show image using label
label1 = Label( r, image = M_img,width=380,height=480,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 430, y = 75)

# Image 2 text:
# Add Mf image file
Main_img2 = Image.open("AppImages1/twofriends.png")
# Reszie the image using resize() method
Resize_Main_img2 = Main_img2.resize((280,300))
M_img2 = ImageTk.PhotoImage(Resize_Main_img2)
# Show image using label
label1 = Label( r, image = M_img2,width=250,height=320,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 1, y = 190)

#--------------------------- About ------------------------------#

# About UI
ImageTit = Label(r,text="Image Steganography",font= ('Helvetica 13 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ImageTit.place(x=10,y=60)
ImageSteg1 = Label(r,text="In image steganography, a message is embedded into an image by altering",font= ('Helvetica 11'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ImageSteg1.place(x=10,y=90)
ImageSteg2 = Label(r,text="the values of some pixels, which are chosen by an encryption algorithm.",font= ('Helvetica 11'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ImageSteg2.place(x=10,y=110)
AudioTit = Label(r,text="Audio Steganography",font= ('Helvetica 13 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
AudioTit.place(x=10,y=140)
AudioSteg1 = Label(r,text="Audio Steganography is a technique used to transmit hidden information",font= ('Helvetica 11'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
AudioSteg1.place(x=10,y=170)
AudioSteg2 = Label(r,text="by modifying an audio signal in an imperceptible manner.",font= ('Helvetica 11'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
AudioSteg2.place(x=10,y=190)

ImageDev = Label(r,text="Developed By Sourav & Atul",font= ('Helvetica 13 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ImageDev.place(x=40,y=520)

ImageContact = Label(r,text="Contact Us : +91 9920380255",font= ('Helvetica 13 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ImageContact.place(x=440,y=520)

new = 1
url1 = "https://www.instagram.com/atulparte6350/"
def openinsta():
    webbrowser.open(url1,new=new)
    
# Add insta image file
Insta_Btn_img = Image.open("AppImages1/icons8-instagram-48.png")
# Reszie the image using resize() method
Resize_Insta_Btn_img = Insta_Btn_img.resize((30,30))
InstaB_img = ImageTk.PhotoImage(Resize_Insta_Btn_img)
InstaB = Button(r,text="Insta",image=InstaB_img,bg=DGRAY, width=30,height=25,borderwidth=5, relief="flat",command=openinsta)
InstaB.place(x=680, y=510)

new = 1
url = "https://github.com/AtulParte"
def opengithub():
    webbrowser.open(url,new=new)
    
# Add GitHub image file
GitHub_Btn_img = Image.open("AppImages1/icons8-github-30.png")
# Reszie the image using resize() method
Resize_GitHub_Btn_img = GitHub_Btn_img.resize((30,30))
GitHubB_img = ImageTk.PhotoImage(Resize_GitHub_Btn_img)
GitHubB = Button(r,text="GitHub",image=GitHubB_img,bg=DGRAY, width=30,height=25,borderwidth=5, relief="flat",command=opengithub)
GitHubB.place(x=730, y=510)


#------------------------- End About ---------------------------#

#------------------------------------------------------------------#
#------------------------ End Main Frame --------------------------#
#------------------------------------------------------------------#

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
