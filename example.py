import Steganography as stg

if __name__ == "__main__":
    stega_audio=stg.Steganography("C:/Users/soura/Desktop/hell.wav")  # sound path
    stega_audio.Write_Audio("Hello There Audio File!","C:/Users/soura/Desktop/hell2.wav","123")  # Encry text  auto save current dir
    print(stega_audio.Read_Audio("C:/Users/soura/Desktop/hell2.wav","123")) # reading path

#Changes
    #1. Custome Path
