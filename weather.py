from tkinter import *
import requests
from tkinter import messagebox
window =Tk()
window.geometry('550x200')
window.title("Weather App")
window.config(bg="yellow")

def test_function(entry):
    print("This is the entry:", entry)
def formatresponse(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humid = weather['main']['humidity']
        feel = weather['main']['feels_like']
        winds = weather['wind']['speed']
        cloud= weather['clouds']['all']

        if showbtn:
            final = 'Place: %s \nSky: %s \nTemperature: %s \nFeels like: %s\n humditiy: %s\n Wind speed: %s\n Cloud cover: %s '%(name, desc, temp, feel, humid, winds, cloud)

    except:
        messagebox.showinfo('ERROR','Please enter a valid city')

    return final

    # GETTING WEATHER INFO
def check(city):
    weatherkey = 'f5794d360a817b45f1032a121e890b49'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weatherkey, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = formatresponse(weather)


def exit():
    window.destroy()
#canvas = Canvas(window, bg='light grey')
#canvas.pack()

f1 = Label(window)
f1.grid(row=1, column=1)

en1 = Entry(f1, font=30)
en1.grid(row=1, column=2)

showbtn = Button(f1, text="Show", command=lambda: check(en1.get()))
showbtn.grid(row=1, column=4)

exitbtn= Button(window, text="Exit", command=exit)
exitbtn.grid(row=1, column=5)


label = Label(window)
label.grid(row=2, column=1)
window.mainloop()
