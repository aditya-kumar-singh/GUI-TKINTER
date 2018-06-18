
# coding: utf-8

# In[258]:


import tkinter as tk
#root=Tk()
#from tkinter import ttk
from tkinter import *
import tkinter.messagebox


# In[259]:


LARGE_FONT=("Verdana",12)
#Credentials={'ADI': '123'}
Credentials={}


# In[260]:


def insert(Username,Password):
    if Username.get() not in Credentials:
        Credentials[Username.get()]=Password.get()
        print(Credentials)


# In[261]:


#def popupmsg(msg):
    #popup=tk.Tk()
    #popup.wm_title("!")
    #label=tk.Label(popup,text=msg,font=LARGE_FONT)
    #label.pack(side="top",fill="x",pady=10)
    #Button1=ttk.Button(popup,text="okay",command=popup.destroy)
    #Button1.pack()
    #popup.mainloop()


# In[262]:


def successful(Username,Password):
    if Username.get() in Credentials:
        new=tk.Tk()
        new.geometry('500x500')
        label=tk.Label(new,text="Welcome to Booking.com",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
    else:
        #print(" Wrong ")
        tk.messagebox.showinfo('Window Title','Check Your Credentials')
        #popupmsg("Check your Credentinals")
        
        #label=tk.Label(self,text="Kindly check your Credentials ",font=LARGE_FONT)
        #label.pack(pady=10,padx=10)


# In[263]:


class SeaofBTCapp(tk.Tk):
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        tk.Tk.wm_title(self,"Booking.com")
        
        
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        
        container.grid_rowconfigure(0,weight=1)#0 is min size
        container.grid_columnconfigure(0,weight=1)#weight is like priority
        
        self.frames={}
        
        for F in (LandingPage,SuccessfulLogin,StartPage,Login,SuccessfulRegister):
       # for F in (StartPage,PageOne,PageTwo,SuccessfulLogin,LandingPage):
         #for F in (LandingPage,PageOne,PageTwo,SuccessfulLogin,StartPage):
            #frame=StartPage(container,self)
            frame=F(container,self)
            

            #self.frames[StartPage]=frame
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")#grid is like pack#grid tells in which row or column are you in
            # sticky is used for dirn  #nsew-north south east west #ticky is like alignment

            
        #self.show_frame(StartPage) 
        self.show_frame(LandingPage) 

    def show_frame(self,cont):
        
        frame=self.frames[cont]
        frame.tkraise()


# In[264]:


class LandingPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label=tk.Label(self,text="WELCOME USER",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button=ttk.Button(self,text="Login",command=lambda: controller.show_frame(Login))
        
        button.pack(pady=12)
        
        button2=ttk.Button(self,text="Registration",command=lambda: controller.show_frame(StartPage))
        
        button2.pack()
        


# In[265]:


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #root.geometry('500*500')
        label=tk.Label(self,text="Registration Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #entry_1=Entry(root)
        #entry_1.place(x=50,y=45)
        
        #global entry1,entry2,entry3,entry4
        entry1V=tk.StringVar()
        entry4V=tk.StringVar()
        
        label=tk.Label(self,text="Name",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry1=tk.Entry(self,bd=4,textvariable=entry1V)
        entry1.pack()
        
        label=tk.Label(self,text="Email",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry2=tk.Entry(self,bd=4)
        entry2.pack()
        
        label=tk.Label(self,text="Phone",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry3=tk.Entry(self,bd=4)
        entry3.pack()
        

        label=tk.Label(self,text="Password",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry4=tk.Entry(self,bd=4,textvariable=entry4V)
        entry4.pack()
        entry4.config(show="*");
        


        #button1=tk.Button(self,text="Visit Page 1",command=qf("Successs"))
       # button1=tk.Button(self,text="Visit Page 1",command=lambda:qf("Successs"))
        
        button=ttk.Button(self,text="Submit",command=lambda: [controller.show_frame(SuccessfulRegister),insert(entry1,entry4)])
        
        button.pack()
        #button.place(x=78,y=90)
       
        
        button2=ttk.Button(self,text="Reset",command=lambda: Reset(entry1,entry2,entry3,entry4))#controller.show_frame(PageTwo))
        button2.pack()
        #button2.place(x=88,y=95)
        
def  Reset(entry1,entry2,entry3,entry4):
    
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(0,'end')
    
    '''entry1.insert(' ')
    entry2.insert(' ')
    entry3.insert(' ')
    entry4.insert(' ')
    #entr'''
    


# In[266]:


class SuccessfulRegister(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label=tk.Label(self,text="You are Successfully Registered,Login To Continue",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button=ttk.Button(self,text="Login",command=lambda: controller.show_frame(Login))
        
        button.pack()
        


# In[267]:


class SuccessfulLogin(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        label=tk.Label(self,text="Welcome to Booking.com",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
            
        


# In[268]:


class Login(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        entry1V=tk.StringVar()
        entry2V=tk.StringVar()
        
       
        label=tk.Label(self,text="Login Page",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        #global entry1,entry2
        
        
        label=tk.Label(self,text="Username",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry1=tk.Entry(self,bd=4,textvariable=entry1V)
        entry1.pack()
        #print(entry1.get())
        
        
        label=tk.Label(self,text="Password",font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        entry2=tk.Entry(self,bd=4,textvariable=entry2V)
        entry2.pack()
        entry2.config(show="*");
        
        
        
        
        button=ttk.Button(self,text="Submit",command=lambda: [successful(entry1,entry2)])
        
        button.pack(pady=10)
        
       # button1=ttk.Button(self,text="Reset",command=lambda: controller.show_frame(SuccessfulLogin))
        
       # button1.pack()
    
        button3=ttk.Button(self,text="Reset",command=lambda: Reset1(entry1,entry2))
        button3.pack(pady=12)
        

        
        button2=ttk.Button(self,text="Go to Registration Page",command=lambda: controller.show_frame(StartPage))
        
        button2.pack()
        
def  Reset1(entry1,entry2):
    
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    
        


# In[ ]:


app=SeaofBTCapp()
app.geometry('500x500')
app.mainloop()

