from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime
import csv

def writecsv(datalist):
    with open('013_tkinter-gui-csv-hw.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) 
        fw.writerow(datalist)

def readcsv():
    with open('013_tkinter-gui-csv-hw.csv',encoding='utf-8',newline='') as file2:
        fr = csv.reader(file2) 
        data = next(fr)
    return data

def readcsv2(x):
    i = x
    if i >= 0:
        with open('013_tkinter-gui-csv-hw.csv',encoding='utf-8',newline='') as file2:
            dataArray = []
            fr = csv.reader(file2)
            for row in fr:
                dataArray.append(row)
            data = dataArray[i+1]
        return data

def savedata():
    timeget = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_hw = hw_data.get()
    data_detail = hw_detail.get()
    text = [timeget,data_hw,data_detail]
    writecsv(text)
    hw_data.set('..กรอกเรียบร้อย..')
    hw_detail.set('..กรอกเรียบร้อย..')

#ฟังก์ชั่น ตรวจจับ click
def handle_click(event):
    hw_detail.set('')   
def handle_click2(event):
    hw_data.set('')       
def handle_click3(event):
    rowget.set('')   


GUI = Tk() 
GUI.title('โปรแกรมบันทึกข้อมูลการบ้าน')
GUI.geometry('900x600')

#กรอบ
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลการบ้านที่ต้องการเข้าไป')
LF1.place(x=50,y=30)
LF3 = ttk.LabelFrame(GUI,text='แสดงผล')
LF3.place(x=400,y=30)

#Entry E1 คือข้อมูลการบ้าน hw_data
#Entry E2 คือรายละเอียด hw_detail

hw_data = StringVar()
hw_data.set('กรอกข้อมูลการบ้าน')
hw_detail = StringVar()
hw_detail.set('กรอกรายละเอียด')
rowget = IntVar()
rowget.set('1')
firstRow = StringVar()
firstRow.set('                                                                                   ')
rowShow = StringVar()
rowShow.set('                                                                                   ')

E1 = ttk.Entry(LF1,textvariable=hw_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)
E1.bind("<1>", handle_click2) #ล้างเมื่อคลิกจะกรอก

E2 = ttk.Entry(LF1,textvariable=hw_detail,font=('Angsana New',25))
E2.pack(pady=10,padx=10)
E2.bind("<1>", handle_click) #ล้างเมื่อคลิกจะกรอก

lb12 = ttk.Label(LF1,text='กรอกแถวที่ต้องการ (เริ่มที่ 1)')
lb12.pack(pady=10,padx=10)

E3 = ttk.Entry(LF1,textvariable=rowget,font=('Angsana New',25))
E3.pack(pady=10,padx=10)
E3.bind("<1>", handle_click3) #ล้างเมื่อคลิกจะกรอก

EsuEsu = ttk.Label(LF3,textvariable=firstRow,font=('Angsana New',20))
EsuEsu.pack(pady=10,padx=10)

Esu = ttk.Label(LF3,textvariable=rowShow,font=('Angsana New',20))
Esu.pack(pady=10,padx=10)

B4 = ttk.Button(LF1,text='บันทึกข้อมูลทั้งหมด',command=savedata)
B4.pack(ipadx=20,ipady=20)

def getdata():
    row = rowget.get()
    row = row - 1
    firstRow.set(readcsv())
    rowShow.set(readcsv2(row))
    print(readcsv2(row))

def getnextdata():
    row = rowget.get()
    rowget.set(row + 1)
    row = rowget.get()
    row = row - 1
    firstRow.set(readcsv())
    rowShow.set(readcsv2(row))
    print(readcsv2(row))

def getpervdata():
    row = rowget.get()
    rowget.set(row - 1)
    row = rowget.get()
    row = row - 1
    firstRow.set(readcsv())
    rowShow.set(readcsv2(row))
    print(readcsv2(row))    

B6 = ttk.Button(LF1,text='แสดงข้อมูลแถวที่เลือก',command=getdata)
B6.pack(ipadx=20,ipady=20)

B7 = ttk.Button(LF1,text='แสดงข้อมูลแถวถัดไป',command=getnextdata)
B7.pack(ipadx=20,ipady=20)

B8 = ttk.Button(LF1,text='แสดงข้อมูลแถวก่อนหน้า',command=getpervdata)
B8.pack(ipadx=20,ipady=20)

GUI.mainloop()