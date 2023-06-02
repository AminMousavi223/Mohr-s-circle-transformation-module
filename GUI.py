from tkinter import *
from tkinter import ttk
#Start Tkinter
W = Tk()

#Add titel
W.title("Mohr's circle transformation module")

#By difault Window size
W.geometry('700x400')

#Scrollbar
Scr = Scrollbar(W)
Scr.pack(side=RIGHT,fill=BOTH)
frame1 = Frame(W)
frame1.pack(expand=True,fill=BOTH)
#Scr.config(command=frame1.yview)

#Menu 
menu = Menu(W)
M1 = Menu(menu,tearoff=0)
M1.add_command(label='New File')
M1.add_command(label='Open File...')
M1.add_command(label='Save')
M1.add_command(label='Save As...')
M1.add_command(label='Close',command=W.quit)

M2 = Menu(menu,tearoff=0)
M2.add_command(label='Undo')
M2.add_command(label='Redo')
M2.add_command(label='Cut')
M2.add_command(label='Copy')
M2.add_command(label='Pase')

M3 = Menu(menu,tearoff=0)
M3.add_command(label='Slove')
M3.add_command(label='Solution...')

M4 = Menu(menu,tearoff=0)

menu.add_cascade(label='File',menu=M1)
menu.add_cascade(label='Edit',menu=M2)
menu.add_cascade(label='Solver',menu=M3)
menu.add_cascade(label='Help',menu=M4)

#Make Menu
W.config(menu=menu)

#Labe Frame - entry
frame2 = Frame(frame1)

xd = LabelFrame(frame2,text='x direction')
Label(xd,text='Normal Stress').pack()
En1 = Entry(xd).pack()
Radio1 = [("Positive","Tension (+)"),("Negative","Compression (-)")]
c1 = StringVar()
c1.set("Positive")
for a1,b1 in Radio1:
  Radiobutton(xd,value=a1,text=b1,variable=c1,).pack()

yd = LabelFrame(frame2,text='y direction')
Label(yd,text='Normal Stress').pack()
En2 = Entry(yd).pack()
Radio2 = [("Positive","Tension (+)"),("Negative","Compression (-)")]
c2 = StringVar()
c2.set("Positive")
for a2,b2 in Radio2:
  Radiobutton(yd,value=a2,text=b2,variable=c2).pack()

xyd = LabelFrame(frame2,text='xy direction')
Label(xyd,text='Shear Stress').pack()
En3 = Entry(xyd).pack()
Radio3 = [("Positive","CW on x face (-)"),("Negative","CCW on x face (+)")]
c3 = StringVar()
c3.set("Positive")
for a3,b3 in Radio3:
  Radiobutton(xyd,value=a3,text=b3,variable=c3).pack()

#Button
but1 = Button(frame2,text='Compute')
but2 = Button(frame2,text='Details')

#Combo Box
val = ['MPa' , 'kPa' , 'kg/cm^2' , 'N/mm^2' , 'N/cm^2']
combo = ttk.Combobox(frame2,values=val)
combo.set('Select Unit')

#Check Button
AbsMax = IntVar()
ch1 = Checkbutton(frame2,text='Show Absolute Maximum Shear Stress',variable=AbsMax)

#Pack-grid
frame2.grid(row=0,column=0)
xd.grid(row=0,column=0)
yd.grid(row=0,column=1)
xyd.grid(row=0,column=2)

but1.grid(row=1,column=0,pady=10,ipadx=30)
but2.grid(row=1,column=1,pady=10,ipadx=40)

combo.grid(row=1,column=2,pady=10,padx=70)

ch1.grid(row=2,column=0,ipadx=20,ipady=20)

#Run Tkinter
W.mainloop()

