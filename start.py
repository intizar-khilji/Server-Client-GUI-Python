import Server, Client
import threading
from tkinter import *

def server():
    server = Tk()
    obj = Server.Server(server)
    server.mainloop()
    
def client():
    client = Tk()
    obj = Client.Client(client)
    client.mainloop()

if __name__ == '__main__':

    t1 = threading.Thread(target = server)
    t2 = threading.Thread(target = client)
    t1.start()
    t2.start()
