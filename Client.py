from tkinter import *
from socket import *
from threading import *
from tkinter import messagebox


class Client:
    def __init__(self, root):
        self.root = root
        self.root.title('Client')
        self.s = None
        self.font = ('Times New Roman', -25, 'bold')
        self.f1 = Frame(self.root)
        self.f1.propagate(0)
        self.f1.grid(row=0, padx=2, pady=2)
        self.l1 = Label(self.f1, text='HOST', width=20, font=self.font)
        self.l2 = Label(self.f1, text='PORT', width=20, font=self.font)
        self.l3 = Label(self.f1, text='STATUS', width=20, font=self.font, fg='white', bg='red')
        self.l4 = Label(self.f1, text='CONNECTED WITH', width=20, font=self.font)
        self.lname = Label(self.f1, text='NAME', width=20, font=self.font)
        self.b3 = Button(self.f1, text='NOT CONNECTED', width=16, font=self.font, command=self.connect)
        self.e1 = Entry(self.f1, width=20,  font=self.font)
        self.e2 = Entry(self.f1, width=20, font=self.font)
        self.e3 = Entry(self.f1, width=20, font=self.font)
        self.e4 = Entry(self.f1, width=20, font=self.font)
        self.name = Entry(self.f1, width=20, font = self.font)
        self.name.insert(0, 'Client')
        self.e1.insert(0, '127.0.0.1')
        self.e2.insert(0, '9999')
        self.e4.insert(0, 'Not Connected')
        self.lname.grid(row=0, column=0, padx=2, pady=2)
        self.l1.grid(row=1, column=0, padx=2, pady=2)
        self.l2.grid(row=2, column=0, padx=2, pady=2)
        self.l3.grid(row=3, column=0, padx=2, pady=2)
        self.l4.grid(row=4, column=0, padx=2, pady=2)
        self.name.grid(row=0, column=1, padx=2, pady=2)
        self.e1.grid(row=1, column=1, padx=2, pady=2)
        self.e2.grid(row=2, column=1, padx=2, pady=2)
        self.b3.grid(row=3, column=1, padx=2, pady=2)
        self.e4.grid(row=4, column=1, padx=2, pady=2)

        self.f2 = Frame(self.root)
        self.f2.propagate(0)
        self.f2.grid(row=1, padx=2, pady=2)
        self.t1 = Text(self.f2, width=70)
        self.t1.grid(row=0)

        self.f3 = Frame(self.root)
        self.f3.propagate(0)
        self.f3.grid(row=2, padx=2, pady=2)
        self.msg = Entry(self.f3, font=self.font, width=30)
        self.send = Button(self.f3, width=10, text='Send', font=('Times New Roman', -20, 'bold'), command=self.send)
        self.msg.grid(row=0, column=0, padx=2, pady=2)
        self.send.grid(row=0,column=1, padx=2, pady=2)

        t = Thread(target=self.recv)
        t.start()

        self.root.protocol('WM_DELETE_WINDOW', self.onclose)

    def connect(self):
        try:
            self.s = socket()
            self.s.connect((self.e1.get(), int(self.e2.get())))
            self.e4.delete(0,END)
            self.b3.config(text='Connected')
            self.e4.insert(0,self.e1.get())
            self.l3.config(bg='green')
        except:
            messagebox.showwarning('Connection Error','Connection not astablished.')
        

    def send(self):
        try:
            self.t1.insert(END, 'You : '+self.msg.get()+'\n')
            s = self.name.get() +' : '+ self.msg.get()
            self.s.send(s.encode())
            self.msg.delete(0,END)
        except:
            messagebox.showerror('Connection Error','Something going wrong.\nPlease check the connection.')

    def recv(self):
        while True :
            try :
                str = self.s.recv(1024).decode()
                if str == '123321.....!@#$CLOSE$#@!......123321':
                    self.e4.delete(0,END)
                    self.b3.config(text='NOT CONNECTED')
                    self.e4.insert(0, 'Not Connected')
                    self.l3.config(bg='red')
                else:
                    self.t1.insert(END, str+'\n')
                    str = None
            except :
                pass

    def onclose(self):
        try:
            self.s.send(b'123321.....!@#$CLOSE$#@!......123321')
            self.s.close()
        except:
            pass
        finally:
            self.root.destroy()
