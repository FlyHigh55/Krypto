from PIL import Image
import PIL
from cryptography.fernet import Fernet
from scipy.io.wavfile import read,write
import numpy
from scipy import signal


class Steganography():
    def __init__(self,p_path=""):
        self.Path = p_path
    
    def Write_Audio(self,p_msg,s_path,key):
        p_msg = self.ENCRYPT(p_msg,key)
        print(self.Path)
        a = read(self.Path)
        rate = a[0]
        data=numpy.array(a[1])
        my_Data = self.Char_ToBinary(p_msg)
        newdata = []
        loop1 = 0
        #Crate the data to write
        while (loop1<len(my_Data)):
            loop2 =0
            while(loop2<8):
                newdata.append(my_Data[loop1][loop2])
                loop2 +=1
            loop1 +=1
        #Message Lenght to Binary
        lenght = []
        dummy=len(p_msg)
        for i in range(32):
            if(dummy%2==0):
                lenght.insert(0,0)
                dummy=dummy>>1
            else:
                lenght.insert(0,1)
                dummy=dummy>>1
        #Write Data
        for i in range(len(newdata)):        
            if(newdata[i]==0):
                data[i][0] = data[i][0] >>1
                data[i][0] = data[i][0] <<1
            else:
                data[i][0] = data[i][0] | 1
        #Write Lenght
        for i in range(32):
            if(lenght[i]==0):
                data[i][1] = data[i][1] >>1
                data[i][1] = data[i][1] <<1
            else:
                data[i][1] = data[i][1] | 1
        write(s_path,rate,data)
        

    def Read_Audio(self,p_path,key):
        audio = read(p_path)
        data=numpy.array(audio[1])
        size = 0
        #Get Message Lenght
        for i in range(32):
            size += ( data[i][1] & 1)*(2**(32-i-1))
        dummy=0
        count = 0    
        msg ="" 
        #Get Message
        for i in range(size*8):
            dummy += (data[i][0] &1)*(2**count)
            count +=1        
            if (count%8==0):
                msg += chr(dummy)
                dummy=0            
                count=0
        return self.DECRYPT(msg,key)
    
    #FUNCTION THAT ENCRYPTS THE MESSAGE RETURNS KEY TO DECRYPT AND ENCRYPTED MESSAGE
    def Char_ToBinary(self,p_message):
        array1 = bytearray(p_message, 'utf-8')
        charlist=list(array1)
        binarylist=[]
        for i in charlist:
            j=0
            dummylist=[]
            dummy = i
            while(j<8):         
                dummylist.append(dummy & 1)
                dummy = dummy>>1
                j+=1
            binarylist.append(dummylist)
        return binarylist
    #Encypt Text With Symet Key
    def ENCRYPT(self ,plain, key):
        # The following is my encryption technique...
        key_len = len(key)
        plain_split = []
        cipher = []
        plain = list(plain)
        if len(plain) % (key_len) != 0:
            a = key_len - (len(plain) % (key_len))
            for i in range(a):
                plain.append(" ")
        for i in range(0, len(plain), key_len):
            temp = []
            for j in range(key_len):
                temp.append(plain[i + j])
            plain_split.append(''.join(temp))

        for i in range(len(plain_split)):
            if i == 0:
                cipher.append(self.GET_CIPHER(plain_split[i], key))
            else:
                cipher.append(self.GET_CIPHER(plain_split[i], cipher[i - 1]))
        return ("".join(cipher))

    

    def DECRYPT(self,cipher,key):
        key_len = len(key)
        cipher_split = []
        plain = []

        temp = list(cipher)
        if len(cipher) % (key_len) != 0:
            a = key_len - (len(cipher) % (key_len))
            for i in range(a):
                temp.append(" ")
            cipher = "".join(temp)

        for i in range(0, len(cipher), key_len):
            temp = []
            for j in range(key_len):
                temp.append(cipher[i + j])
            cipher_split.append(''.join(temp))

        for i in range(len(cipher_split) - 1, -1, -1):
            if i == 0:
                plain.insert(0, self.GET_PLAIN(cipher_split[i], key))
            else:
                plain.insert(0, self.GET_PLAIN(cipher_split[i], cipher_split[i - 1]))

        y = list("".join(plain))

        for i in range(len(y)):
            j = i + 1
            if j >= len(y):
                pass
            else:
                if y[i] == "\\" and y[i + 1] == "n":
                    y[i] = "\n"
                    y = y[:i + 1] + y[i + 1 + 1:]
        x = "".join(y)
        ans = "".join(x)
        ans = list(ans)
        for i in range(len(ans)):
            if ans[i] == "\n":
                ans[i] = " "
        return "".join(ans)

    def GET_PLAIN(self,cipher, key):
        ans = []
        for i in range(len(cipher)):
            x = ord(cipher[i])
            y = ord(key[i])
            if i % 2 == 0:
                for _ in range(y):
                    x -= 1
                    if x <= 31:
                        x = 126
            else:
                for _ in range(y):
                    x += 1
                    if x >= 127:
                        x = 32
            # print(x)
            ans.append(chr(x))
        return ("".join(ans))
    def GET_CIPHER(self,plain, key):
        ans = []
        for i in range(len(plain)):
            x = ord(plain[i])
            y = ord(key[i])
            if i % 2 == 0:
                for j in range(y):
                    x += 1
                    if x == 127:
                        x = 32
            else:
                for j in range(y):
                    x -= 1
                    if x == 31:
                        x = 126
            ans.append(chr(x))
        return ("".join(ans))


    

