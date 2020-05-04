import requests
from tkinter import *
from tkinter import messagebox as m_box

#city_name_list=["Mumbi","Indore","Pune","Bhopal","Delhi","Chandigarh","Rewa","Ahmadabad","Surat"]

def read():
    filename = "City.txt"
    with open(filename) as f:
        lines = f.read().splitlines()
        f.close()
    city_name_list =list(lines)
    
    return city_name_list
    #print(city_name_list," List of city")

def write(l1):
    f=open('City.txt','w')
    s1='\n'.join(l1)
    f.write(s1)
    f.close()


def weather():
    try:
        city = city_listbox.get()
        
        url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
        res = requests.get(url)
        output = res.json()

        w_status = output['weather'][0]['description']
        temp = output['main']['temp']
        humidity = output['main']['humidity']
        w_speed = output['wind']['speed']

        w_status_label.configure(text="weather status: "+ w_status)
        temp_status_label.configure(text="temprature: "+ str(temp))
        humidity_label.configure(text="humidity: " + str(humidity))
        windspeed_label.configure(text="Wind Speed: " + str(w_speed))
    except:
        city_name_list.remove(city)
        write(city_name_list)
        #print(city_name_list)
        m_box.showerror('Error','Some Error Occured Please Try Again')
        window.destroy()



window = Tk()

window.geometry("400x450")

name_label = Label(window,text = 'Search for Weather Information', font=('Helvetica', 14))
name_label.grid(row=2,column=2)

city_listbox=StringVar(window)
city_name_list = read()

city_listbox.set("Select City")
option = OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=4,column=2,padx=150,pady=10)

b1 = Button(window,text="GO",width=15,command = weather)
b1.grid(row=6,column=2,padx=150)
print(b1)

w_status_label = Label(window,font=('times',10,"bold"))
w_status_label.grid(row=10,column=2)
temp_status_label = Label(window,font=('times',10,"bold"))
temp_status_label.grid(row=12,column=2)
humidity_label = Label(window,font=('times',10,"bold"))
humidity_label.grid(row=14,column=2)
windspeed_label = Label(window,font=('times',10,"bold"))
windspeed_label.grid(row=16,column=2)
    
window.mainloop()