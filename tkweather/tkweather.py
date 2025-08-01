# Weather Program by Travis Bare

# This program gets json info from 2 apis from OpenWeatherMap.org and displays
# weather information to the user.

import requests # imports the requests module which must be separately 
                # installed.
import customtkinter # more modern version of tkinter

# Set the theme and color options
customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title("Weather Report")


def report(city, state):
    # print(city,state,country)
    entry_city.delete(0, 'end')
    entry_state.delete(0,'end')
    # entry_country.delete(0,'end')

    apikey = "7545be23dce3cfbc78f1895dc0e38158"
   
    try:
        georesponse = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&limit=5&appid={apikey}")
    except:
        print("Error: Internet connection problems.")

    # testing statements
    # print(georesponse.json())
    # print("*************************")

    geo_json = georesponse.json()

    name = geo_json[0]["name"]
    state = geo_json[0]["state"]
    lat = geo_json[0]["lat"]
    lon = geo_json[0]["lon"]

    my_city = City(name, state, lat, lon) # creates a city object

    my_city.temp_print()
    textbox.delete("0.0", "end")
    textbox.insert("0.0", my_report)


class City:
    def __init__(self, name, state, lat, lon, units="imperial"):
        self.name = name
        self.state = state
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={self.lat}&lon={self.lon}&appid=7545be23dce3cfbc78f1895dc0e38158")
        except:
            print("Error: Internet connection problems.")

        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.description = self.response_json["weather"][0]["description"]

    def temp_print(self):
        global my_report
        # print(f"In {self.name}, it is currently {self.temp}°F")
        # print(f"Today's high: {self.temp_max}°F")
        # print(f"Today's low: {self.temp_min}°F")
        # print(f"Description: {self.description}")
        line1 = f"In {self.name}, {self.state}, "
        line2 = f"it is currently {self.temp}°F"
        line3 = f"Today's high: {self.temp_max}°F"
        line4 = f"Today's low: {self.temp_min}°F"
        line5 = f"Description: {self.description}"
        my_report = line1 + "\n" + line2 + "\n\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n"
        return my_report

# interface layout
frame_top = customtkinter.CTkFrame(master=root,height=800,width=500,border_width=3)
frame_top.grid(row=1,column=0)

frame_bottom = customtkinter.CTkFrame(master=root,height=800,width=500, border_width=3)
frame_bottom.grid(row=2,column=0)

# top frame widgets
label_main = customtkinter.CTkLabel(frame_top, text="Weather Report", font=("Arial",30),padx=50, pady=30, fg_color="transparent")
label_main.grid(row=0,column=0, columnspan=2, pady=15)

label_city = customtkinter.CTkLabel(frame_top, text="Enter City:", font=("Arial",12),padx=5, pady=5, fg_color="transparent")
label_city.grid(row=1,column=0, sticky="e")

entry_city = customtkinter.CTkEntry(frame_top, placeholder_text="city")
entry_city.grid(row=1,column=1, sticky="w")

label_state = customtkinter.CTkLabel(frame_top, text="Enter State:", font=("Arial",12),padx=5, pady=5, fg_color="transparent")
label_state.grid(row=2,column=0, sticky="e")

entry_state = customtkinter.CTkEntry(frame_top, placeholder_text="state")
entry_state.grid(row=2,column=1, sticky="w")

# label_country = customtkinter.CTkLabel(frame_top, text="Enter Country Code:", font=("Arial",12),padx=5, pady=5, fg_color="transparent")
# label_country.grid(row=3,column=0, sticky="e")

# entry_country = customtkinter.CTkEntry(frame_top, placeholder_text="can leave blank")
# entry_country.grid(row=3,column=1, sticky="w")

button_report = customtkinter.CTkButton(frame_top, text="Get Report", command=lambda: report(entry_city.get(),entry_state.get()))
button_report.grid(row=5, column=0, columnspan=2, padx=160, pady=30)

# bottom frame widgets
label_report = customtkinter.CTkLabel(frame_bottom, fg_color="transparent",text="Your report:", font=("Arial",18),padx=10, pady=10)
label_report.grid(row=0,column=0, columnspan=2, pady=10)

textbox = customtkinter.CTkTextbox(frame_bottom, font=("Arial",18), width=400, padx=20, pady=20)
# textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
# textbox.delete("0.0", "end")  # delete all text
# textbox.configure(state="disabled")  # configure textbox to be read-only
textbox.grid(row=1, column=0, columnspan=2, padx=30,pady=30)




    
root.mainloop()


