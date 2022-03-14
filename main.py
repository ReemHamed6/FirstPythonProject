from cgitb import text
import csv
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
from people import people



root = Tk()#Creating object of the tkinter
root.geometry('500x500')#Setting the width and the height of the window 
root.config(bg='#D3D3D3')
root.title("Special Events")
frame = Frame(root)
list = []


var1 = StringVar()
label1 = Label(root, textvariable=var1, relief=RIDGE,font=('David 14 bold'),width=10,height=1,bg='#5F9EA0',fg='white')
var1.set("Invitation")
label1.place(x=190,y=10)


var2 = StringVar()
label2 = Label(root, textvariable=var2, relief=FLAT,font=('David 14'),width=12,height=1,bg='#F5F5F5',fg='black')
var2.set("First Name: ")
label2.place(x=10,y=80)
i=0

def finishOnClick():
  fieldnames = ['First Name', 'Middle Name', 'Last Name' , 'Phone Number' , 'City']
  if len(name.get()) == 0 or len(lastName.get()) == 0 or len(city.get()) == 0:
    messagebox.showinfo("Error!","Missing Info")
  else:
    p = people(name.get(),middleName.get(),lastName.get(),phoneNumber.get(),city.get())
    list.append(p)
    with open('people.csv', mode='w',newline='') as people2:
      people1 = csv.DictWriter(people2, fieldnames=fieldnames)
      people1.writeheader()
      for person in list:
        
        people1.writerow({'First Name' :person.firstName,'Middle Name' : person.middleName,'Last Name':person.lastName , 'Phone Number':person.phoneNumber , 'City' :person.city })
      
     
  

def addAnotherOnClick():
  if len(name.get()) == 0 or len(lastName.get()) == 0 or len(city.get()) == 0:
    messagebox.showinfo("Error!","Missing Info")
  else:  
   p = people(name.get(),middleName.get(),lastName.get(),phoneNumber.get(),city.get())
   list.append(p)
   p.printFunc()
   nameEntered.delete(0,END)
   middleEntered.delete(0,END)
   lastEntered.delete(0,END)
   phoneEntered.delete(0,END)
   cityEntered.delete(0,END)


 
  


helv12 = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)

finishButton = Button(root, text = "Finish!", command = finishOnClick,font=helv12) 
finishButton.place(x=400, y=450)

nextBtn = Button(root,text='Add Another',command=addAnotherOnClick,font=helv12)
nextBtn.place(x=100,y=300)
name = StringVar()
nameEntered = Entry(root, textvariable = name)
nameEntered.place(width=100,height=28)
nameEntered.place(x=155, y=80)


var3 = StringVar()
label3 = Label(root, textvariable=var3, relief=FLAT,font=('David 14'),width=12,height=1,bg='#F5F5F5',fg='black')
var3.set("Middle Name: ")
label3.place(x=10,y=120)

middleName = StringVar()
middleEntered = Entry(root, textvariable = middleName)
middleEntered.place(width=100,height=28)
middleEntered.place(x=155, y=120)

var4 = StringVar()
label4 = Label(root, textvariable=var4, relief=FLAT,font=('David 14'),width=12,height=1,bg='#F5F5F5',fg='black')
var4.set("Last Name: ")
label4.place(x=10,y=160)

lastName = StringVar()
lastEntered = Entry(root, textvariable = lastName)
lastEntered.place(width=100,height=28)
lastEntered.place(x=155, y=160)

var5 = StringVar()
label5 = Label(root, textvariable=var5, relief=FLAT,font=('David 14'),width=12,height=1,bg='#F5F5F5',fg='black')
var5.set("Phone Number: ")
label5.place(x=10,y=200)

phoneNumber = StringVar()
phoneEntered = Entry(root, textvariable = phoneNumber)
phoneEntered.place(width=100,height=28)
phoneEntered.place(x=155, y=200)

var6 = StringVar()
label6 = Label(root, textvariable=var6, relief=FLAT,font=('David 14'),width=12,height=1,bg='#F5F5F5',fg='black')
var6.set("City: ")
label6.place(x=10,y=240)

city = StringVar()
cityEntered = Entry(root, textvariable = city)
cityEntered.place(width=100,height=28)
cityEntered.place(x=155, y=240)


root.mainloop()