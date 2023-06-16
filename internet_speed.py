from tkinter import *
import speedtest

def speedcheck():
    sp =  speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+ "Mbps"
    upload = str(round(sp.upload()/(10**6),3))+ "Mbps"
    lab_download.config(text=download)
    lab_upload.config(text=upload)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="blue")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman",20,"bold"),bg="Blue", fg="White")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman",20,"bold"),bg="Blue", fg="White")
lab.place(x=60,y=130,height=50,width=380)

lab_download = Label(sp, text="00", font=("Time New Roman",20,"bold"),bg="Blue", fg="White")
lab_download.place(x=60,y=200,height=50,width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman",20,"bold"),bg="Blue", fg="White")
lab.place(x=60,y=290,height=50,width=380)

lab_upload = Label(sp, text="00", font=("Time New Roman",20,"bold"),bg="Blue", fg="White")
lab_upload.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="Check Speed", font=("Time New Roman",20,"bold"), relief=RAISED,command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()