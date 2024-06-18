from tkinter import *
from tkinter import messagebox #to display dialogbox 
import random  #For generating random results
root = Tk() #Base Window
root.title('Rock Paper Scissors Game !!')# Giving title to base window
root.attributes('-fullscreen',1) #giving fullscreen attribute as 1(True)
root.config(bg='Light Green',pady=15) #setting light green colour to main window 
x = ['Rock','Paper','Scissor'] #List which will shuffle later 
r = 1 #To Count Rounds
g = 0 # To Track User Score Count 
h = 0 # To Track computer Score Count 
def play(): #Whenever i will press play btn play() function will run
    w2.config(text='Play Again ')
    global g 
    global h
    global r
    y = random.randrange(0,3) #Genrating random numbers and that genrated no. is storing inside y variable 
    s = x[y] #Passing genrated no as a index of list (for list refer line no. 8)
    if s == 'Rock' and f.get() == 'Rock': 
        w5.config(text='Your Choice Was Rock & Computer Choice Was Rock So its tied !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 1 #Incrementing user score as well as computer score because its tied round 
        h += 1 
        w7.config(text='After '+str(r) +'Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))#Displaying Score
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Paper' and f.get() == 'Rock':
        w5.config(text='Your Choice Was Rock & Computer Choice Was Paper So computer win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        h += 2 #Incrementing computer score becuase in these case computer is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Scissor' and f.get() == 'Rock':
        w5.config(text='Your Choice Was Rock & Computer Choice Was Scissor So You win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 2 #Incrementing user score becuase in these case user is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Rock' and f.get() == 'Paper':
        w5.config(text='Your Choice Was Paper & Computer Choice Was Rock So you win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 2 #Incrementing user score becuase in these case user is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Paper' and f.get() == 'Paper':
        w5.config(text='Your Choice Was Paper & Computer Choice Was Paper So its tied!!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 1 #Incrementing user score as well as computer score because its tied round 
        h += 1
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Scissor' and f.get() == 'Paper':
        w5.config(text='Your Choice Was Paper & Computer Choice Was Scissor So computer win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        h += 2 #Incrementing computer score becuase in these case computer is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Rock' and f.get() == 'Scissor':
        w5.config(text='Your Choice Was Scissor & Computer Choice Was Rock So computer win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        h += 2 #Incrementing computer score becuase in these case computer is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Paper' and f.get() == 'Scissor':
        w5.config(text='Your Choice Was Scissor & Computer Choice Was Paper So you win !!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 2 #Incrementing user score becuase in these case user is winner 
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    elif s == 'Scissor' and f.get() == 'Scissor':
        w5.config(text='Your Choice Was Scissor & Computer Choice Was Scissor So its tied!!')
        w5.pack(padx=5,pady=5,ipadx=5,ipady=5)
        g += 1 #Incrementing user score as well as computer score because its tied round 
        h += 1
        w7.config(text='After '+str(r) +' Rounds ,Your Score :- '+str(g)+' & Computer Score :- '+str(h))
        w7.pack(padx=5,pady=5,ipadx=5,ipady=5)
    else:
        messagebox.showwarning('Warning !!!','You Have To Select Options From Drop Down List')#without any selection if player press play button then warning event will occur by using message box
        r -= 1#Decrement is necessary here otherwise without any playing it will count round 1 because play funtion is runned for compiler
    r += 1 #At the end incrementing value is helpful to calculate how many rounds completed  
def refresh():#Whenever i will press reset button refresh() funtion will run 
    global g
    global h
    global r
    w5.config(text='Score Has Been Sucessfully Reset')#setting text for dynamic label
    g = 0
    h = 0
    r = 1
    w7.config(text='Your Score :- '+str(g)+' & Computer Score :- '+str(h))#setting text for dynamic label
    w7.pack(padx=5,pady=5,ipadx=5,ipady=5) 
frame_1 = Frame(root)#Making frame for one label widget(w1)which displays heading 
frame_1.pack()
frame_1.config(bg='Black',bd=4)
w1 = Label(frame_1,text='Rock Paper Scissors Game !!',bg='Yellow',fg='Black',font=('Cambria',15))
w1.pack(padx=5,pady=5,ipadx=5,ipady=5)
#Displaying Game Rules By using wigdet name as w9
w9 = Label(root,text='Please Read All Rules carefully To Avoide Confusions.\nRule No. 1 :- Rock beats scissors\
\nRule No. 2 :- scissors beat paper \nRule No.3 :- paper beats rock\n Rule No. 4 :- Winner Will Get 2 Points & \
In Case Of Tie , Both Player Will Get 1 Point Each',bg='Yellow',fg='Red',font=('Cambria',15))
w9.pack(padx=15,pady=15,ipadx=5,ipady=5)
w4 = Label(root,text='Please Select Your Choice From Following Options :- ',fg='Black',font=('Cambria',12))
w4.pack(ipadx=5,padx=5,ipady=5,pady=5)
f = StringVar()#Variable which assigned with drop down list which stores users choice
f.set('Options')
w6 = OptionMenu(root,f,*x)#Making drop down options
w6.pack()
w2 = Button(root,text='Play',command=play,fg='Black',font=('Cambria',12))#Refer Line no. 12
w2.pack(ipadx=5,ipady=5,padx=5,pady=5)
w5 = Label(root,font=('Cambria',12,'bold'),fg='Red',bg='Yellow')#Label With Dynamic text 
w5.pack_forget() # Disappering here but it will pack once if i press play button
w7 = Label(root,font=('Cambria',12,'bold'),fg='Red',bg='yellow')
w7.pack_forget() # Disappering here but it will pack once if i press play button
w8 = Button(root,text='Reset',command=refresh,fg='Black',font=('Cambria',12))#Refer Line no. 80
w8.pack(ipadx=5,ipady=5,padx=5,pady=5)
w3= Button(root,text='Exit',command=root.destroy,fg='Black',font=('Cambria',12)) #Button with built in destroy method which kills base window
w3.pack(ipadx=5,ipady=5,padx=5,pady=5)
root.mainloop()