from tkinter import *
from tkinter import  ttk
import requests
from PIL import Image, ImageTk 


def data_get():
    
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4fbb253d5bc2c38c00c5dedea7bf30f7").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label2.config(text=data["weather"][0]["description"])
    temp_label3.config(text=str(int(data["main"]["temp"]-273.15)))
    pr_label4.config(text=data["main"]["pressure"])

win = Tk()
win.title("Met Report")
win.config(bg ="blue")
win.geometry("500x530+100+100")

# Load and display the background image
background_image = Image.open("/Users/bhavya/Downloads/pexels-pixabay-209831.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a Label to place the background image
background_label = Label(win, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adding the widgets 
name_label = Label(win,text="Meteorogical conditions",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=40,height=50,width=450)

city_name = StringVar()

list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Wscube Weather App",values=list_names,
                   font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman",18))
w_label.place(x=25,y=260,height=50,width=220)

w_label1 = Label(win,text="",
                   font=("Time New Roman",18))
w_label1.place(x=255,y=260,height=50,width=220)

wd_label = Label(win,text="Weather Description",
                   font=("Time New Roman",18))
wd_label.place(x=25,y=320,height=50,width=220)

wd_label2 = Label(win,text="",
                   font=("Time New Roman",18))
wd_label2.place(x=255,y=320,height=50,width=220)

temp_label = Label(win,text="Temperature",
                   font=("Time New Roman",18))
temp_label.place(x=25,y=380,height=50,width=220)

temp_label3 = Label(win,text="",
                   font=("Time New Roman",18))
temp_label3.place(x=255,y=380,height=50,width=220)

pr_label = Label(win,text="Pressure",
                   font=("Time New Roman",18))
pr_label.place(x=25,y=440,height=50,width=220)

pr_label4 = Label(win,text="",
                   font=("Time New Roman",18))
pr_label4.place(x=255,y=440,height=50,width=220)

done_button = Button(win,text="Done",
                     font = ("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200 ,y=190,height=50,width=100) 

win.mainloop()