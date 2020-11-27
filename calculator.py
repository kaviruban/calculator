from tkinter import*


#crete object
one=Tk()
#crete calc specifications
one.geometry("500x600")
one.title("CALCULATOR")
one.configure(bg='black')


#calling the operations
total=""
def press(num):
    global total

    total=total+str(num)
    expression.set(total)
    
def equalpress():
    global total

    try:
        a=str(eval(total))
        expression.set(a)
        total=""
    except:
        expression.set('ERROR')
        total=""
def clear():
    global total

    total=""
    expression.set('0')

#creting display screen
screen=Frame(one,bg='#80ccff')
screen.pack()


expression=StringVar()
expression.set('0')
bt_screen=Entry(screen,textvariable=expression,justify='right',font=('arial',25,'bold'))
bt_screen.pack()

#creating buttons
bt1=Button(screen,text='1',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(1))
bt2=Button(screen,text='2',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(2))
bt3=Button(screen,text='3',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(3))
addition=Button(screen,text='+',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press('+'))
bt4=Button(screen,text='4',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(4))
bt5=Button(screen,text='5',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(5))
bt6=Button(screen,text='6',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(6))
subtraction=Button(screen,text='-',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press('-'))
bt7=Button(screen,text='7',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(7))
bt8=Button(screen,text='8',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(8))
bt9=Button(screen,text='9',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(9))
multiply=Button(screen,text='*',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press('*'))
bt0=Button(screen,text='0',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press(0))
decimal=Button(screen,text='.',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press('.'))
clear=Button(screen,text='C',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=clear)             
Division=Button(screen,text='/',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=9,height=3,command=lambda:press('/'))                
equal=Button(screen,text='=',font=('Ebrima',13,'bold'),relief='ridge',bd=3,bg='#80ccff',width=40,height=3,command=equalpress)

bt_screen.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=15)

bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)
addition.grid(row=1,column=3)

bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)
subtraction.grid(row=2,column=3)

bt7.grid(row=3,column=0)
bt8.grid(row=3,column=1)
bt9.grid(row=3,column=2)
multiply.grid(row=3,column=3)

bt0.grid(row=4,column=1)
decimal.grid(row=4,column=2)
Division.grid(row=4,column=0)
clear.grid(row=4,column=3)

equal.grid(row=5,column=0,columnspan=4)







