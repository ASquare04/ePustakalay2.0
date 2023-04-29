import requests
from customtkinter import *
import customtkinter as custom

custom.set_appearance_mode("Dark")

def Generate():
    global f1
    a1 = auth.get()
    b1 = choice.get()
    query = a1 + " " + b1
    
    # set the API endpoint and parameters
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    total_items = data.get("totalItems")
    result = CTkTextbox(
        root,
        font=custom.CTkFont(size=14, family="Times New Roman"),
        width=620,
        height=350,
        fg_color="black"
    )
    result.place(x=90, y=300)
    
    items = data.get("items")
    for item in items:
        volume_info = item.get("volumeInfo")
        title = volume_info.get("title")
        authors = volume_info.get("authors")
        t1 = "Title: " + title 
        a1 = "Authors: " + (', '.join(authors) if authors else "Unknown Author")
        result.insert("end", t1 + "\n" + a1 + "\n\n")
    
    btn = CTkButton(
        root,
        text="Exit",
        command=root.destroy,
        font=custom.CTkFont(size=14, family="Times New Roman"),
        fg_color="red"
    )
    btn.place(x=330, y=700)
        
def Bot():
    
    global root
    root = custom.CTk()
    root.geometry("800x780+510+95")    
    root.resizable(0,0)
    root.title("Recommender")

    title = custom.CTkLabel(root,text="Enter Prefrence To Generate Result",font= custom.CTkFont(size=18,family="Times New Roman"))
    title.pack(padx=10,pady=15)
    
    l1 = custom.CTkLabel(root,text ="Book Name or Author : ",font = custom.CTkFont(size=16,family="Times New Roman"))
    l1.place(x=220,y=85)
    
    global auth
    
    auth = custom.CTkEntry(root, width=180)
    auth.place(x=420,y=85)
    
    l1 = custom.CTkLabel(root,text =" OR ",font = custom.CTkFont(size=22,family="Times New Roman"))
    l1.pack(padx=10,pady=65)
    
    l2 = custom.CTkLabel(root, text="Choose Book Genres : ", font=custom.CTkFont(size=16,family="Times New Roman"))
    l2.place(x=220,y=160)
    
    global choice
    
    choice = custom.CTkComboBox(root, font=custom.CTkFont(size=14,family="Times New Roman"), values=['','Programming','Fiction','Romance','Thriller','Biogragphy','Comedy'], width=180)
    choice.place(x=420,y=160)
    
    btn = CTkButton(root, text= "Fetch Results",fg_color="purple",hover_color= "green", command=Generate,font=custom.CTkFont(size=14,family="Times New Roman"))
    btn.place(x=330,y=220)
    
    root.mainloop()

Bot()