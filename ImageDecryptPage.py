from tkinter import *
import PIL.Image
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
    lines = ['Enter Image Location - copy your image.png file location',' ', 'Enter Key - enter key to decrypt',' ','Message - your decrypted msg will be shown here, keep it blank',' ','Enter Location To Save .txt File - give location to save your decrypted msg in .txt file',' ','Note : Use * .png * Extension Image Files']
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
Main_img = Image.open("AppImages1/htabnet.png")
# Reszie the image using resize() method
Resize_Main_img = Main_img.resize((350,480))
M_img = ImageTk.PhotoImage(Resize_Main_img)
# Show image using label
label1 = Label( r, image = M_img,width=520,height=470,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 350, y = 100)

#----------------------------------------------------------------#
#--------------------- Decrypt Code -----------------------------#
def EXTRACT_TEXT():
    #Here we get the image to extract data...
    Loc = list(EEntry.get())
    for i in range(len(Loc)):
        if Loc[i] == '\\':
            Loc[i]="/"
    Loc = "".join(Loc)
    try:
        image = PIL.Image.open(Loc)  
        image = image.convert('RGB')
    except Exception:
        mb.showerror("ERROR", "Image Location NOT Found !!!")

    key = EKeyEntry.get()
    if key == "":
        mb.showwarning("WARNING","No key used, Message might be not VALID")

    try:  
        cipher = EXTRACT(image,key)
        DECRYPT(cipher)
    except Exception:
        pass
def EXTRACT(image,key):
    #Again getting the pixel values...
    #We do same process of getting %2 to get character ascii values in binary...
    #We do this process wntill we have b3%2 as 0...
    pix_val = list(image.getdata())
    pix_val = [list(x) for x in pix_val]
    step = 0
    ans = []
    while (True):
        temp = []
        for _ in range(3):
            temp.append(pix_val[step][0]%2)
            temp.append(pix_val[step][1]%2)
            temp.append(pix_val[step][2]%2)
            step+=1
        check = temp[8]
        temp.pop(8)
        temp = [str(i) for i in temp]
        ans.append("".join(temp))
        if check == 1:
            break
    
    for i in range(len(ans)):
        ans[i] = chr(int(ans[i],2))

    #Returning the joint character string...
    return(''.join(ans))
def DECRYPT(cipher):
    key = EKeyEntry.get()
    key_len = len(key)
    cipher_split = []
    plain = []

    temp = list(cipher)
    if len(cipher) % (key_len) != 0:
        a = key_len - (len(cipher)%(key_len))
        for i in range(a):
            temp.append(" ")
        cipher = "".join(temp)
            
    for i in range(0,len(cipher),key_len):
        temp = []
        for j in range(key_len):
            temp.append(cipher[i+j])
        cipher_split.append(''.join(temp))

    for i in range(len(cipher_split)-1,-1,-1):
        if i == 0:
            plain.insert(0,GET_PLAIN(cipher_split[i],key))
        else:
            plain.insert(0,GET_PLAIN(cipher_split[i],cipher_split[i-1]))
    
    y = list("".join(plain))

    for i in range(len(y)):
        j=i+1
        if j>=len(y):
            pass
        else:
            if y[i]=="\\" and y[i+1]=="n":
                y[i]="\n"
                y = y[:i+1] + y[i + 1 + 1:]
    x="".join(y)
    ans = "".join(x)
    if v2.get() == 2:
        temp = list(NewTxtEntry.get())
        for i in range(len(temp)):
            if temp[i] == '\\':
                temp[i]="/"
        temp = "".join(temp)
        location = temp.split(".")
        location[-1]=".txt"
        location = "".join(location)
        try:
            file = open(location,"w")
            file.writelines(ans)
        except Exception:
            mb.showerror("ERROR","INALID Location !!!")
    else:
        ans = list(ans)
        for i in range(len(ans)):
            if ans[i]=="\n":
                ans[i]=" "
        tTxtLoc.set("".join(ans))
def GET_PLAIN(cipher,key):
    ans=[]
    for i in range(len(cipher)):
        x = ord(cipher[i])
        y = ord(key[i])
        if i%2 == 0:
            for _ in range(y):
                x-=1
                if x<=31:
                    x=126
        else:
            for _ in range(y):
                x+=1
                if x>=127:
                    x=32
        #print(x)
        ans.append(chr(x))
    return("".join(ans))
#------------------- Decrypt UI --------------------#
tELoc = StringVar()
tEKey = StringVar()
tTxtLoc = StringVar()
v2 = IntVar(None,1)

# Enter Image Location
ELoc = Label(r,text="Enter Image Location :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ELoc.place(x=10,y=100)
EEntry = Entry(r,textvariable = tELoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
EEntry.place(x=10,y=130)

# Enter Key
EKey = Label(r,text="Enter Key :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
EKey.place(x=10,y=190)
EKeyEntry = Entry(r,textvariable = tEKey,font = large_font,width = 22,fg="gray20",borderwidth=2)
EKeyEntry.place(x=10,y=220)

# Get Message Here & Enter the Location to save .txt file 
s1 = Radiobutton(r,variable = v2,value = 1,bg="#242424")
s1.place(x=10,y=300)
s2 = Radiobutton(r,variable = v2,value = 2,bg="#242424")
s2.place(x=10,y=330)

Extract_Option = Label(r,text="Get Message Here :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
Extract_Option.place(x=35,y=300)
Extract_Option = Label(r,text="Enter the Location to save .txt file :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
Extract_Option.place(x=35,y=330)
NewTxtEntry = Entry(r,textvariable = tTxtLoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
NewTxtEntry.place(x=10,y=360)

# Decrypt Button
EExtract_Button = Button(r,text="Decrypt",font= ('Helvetica 15 bold'),fg="#f5f5f5",relief="raised",bg=DGRAY,borderwidth = 5,command = EXTRACT_TEXT)
EExtract_Button.place(x=160,y=450)
#------------------- End Decrypt UI --------------------#

#--------------------- End Decrypt Code -----------------------------#
#--------------------------------------------------------------------#

def ImgEnDecryptPage():
    r.destroy()
    import ImageEncryptDecryptPage
# Add BackBtn image file
Back_Btn_img = Image.open("AppImages1/back.png")
# Reszie the image using resize() method
Resize_Back_Btn_img = Back_Btn_img.resize((40,25))
BackB_img = ImageTk.PhotoImage(Resize_Back_Btn_img)
BackB = Button(r,text="Back",font= ('Helvetica 15 bold'),fg="#FFFDD0",image=BackB_img,bg=DGRAY, width=40,height=20,borderwidth=5, relief="flat",command=ImgEnDecryptPage)
BackB.place(x=746, y=50)
#r.pack()

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
