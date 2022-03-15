from urllib.request import urlopen
from bs4 import BeautifulSoup
import tkinter as tk
import time
#urls  
urls = ('https://www.geeksforgeeks.org/',"https://uzgrow.uz/")
root= tk.Tk()
master = tk.Canvas(root, width = 500, height = 500)
master.pack()

label1 = tk.Label(root, text="Iltimos 'https' yoki 'http' mavjud manzillarni kiriting!\n Agar bittadan ko'p manzil kiritsangiz,\n orasini vergul (,) bilan ajrating!")
e1 = tk.Entry(master,width=50,)


master.create_window(250, 70, window=e1)
master.create_window(250, 30, window=label1)
def show():
    a=170
    global e1
    urls = e1.get()
    for url in urls.split(","):
        try:  
            a+=40
            soup = BeautifulSoup(urlopen(url))
            label2 =tk.Label(root, text=f"'{url}' web sahifasi nomi:\n{soup.title.get_text()}")
            master.create_window(250, a, window=label2)
        except:
            label3 =tk.Label(root, text=f"'{url}' - bunday url mavjud emas! Tekshirib ko'ring!")
            master.create_window(250, a, window=label3)
            
button = tk.Button(root, 
          text='Show', command=show)
master.create_window(250, 100, window=button)
tk.mainloop()

    
