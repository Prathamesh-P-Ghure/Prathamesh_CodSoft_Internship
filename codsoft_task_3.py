from tkinter import * #Importing graphichal library
from tkinter import messagebox #importing messagebox module to display error messages
import string #Importing String Module to generate string 
import random #Importing random module to generate random results 
x = ''#variable with string data type 
root = Tk() #Base window
root.config(bg='Light Green',pady=10) # setting light green colour to main window 
root.title('Password Generator') #title given to base window
root.attributes('-fullscreen',1) #giving fullscreen attribute as 1(True)
def submit():# Whenever I Will Press Generate Password button submit() function will run 
    global x #Declaring x as global variable
    #Pack_forget method is used here with label & buttons to hide them temporary
    set_length.pack_forget()
    pw_length.pack_forget()
    exit_btn.pack_forget()
    genrate_pw.pack_forget()
    next_button.pack()
    exit_btn.pack(padx=5,pady=5)
    frame_2.pack(padx=5,pady=5)#specifying frame attributes 
    a = pw_length.get() #to get no. on scale 
    if d.get() == 1 and f.get() == 0 and g.get() == 0: #d.get == 1 means low checkbutton is selected by user 
        final_password = ''#Blank String in which final password will be store 
        x += string.ascii_letters #Storing all alphabets generated by using string module(upper & Lower case Both)
        for i in range(a):#for loop will run untill no stored on 'a' variable #Refer line no. 20 
            q = random.choice(x)#After every iteration,it will genrate random letter and stores inside 'q' variable 
            final_password += q #String concatenation 
        final_pw_label.config(text='Genrated Password (With Desired Length '+str(a)+' & Low Complexity) Is ---> '+final_password)#Displaying Output
        final_pw_label.pack(ipadx=5,ipady=5,padx=5,pady=5)
        low.toggle() #Clearing Checkbutton 
    elif f.get() == 1 and d.get() == 0 and g.get() == 0: #f.get == 1 means medium checkbutton is selected by user
        x += string.ascii_letters+string.digits
        final_password_1 = ''
        for i in range(a):
            t = random.choice(x)
            final_password_1 += t
        final_pw_label.config(text='Genrated Password (With Desired Length '+str(a)+' & Medium Complexity) Is ---> '+final_password_1)
        final_pw_label.pack(ipadx=5,ipady=5,padx=5,pady=5)
        medium.toggle() #Clearing Checkbutton
    elif g.get() == 1 and f.get() == 0 and d.get() == 0: #g.get == 1 means high checkbutton is selected by user
        x += string.ascii_uppercase + string.digits + string.punctuation
        final_password_2 = ''
        for i in range(a):
            t = random.choice(x)
            final_password_2 += t 
        final_pw_label.config(text='Genrated Password (With Desired Length '+str(a)+' & High Complexity) Is ---> '+final_password_2)
        final_pw_label.pack(ipadx=5,ipady=5,padx=5,pady=5)
        high.toggle() #Clearing Checkbutton
    elif g.get() == 0 and d.get() == 0 and f.get() == 0 :#Means No check button is selected 
        set_length.pack_forget()
        pw_length.pack_forget()
        final_pw_label.pack_forget()
        frame_2.pack_forget()
        #Dialog box will occur if user press Generate Password button without specifying dificulty level
        messagebox.showerror('Attention Here !!','You Have Pressed Generate Password button Without Specifying Dificulty Level.')
    else:
        set_length.pack_forget()
        pw_length.pack_forget()
        final_pw_label.pack_forget()
        frame_2.pack_forget()
        #Dialog box will occur if you select more than 1 dificulty level and press Generate Password button
        messagebox.showerror('Attention Here !!','You Cannot Specify More Than 1 Dificulty Level At Single Time.')
frame_1 = Frame(root) #Creating one frame
frame_1.pack()#Packing Frame_1
frame_1.config(bg='Black',bd=4)  #specifying frame attributes 
heading = Label(frame_1,text='Password Generator',bg='Yellow',fg='Black',font=('Cambria',20)) #Adding head message into frame_1
heading.pack(ipadx=5,padx=5,ipady=5,pady=5) #specifying widget attributes 
def next_button_cmd(): # Whenever i will press Next button next_button_cmd() function will run 
    #Pack_forget method is used here with label & buttons to hide them temporary
    frame_2.pack_forget()
    final_pw_label.pack_forget()
    exit_btn.pack_forget()
    set_length.config(text='Please Select Length Of Password On Following Scale:- ')#Label With Static Text
    set_length.pack(ipadx=5,ipady=5,padx=5,pady=5)
    if d.get() == 1 and f.get() == 0 and g.get() == 0: #d.get == 1 means low checkbutton is selected by user 
        pw_length.config(from_=1,to=5) #As low password is expecting by user so i am giving scale range (1 to 5)
        pw_length.pack(ipadx=5,ipady=5,padx=5,pady=5)
        genrate_pw.config(text='Generate Password',command=submit)#Refer Line no. 10
        genrate_pw.pack(ipadx=5,ipady=5,padx=5,pady=5)
    elif f.get() == 1 and d.get() == 0 and g.get() == 0: #f.get == 1 means medium checkbutton is selected by user
        pw_length.config(from_=6,to=11) #As medium password is expecting by user so i am giving scale range (6 to 11)
        pw_length.pack(ipadx=5,ipady=5,padx=5,pady=5)
        genrate_pw.config(text='Generate Password',command=submit)#Refer Line no. 10
        genrate_pw.pack(ipadx=5,ipady=5,padx=5,pady=5)
    elif g.get() == 1 and d.get() == 0 and f.get() == 0 : #g.get == 1 means high checkbutton is selected by user
        pw_length.config(from_=12,to=20) #As high password is expecting by user so i am giving scale range (12 to 20)
        pw_length.pack(ipadx=5,ipady=5,padx=5,pady=5)
        genrate_pw.config(text='Generate Password',command=submit)#Refer Line no. 10
        genrate_pw.pack(ipadx=5,ipady=5,padx=5,pady=5)
    elif g.get() == 0 and d.get() == 0 and f.get() == 0 :#Means No check button is selected 
        set_length.pack_forget()
        pw_length.pack_forget()
        final_pw_label.pack_forget()
        #Dialog box will occur if you press next button without specifying dificulty level
        messagebox.showerror('Attention Here !!','You Have Pressed Next button Without Specifying Dificulty Level.')
    else:
        set_length.pack_forget()
        pw_length.pack_forget()
        final_pw_label.pack_forget()
        #Dialog box will occur if you select more than 1 dificulty level  and press next button
        messagebox.showerror('Attention Here !!','You Cannot Specify More Than 1 Dificulty Level At Single Time.')
    exit_btn.config()
    exit_btn.pack(ipadx=5,padx=5,pady=5,ipady=5)
simp_label = Label(root,text='Please Select Dificulty Level Of Password You Want From Follwing',font=('Cambria',12))#Label With Static Text
simp_label.pack(ipadx=5,ipady=5,padx=5,pady=5)
d = IntVar() #Holds Integer Value 
low = Checkbutton(root,text='Low',variable=d,font=('Cambria',12))#Creating Check Button Low and assigning variable d
low.pack(ipadx=5,ipady=5,padx=5,pady=5)
f = IntVar() #Holds Integer Value 
medium = Checkbutton(root,text='Medium',variable=f,font=('Cambria',12))#Creating Check Button Medium and assigning variable f
medium.pack(ipadx=5,ipady=5,padx=5,pady=5)
g = IntVar() #Holds Integer Value 
high = Checkbutton(text='High',variable=g,font=('Cambria',12)) #Creating Check Button High and assigning variable g
high.pack(ipadx=5,ipady=5,padx=5,pady=5)
next_button = Button(root,text='Next --->',command=next_button_cmd,font=('Cambria',12))#Refer Line no. 67
next_button.pack(ipadx=5,ipady=5,padx=5,pady=5)
set_length = Label(root) 
set_length.config(font=('Cambria',12))
set_length.pack_forget()
pw_length = Scale(root,from_=1, to= 5,orient=HORIZONTAL)
pw_length.pack_forget() #It will not display in main window untill next_button function runs
genrate_pw = Button(root)
genrate_pw.config(font=('Cambria',12))
genrate_pw.pack_forget()
frame_2 = Frame(root) #creating frame_2 
frame_2.config(bg='Black',bd=1) #specifying attributes to frame_2 
frame_2.pack(padx=5,pady=5)
final_pw_label = Label(frame_2) #Adding final result into frame_2
final_pw_label.config(font=('Cambria',17,'bold'),fg='Red',bg='Light Blue')
final_pw_label.pack_forget() #It will not display in main window untill submit function runs
exit_btn = Button(root,text='Exit',command=root.destroy,font=('Cambria',12)) #Button with built in destroy method
exit_btn.pack(ipadx=5,ipady=5,padx=5,pady=5)
root.mainloop() #Main Event 