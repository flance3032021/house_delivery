import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="car_price")
st.set_page_config(page_title= 'Car Delivery Price Calculation Project', initial_sidebar_state = 'auto')
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

total_price= 0

col3, col4= st.beta_columns(2)
bedrooms= col3.number_input('Enter number of bedrooms', 0, 100, 1)
if col3.checkbox('Assembly needed', key= '1'):
  bedroom_price= 200
else:
  bedroom_price= 120

kidrooms= col3.number_input('Enter number of kid rooms', 0, 100, 1)
if col3.checkbox('Assembly needed', key= '2'):
  kidroom_price= 150
else:
  kidroom_price= 100

livingrooms= col4.number_input('Enter number of living rooms', 0, 100, 1)
if col4.checkbox('Assembly needed', key= '3'):
  livingroom_price= 250
else:
  livingroom_price= 140

kitchens= col4.number_input('Enter number of kitchens', 0, 100, 1)
if col4.checkbox('Assembly needed', key= '4'):
  kitchen_price= 500
else:
  kitchen_price= 100

ac_windows= st.number_input('Enter number of AC wndows', 0, 100, 1)
acs= st.number_input('Enter number of ACs', 0, 100, 1)
floors= st.number_input('Enter number of floors', 0, 100, 1)

col1, col2= st.beta_columns(2)
time1= col1.time_input('Order time : ')
date1= col1.date_input('Order date : ')
place1= col1.text_input('Order location : ')
time2= col2.time_input('Pickup time : ')
date2= col2.date_input('Pickup date : ')
days= (date2-date1).days
place2= col2.text_input('Pickup location : ')

try:
  loc1= geolocator.geocode(place1)
  loc2= geolocator.geocode(place2)
  lat_lon1= (loc1.latitude, loc1.longitude)
  lat_lon2= (loc2.latitude, loc2.longitude)
  distt= geodesic(lat_lon1, lat_lon2).kilometers  
  
  st.write(f'The distance is {round(distt, 2)} kilometres.')

  total_price= (bedroom_price*bedrooms)+(kidroom_price*kidrooms)+(livingroom_price*livingrooms)+(kitchen_price*kitchens)+(ac_windows*50)+(acs*200)+(floors*50)+(distt*2)

  st.subheader(f'Total cost of transportation : {round(total_price, 2)}')  
  st.number_input('Insert your price')
except:
  pass
