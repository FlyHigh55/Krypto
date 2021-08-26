from tkinter import *
import PIL.Image
from PIL import Image
from PIL import ImageTk
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
    lines = ['Enter Image Location - copy your image.png file location',' ','Enter Plain Text - enter text or msg to to encrypt it in audio file',' ','Enter Text File Location - copy your location of your .txt file with msg in it to be encrypt',' ', 'Enter Key - enter key to encrypt',' ','Enter Location For New Image - give your location for new encrypted image file to be saved',' ','Note : Use * .png * Extension Image Files']
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
Main_img = Image.open("AppImages1/hsecurity.png")
# Reszie the image using resize() method
Resize_Main_img = Main_img.resize((350,360))
M_img = ImageTk.PhotoImage(Resize_Main_img)
# Show image using label
label1 = Label( r, image = M_img,width=520,height=470,borderwidth=5,bg="#242424",relief=FLAT)
label1.place(x = 380, y = 140)

#----------------------------------------------------------------#
#--------------------- Encryp
def INSERT_TEXT():
    #With the help of this function, we insert text from textbox into our inserted images...
    #First we get the location of the image...
    Loc = list(IEntry.get())
    #If we just copy the location from file explored we will get "\" in it, so to replace "\" with "/" we run following code...
    for i in range(len(Loc)):
        if Loc[i] == '\\':   #Using "//" because "\" is the special character and to gert "\" we need to use "\" before that hence "\\"
            Loc[i]="/"
    Loc = "".join(Loc)
    try:
        #Opening the image from the given location and converting that to RGB
        image = PIL.Image.open(Loc)
        print(image)
        image = image.convert('RGB')
    except Exception:
        #If we enter wrong location we will get message-box displaying error
        mb.showerror("ERROR","Image not found !!!"+Exception)


    x = v1.get()   #Checking our first radio button
    if x==1:    #If x=1 we take text from the text box...
        plain = ITxtEntry.get()
        if plain == "":    #If there is no text, it will convert that to " " and encrypt it giving us with cyphertext
            plain = " "
    else:    #Here we take text from an text file (whose location is provided)
        temp = list(IFileEntry.get())
        #Using same procedure as above to access file contents...
        for i in range(len(temp)):
            if temp[i] == '\\':
                temp[i]="/"
        temp = "".join(temp)
        ext = temp.split(".")
        if ext[-1] == "txt":
            try:
                with open(temp,"r") as txt_file:
                    plain = txt_file.read()
            except Exception:
                mb.showerror("ERROR","File not found !!!")
        else:
            mb.showerror("ERROR","File type not supported !")
    try:
        y = list(plain)
        for i in range(len(y)):
            if y[i] == '\n':
                y[i]='\\n'
        plain="".join(y)
    except Exception:
        pass

    #Getting the key to encrypt the image...
    key = IKeyEntry.get()
    if key == "":
        #Necessary to provide a key
        mb.showwarning("WARNING","NO KEY USED, Reciever might not be able to view message !")

    try:
        #Now, calling encrypt funv=ction to get encrypted text...
        cipher = ENCRYPT(plain,key)
        #Using insert function to embedd that into our image...
        INSERT(image,cipher)
    except Exception:
        pass 
def INSERT(image,cipher):
    #This function embedds cypher text into image
    plain = ITxtEntry.get()
    #Getting the size of image
    width, height = image.size 
    if len(plain) > ((width*height)/3):
        #As we are encoding each character into 3 pixels we check if number of characters are more than .33pixels in image...
        mb.showerror("ERROR","Text too long to be encoded into image !")
    else:
        #Getting the pixel values of the image...
        pix_val = list(image.getdata())
        pix_val = [list(x) for x in pix_val]    #Converting them into list of pixel values...

        step = 0
        #Now taking 3 pixels at a time... 
        #Let [r1, g1, b1], [r2, g2, b2], [r3 ,g3, b3] be our 3 pixels in which and our character is "a" => (65)10 => (01000001)2
        #Here we have 8 bits and 9 pixel values...
        #so deending on our bit we change or not change the pixel value...
        #EG => bit1 = 0, if r1%2 == 0, we dont change else we subtract it by 1 to make r1%2 = 0
        #We do this for all 8 pixels
        # (0, 1, 0, 0, 0, 0, 0, 1) = (r1%2, g1%2, b1%2, r2%2, g2%2, b2%2, r3%2, g3%2)
        #Last pixel value is used to tell if this is our last character or not ...
        #If this is last character then b3%2 == 0.
        #If we get b3%2 == 0, then we stop there... else we continue...
        for i in range(len(cipher)):
            a = ord(cipher[i])
            a = list(format(a,'08b'))
            k=0
            for _ in range(3):
                if str((pix_val[step][0])%2) != a[k]:
                    if pix_val[step][0]!=0:
                        pix_val[step][0]-=1
                    else:
                        pix_val[step][0]+=1
                k+=1

                if str((pix_val[step][1])%2) != a[k]:
                    if pix_val[step][1]!=0:
                        pix_val[step][1]-=1
                    else:
                        pix_val[step][1]+=1
                k+=1

                if k!=8:
                    if str((pix_val[step][2])%2) != a[k]:
                        if pix_val[step][2]!=0:
                            pix_val[step][2]-=1
                        else:
                            pix_val[step][2]+=1
                    k+=1
                else:
                    if i != len(cipher)-1:
                        if (pix_val[step][2])%2 != 0:
                            if pix_val[step][2]!=0:
                                pix_val[step][2]-=1
                            else:
                                pix_val[step][2]+=1
                    else:
                        if (pix_val[step][2])%2 != 1:
                            if pix_val[step][2]!=0:
                                pix_val[step][2]-=1
                            else:
                                pix_val[step][2]+=1

                step+=1
        
        #Once we change the pixel values, we make them permanent and make a new image using them...
        #We save the image to the location provided, if location is not provided, we simply save that in same directory 
        h=0
        w=0
        for i in range((len(cipher))*3):
            if i == width:
                h+=1
                w=0
            else:
                t = []
                t.append(pix_val[i][0])
                t.append(pix_val[i][1])
                t.append(pix_val[i][2])
                t = tuple(t)
                image.putpixel( (w,h) , t )
                w+=1
        #image.show()
        if NewImgEntry.get() == "":
            temp = list(IEntry.get())
            for i in range(len(temp)):
                if temp[i] == '\\':
                    temp[i]="/"
            temp = "".join(temp)
            location = temp.split(".")
            location.insert(1,"(1).")
            location[-1]="png"
            location = "".join(location)
        else:
            try:
                location = NewImgEntry.get()
            except Exception:
                mb.showerror("ERROR","INVALID Location !!!")
        try:
            image.save(location)
        except Exception:
            pass
def ENCRYPT(plain,key):
    #The following is my encryption technique...
    key_len = len(key)
    plain_split = []
    cipher=[]
    plain = list(plain)
    if len(plain) % (key_len) != 0:
        a = key_len - (len(plain)%(key_len))
        for i in range(a):
            plain.append(" ")
    for i in range(0,len(plain),key_len):
        temp = []
        for j in range(key_len):
            temp.append(plain[i+j])
        plain_split.append(''.join(temp))
    
    for i in range(len(plain_split)):
        if i == 0:
            cipher.append(GET_CIPHER(plain_split[i],key))
        else:
            cipher.append(GET_CIPHER(plain_split[i],cipher[i-1]))
    return("".join(cipher))
def GET_CIPHER(plain,key):
    ans=[]
    for i in range(len(plain)):
        x = ord(plain[i])
        y = ord(key[i])
        if i%2 == 0:
            for j in range(y):
                x+=1
                if x==127:
                    x=32
        else:
            for j in range(y):
                x-=1
                if x==31:
                    x=126
        ans.append(chr(x))
    return("".join(ans))

def EXTRACT_TEXT():
    #Here we get the image to extract data...
    Loc = list(EEntry.get())
    for i in range(len(Loc)):
        if Loc[i] == '\\':
            Loc[i]="/"
    Loc = "".join(Loc)
    try:
        image = Image.open(Loc)  
        image = image.convert('RGB')
    except Exception:
        mb.showerror("ERROR","Image Location NOT Found !!!")

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

#------------------- Encrypt UI --------------------#

tILoc = StringVar()
tIPlainText = StringVar()
tITextFIle = StringVar()
tIKey = StringVar()
tNewLoc = StringVar()
v1 = IntVar(None,1)

# Enter Image Location
ILoc = Label(r,text="Enter Image Location :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ILoc.place(x=10,y=100)
IEntry = Entry(r,textvariable = tILoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
IEntry.place(x=10,y=130)

# Enter Plain Text and Text File Location
IPlain = Label(r,text="Enter Plain Text :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
IPlain.place(x=10,y=200)
ITxtLoc = Label(r,text="Enter Text File Location :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
ITxtLoc.place(x=280,y=200)

r1 = Radiobutton(r,variable = v1,value = 1,bg="#242424",text = "                                                              ")
r1.place(x=10,y=230)
r2 = Radiobutton(r,variable = v1,value = 2,bg="#242424",text = "                                                         ")
r2.place(x=280,y=230)

ITxtEntry = Entry(r,textvariable = tIPlainText,font = large_font,width = 17,fg="gray20",borderwidth=2)
ITxtEntry.place(x=35,y=230)
IFileEntry = Entry(r,textvariable = tITextFIle,font = large_font,width = 17,fg="gray20",borderwidth=2)
IFileEntry.place(x=305,y=230)

# Enter Key
IKey = Label(r,text="Key :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
IKey.place(x=10,y=280)
IKeyEntry = Entry(r,textvariable = tIKey,font = large_font,width = 22,fg="gray20",borderwidth=2)
IKeyEntry.place(x=10,y=310)

# Enter a location for new image
NewImage = Label(r,text="Enter Location For New Image :",font= ('Helvetica 15 bold'),fg="#f5f5f5",borderwidth = 0 , bg = "#242424")
NewImage.place(x=10,y=370)
NewImgEntry = Entry(r,textvariable = tNewLoc,font = large_font,width = 30,fg="gray20",borderwidth=2)
NewImgEntry.place(x=10,y=400)

# Encrypt Button
IInsert_Button = Button(r,text="Encrypt",font= ('Helvetica 15 bold'),fg="#f5f5f5",relief="raised",bg=DGRAY,borderwidth = 5,command = INSERT_TEXT)
IInsert_Button.place(x=200,y=450)

#------------------- End encrypt UI --------------------#

#--------------------- End Encrypt Code -----------------------------#
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
