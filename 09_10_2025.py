#Irena Silmi Azizah
#NIM 2500859
#1b
jenis_kelamin = input("jenis kelamin wanita/pria :")
umur = int(input("berapa umur mu?" ))
tinggi = int(input("berapa tinggi mu? "))
iq = int(input("berapa iq mu?" ))
if (jenis_kelamin.lower() == "wanita") :
    if umur >= 18 and umur <= 25:
        if tinggi == 170 :
            if iq >= 130:
                print("anda adalah model")
        else :
            print("anda belum memenuhi syarat")
    else :
        print("anda belum memenuhi syarat")
if jenis_kelamin.lower() == "pria":
     if umur >= 18 and umur <= 25:
        if tinggi == 175 :
            if iq >= 130:
                print("anda adalah model")
        else :
            print("anda belum memenuhi syarat")
     else :
        print("anda belum memenuhi syarat")

