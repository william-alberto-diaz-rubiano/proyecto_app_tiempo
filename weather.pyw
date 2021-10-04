from tkinter import *
import requests

def weather_json(city_name):
    try:
        Api_key="19e8de8395191edfb417be204cc88b92"
        Api_url="https://api.openweathermap.org/data/2.5/weather"
        parameters={"appid":Api_key,"q":city_name,"units":"metric","lang":"es"}
        response=requests.get(Api_url,params=parameters)
        weather=response.json()
        show_weather(weather)
    
    except:
        print("error")

    

   
   
def show_weather(weather):
    try:
        name_city=weather["name"]
        main_weather=weather["weather"][0]["main"]
        description=weather["weather"][0]["description"]
        tem=weather["main"]["temp"]
        pressure=weather["main"]["pressure"]
        humidity=weather["main"]["humidity"]

        show_city["text"]=name_city
        show_temp["text"]=str(int(tem))+" C°"
        show_main["text"]=main_weather
        show_description["text"]=description
        show_pressure["text"]=str(pressure)+" Pascales"
        show_humidity["text"]=str(humidity)+" %"

    except:
        show_city["text"]="Revisa el nombre de la ciudad \n y vuelve a intentarlo"



window=Tk()
window.geometry("500x700")
window.config(bg="#74DF00")

text_city=Entry(window, font=("courrier",20,"normal"),justify="center")
text_city.pack(padx=30, pady=30)

get_weather=Button(window,text="Obtener clima",font=("courrier",20,"normal"),command=lambda:weather_json(text_city.get()),bg="#FF8000")
get_weather.pack()

show_city=Label(font=("courrier",20,"normal"),bg="#74DF00")
show_city.pack(padx=20,pady=20)

show_temp=Label(font=("courrier",30,"normal"),bg="#74DF00")
show_temp.pack(padx=10,pady=10)

show_main=Label(font=("courrier",15,"normal"),bg="#74DF00")
show_main.pack(padx=15,pady=15)

show_description=Label(font=("courrier",15,"normal"),bg="#74DF00")
show_description.pack(padx=10,pady=10)


show_pressure=Label(font=("courrier",15,"normal"),bg="#74DF00")
show_pressure.pack(padx=10,pady=10)

show_humidity=Label(font=("courrier",15,"normal"),bg="#74DF00")
show_humidity.pack(padx=10,pady=10)

window.mainloop()