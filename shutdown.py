from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")
    
def shutdown():
    os.system("shutdown /s /t 1")
st = Tk()
st.title("Shutdown")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),cursor="hand2",relief=RAISED, command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),cursor="hand1",relief=RAISED, command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),cursor="hand1",relief=RAISED, command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button = Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),cursor="hand1",relief=RAISED, command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()