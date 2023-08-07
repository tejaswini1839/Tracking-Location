import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import tkinter
from tkinter import *
from geopy.geocoders import Nominatim
git number = entry.get()
 ch_number = phonenumbers.parse(number)
 service = phonenumbers.parse(number)
 country= geocoder.description_for_number(ch_number,"en")
 provider=carrier.name_for_number(service,"en")
 geolocator=Nominatim(user_agent="loaction tracing")
 location=geolocator.geocode(country)
 print("country:",country)
 print("service provider:",provider)
 print("latitude:",location.latitude)
 print("longitude:",location.longitude)
root = Tk()
root.title("Tracing Location")
root.geometry("500x300")
global entry
Label(root,text="Enter mobile number").place(x=50,y=20)
entry= Entry(root,bd=5)
entry.place(x=250,y=20)
Button(root,text="TRACK",command=track,height=2,width=13,bd=6).place(x=160,y=120 )
root.mainloop()
