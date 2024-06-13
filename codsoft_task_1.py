#Task Scheduler
from tkinter import *
from tkinter import ttk
main_window = Tk() # Base Window
main_window.title('To Do List Application')# Giving title to base window
main_window.geometry('800x500+115+115') # setting base window size 
tab_ctrl = ttk.Notebook(main_window) # Creating tab 
tab_1_frame = Frame(tab_ctrl) # creating frame for tab 1
tab_1_frame.pack()
tab_1_frame.config(bg='Sky Blue')
tab_2_frame = Frame(tab_ctrl) # creating frame for tab 2
tab_2_frame.pack()
tab_2_frame.config(bg='Sky Blue')
tab_3_frame = Frame(tab_ctrl) # creating frame for tab 3
tab_3_frame.pack()
tab_3_frame.config(bg='Sky Blue')
test_frame = Frame(tab_1_frame) #creating one more frame in tab_1_frame for displaying heading
test_frame.pack()
test_frame.config(bg='Black')
title = Label(test_frame,text='To-Do List Application',bg='Yellow') #Lable with heading
title.pack(ipadx=5,ipady=5,padx=5,pady=5)
z = StringVar() # variable which stores string passed by entry
x = []
w8 = Listbox(tab_2_frame) # Creating list box in which i will insert tasks later
w8.pack(padx=5,pady=5)
w10 = Listbox(tab_3_frame)# Creating list box in which i will insert tasks later
w10.pack(padx=5,pady=5)
count = 1
def add():# When i will press add this task button add() function will call 
    global count
    w2.config(text=f'{count} tasks added sucessfully !!',fg='Red') #Label with dynamic text
    w2.pack(ipadx=5,ipady=5,padx=5,pady=5)
    w8.insert(0,w5.get()) #inserting task from entries into listbox 
    w10.insert(0,w5.get()) #inserting task from entries into listbox 
    w5.delete(0,END) #Clearing entry       
    count += 1 
def final_update():# When i will press Save Edited Task button final_update() function will call  
    for i in w10.curselection(): #Implementing for loop on list box with curselection method to get selected entry
        w10.delete(i)
        w10.insert(END,z.get())
        w8.delete(i)
        w8.insert(END,z.get())
def tab_3_button():# When i will press Edit button tab_3_button() function will call  
    w11 = Entry(tab_3_frame,textvariable=z)#crating entry with textvariable z which will store task
    w11.pack()
    w12 = Button(tab_3_frame,text='Save Edited Task',command=final_update) #refer line no 24
    w12.pack(ipadx=5,ipady=5,padx=5,pady=5)
tab_ctrl.add(tab_1_frame,text='Add Task')#Adding tab 
w4 = Label(tab_1_frame,text='Please Add Your  Task :- ') #Creating Label
w4.pack(padx=5,pady=5,ipadx=5,ipady=5)
w5 = Entry(tab_1_frame) #Creating Entry
w5.pack()
w7 = Button(tab_1_frame,text='Add This Task',command=add) #Refer line no.29
w7.pack(ipadx=5,ipady=5,padx=5,pady=5)
w6 = Button(tab_1_frame,text='Exit',command=main_window.destroy) #Button with built in destroy method
w6.pack(ipadx=5,ipady=5)
w2 = Label(tab_1_frame) #creating label with dynamic text
w2.pack_forget()# Disappering here but it will pack once if i press add task button
tab_ctrl.pack(expand=1,fill=BOTH)#Packing tab
tab_ctrl.add(tab_2_frame,text='View Tasks List') # Adding tab no.2
tab_ctrl.add(tab_3_frame,text='Edit Task') # Adding tab no.3
w1 = Button(tab_3_frame,text='Edit',command=tab_3_button) # Refer line no. 43
w1.pack(ipadx=5,ipady=5,padx=5,pady=5)
w13 = Button(tab_2_frame,text='Exit',command=main_window.destroy) #Button with built in destroy method
w13.pack(ipadx=5,ipady=5,padx=5,pady=5)
w15 = Label(tab_3_frame,text='Note :- Please Select Task That You Want To Edit & Then Click On Edit Button and \
At The End Click On Save Edited Task Button To Save Task ',fg='Red') #Creating label with text colour red 
w15.pack()
w14 = Button(tab_3_frame,text='Exit',command=main_window.destroy) #Button with built in destroy method
w14.pack(ipadx=5,ipady=5,padx=5,pady=5)
main_window.mainloop() #Main Event 
#Thank You !!!!