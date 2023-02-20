from tkinter import *
from tkinter import ttk
from tkinter import messagebox

TKGUI = Tk()
TKGUI.title('โปรแกรมบวกเลข')
TKGUI.geometry('720x360')

def cal_sum():
    num1 = int(innum1.get())
    num2 = int(innum2.get())
    sum = num1 + num2
    L3.config(text=sum)

L1 = ttk.Label(TKGUI, text="กรอกเลขตัวแรก")
L1.pack()
innum1=Entry(TKGUI, width=35)
innum1.pack()

L2 = ttk.Label(TKGUI, text="กรอกเลขตัวที่สอง")
L2.pack()
innum2=Entry(TKGUI, width=35)
innum2.pack()

L25 = Label(TKGUI, text="ผลรวม : ")
L25.pack(pady=20)

L3 = Label(TKGUI, text="...")
L3.pack(pady=20)

R1 = Radiobutton(TKGUI, text="บวก")
R1.pack(pady=20)

B1 = ttk.Button(TKGUI, text="กดเพื่อคำนวณ", command=cal_sum)
B1.pack()

TKGUI.mainloop()
