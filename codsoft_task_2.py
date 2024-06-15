from tkinter import *#Importing graphichal library
root = Tk() #Base window
root.title('Simple Calculator')#title given to base window
root.attributes('-fullscreen',1) #giving fullscreen attribute as 1(True)
root.config(bg='Light Green')#setting light green colour to main window 
from tkinter import messagebox #importing messagebox module to display error messages
frame_1 = Frame(root) #Creating one frame
frame_1.pack(padx=5,pady=10) 
frame_1.config(bg='Black',bd=2) #specifying frame attributes 
head_widget = Label(frame_1,text='Simple Calculator',bg='Yellow',fg='Black')#Adding head message into frame_1
head_widget.pack(padx=5,pady=5,ipadx=5,ipady=5)#specifying widget attributes 
def addition():# Whenever i will press addition button addition () function will call 
    a = w2.get() #storing value passed by user 
    b = w4.get() #storing value passed by user 
    try:#(This try block  will only runs if compiler gets int values otherwise it will move towards except block)
        w_1.config(text='Addition Of Entered Numbers( '+a+' & '+b+') is :- ' +str(int(a)+int(b)))#Displaying Output
        w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
    except :
        try:#This try block will only runs if compiler gets float values otherwise it will move towards except block
            w_1.config(text='Addition Of Entered Numbers( '+a+' & '+b+') is :- ' +str(float(a)+float(b)))
            w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
        except ValueError:#Whenever value error occurs it will display dialog box window (line no. 23 & 24)
            messagebox.showerror('Warning !!!','Might be You Have Passed Letters\n\t      Or\n      \
Gaved Blank Input !!!')
    w2.delete(0,END) #Clearing entry  
    w4.delete(0,END) #Clearing entry  
def substraction(): # Whenever i will press substraction button substraction() function will call 
    a = w2.get()#storing value passed by user
    b = w4.get()#storing value passed by user
    try:#This try block  will only runs if compiler gets int values otherwise he will move towards except block
        w_1.config(text='Substraction Of Entered Numbers ( '+a+' & '+b+') is '+ str(int(a)-int(b)))
        w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
    except:
        try:#This try block will only runs if compiler gets float values otherwise it will move towards except block
            w_1.config(text='Substraction Of Entered Numbers( '+a+' & '+b+') is :- ' +str(float(a)-float(b)))#Displaying Output
            w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
        except ValueError:#Whenever value error occurs it will display dialog box window (line no. 38 & 39)
            messagebox.showerror('Warning !!!','Might be You Have Passed Letters\n\t      Or\n\
      Gaved Blank Input !!!')
    w2.delete(0,END)#Clearing entry  
    w4.delete(0,END)#Clearing entry  
def multiplication():# Whenever i will press multiplication button multiplication() function will call 
    a = w2.get()#storing value passed by user
    b = w4.get()#storing value passed by user
    try :#This try block  will only runs if compiler gets int values otherwise it will move towards except block
        w_1.config(text='Multiplication Of Entered Numbers ( '+a+' & '+b+') is '+ str(int(a)*int(b)))#Displaying Output
        w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
    except :
        try:#This try block will only runs if compiler gets float values otherwise it will move towards except block
            z = float(a)*float(b)
            e = round(z,2)
            w_1.config(text='Multiplication Of Entered Numbers( '+a+' & '+b+') is :- ' +str(e))#Displaying Output
            w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
        except ValueError:#Whenever value error occurs it will display dialog box window (line no.55 & 56)
            messagebox.showerror('Warning !!!','Might be You Have Passed Letters\n\t      Or\n\
      Gaved Blank Input !!!')
    w2.delete(0,END)#Clearing entry
    w4.delete(0,END)#Clearing entry
def division():# Whenever i will press division button division() function will call 
    a = w2.get()#storing value passed by user
    b = w4.get()#storing value passed by user
    try:#This try block  will only runs if compiler gets int values otherwise it will move towards except block
        w_1.config(text='Division Of Entered Numbers ( '+a+' & '+b+')is '+ str(int(a)/int(b)))#Displaying Output
        w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
    except:
        try:#This try block will only runs if compiler gets float values otherwise it will move towards except block
            z = float(a)/float(b)
            e = round(z,2)
            w_1.config(text='Division Of Entered Numbers( '+a+' & '+b+') is :- ' +str(e))
            w_1.pack(ipadx=5,ipady=5,padx=5,pady=5)
        except ValueError:#Whenever value error occurs it will display dialog box window (line no.72 & 73)
            messagebox.showerror('Warning !!!','Might be You Have Passed Letters\n\t      Or\n\
          Gaved Blank Input !!!')
        except ZeroDivisionError:#Whenever zero division error occurs it will display user friendly dialog box (line no.75)
            messagebox.showerror('Warning !',"Can't Divide By Zero !!")
    w2.delete(0,END)#Clearing entry
    w4.delete(0,END)#Clearing entry
p1 = PanedWindow(root)#creating panned window
p1.pack()
p2 = PanedWindow(root)#creatng another panned window
p2.pack()
w1 = Label(p1,text='Enter no  :- ')#Creating label
w1.pack(ipadx=5,ipady=5,padx=5,pady=5)
p1.add(w1)#Adding created label into panned window 1
w2 = Entry(p1)#Creating entry for number 1
w2.pack(ipadx=5,ipady=5,padx=5,pady=5)
p1.add(w2)#Adding created entry into panned window 1
w3 = Label(p2,text='Enter no  :- ')#Creating label
w3.pack(ipadx=5,ipady=5,padx=5,pady=5)
p2.add(w3)#Adding created label into panned window 2
w4 = Entry(p2)#Creating entry for number 2
w4.pack(ipadx=5,ipady=5,padx=5,pady=5)
p2.add(w4)#Adding created entry into panned window 2
w5 = Button(root,text='Addition',command=addition)#Refer Line No.12
w5.pack(ipadx=5,ipady=5,padx=10,pady=10)
w6 = Button(root,text='substraction',command=substraction)#Refer Line No.27
w6.pack(ipadx=5,ipady=5,padx=5,pady=5)
w7 = Button(root,text='Multiplication',command=multiplication)#Refer Line No.44
w7.pack(ipadx=5,ipady=5,padx=5,pady=5)
w8 = Button(root,text='Division',command=division)#Refer Line No.59
w8.pack(ipadx=5,ipady=5,padx=5,pady=5)
w_1 = Label(root)#Creating label with dynamic text
w_1.pack_forget() #It will not display in main window untill any function runs
w9 = Button(root,text='Exit !',command=root.destroy)#Button with built in destroy method
w9.pack(ipadx=5,ipady=5,padx=5,pady=5)
root.mainloop()#Main Event 