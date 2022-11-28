
stk1=[]
stk=[]
x2=''
t=0

from tkinter import *
def call1():
    lst=[]
    global stk1,stk,x2,t,l1,l2
    x2=''
    if t==1:
        l1.destroy()
        l2.destroy()
        t=0
    p=x.get()
    def call(a,b):
        global stk,stk1
        #print(a)
        #print(b)
        x=['+','-','*','/','^']
        v=x.index(a)
        v1=x.index(b)
        
        if a in '+-' and b in'+-':
            stk1.append(b)
            stk.pop()
            stk.append(a)
        elif a in '/*' and b in '/*':
            stk1.append(b)
            stk.pop()
            stk.append(a)
            
        
        elif v1<v:
            stk.append(a)
            
            
        
        else:
            stk1.append(b)
            stk.pop()
            stk.append(a)
        #print(v,v1)






    stk=[]
    stk1=[]
    for i in p:
        lst+=i,
    lst.insert(0,'(')
    lst.insert(len(lst),')')
    #print(lst)


    for i in range(len(lst)):
        if lst[i].isalpha():
            stk1+=lst[i],
        else:
            if lst[i]==')':
                for j in range(len(stk)-1,-1,-1):
                    if stk[j]!='(':
                        stk1.append(stk[j])
                        stk.pop(j)
                    else:
                        stk.pop(j)
                        break
            
            if lst[i]=='(':
                stk+=lst[i],
                
            if lst[i] in '-+^*/':
                a=lst[i]
                if len(stk)>=1:
                    v=len(stk)-1
                    b=stk[v]
                    if b in '-^+*/':
                       # print(a,b)
                        call(a,b)
                    else:
                        stk+=lst[i],

                  
                else:
                    stk+=lst[i],


    
    #print(stk1)
    l1=Label(root,text='Your Result Is...',font='papyrue 15 bold',bg='cyan',fg='black')
    l1.place(x=130,y=290)        
    t+=1
    for i in stk1:
        x2+=str(i)
        x2+=' '
    l2=Label(root,text=x2,font='papyrue 15 bold',bg='cyan',fg='red')
    l2.place(x=70,y=320)        
        


root=Tk()
root.title('Infix to Postfix Evalution')
root.geometry('400x400')
root.configure(bg='yellow')

Label(root,text='INFIX TO POSTFIX ',font='Lato 18 bold',bg='yellow',fg='red2').place(x=75,y=60)

Label(root,text='Enter Your Infix',font='papyrue 10 bold',bg='yellow',fg='black').place(x=145,y=130)

x=Entry(root,font=10)
x.place(x=90,y=160)
Button(root,text='SUBMIT',fg='red',bg='black',padx=25,pady=10,command=call1).place(x=150,y=210)


Label(root,text='',font='papyrue 10 bold',bg='cyan',fg='black',padx=300,pady=200).place(x=0,y=280)
Label(root,text='Copyright(AnshAgarwal)',font='papyrue 10 bold',bg='cyan',fg='black').place(x=120,y=380)








root.mainloop()