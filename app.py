import streamlit as st 
#header
st.set_page_config(page_title="Wabepage", page_icon=":tada:", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>Ethiopian Super Food</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Teff Grain</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>[ጤፍ]</h1>", unsafe_allow_html=True)
#background color
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.shutterstock.com/image-photo/field-teff-grain-ethiopia-260nw-1062296012.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 



import streamlit as st

option = st.selectbox(
    '1',
    ('What is teff?','A) Smallest Size Cereal Grain in the World','B) Originated from Ethiopia','C) Ethiopia grew more than 90 percent of the world','D) Gluten Free','E) Highly Nitritious','F) Super Food','G) Replace Wheat Products'))

#ADD TABLE
import pandas as pd
df = pd.DataFrame({'Teff Yield in 2020/21': ['National', 'Oromia', 'Amhara', 'Tigay','SNNP','Benishagul 
Gumuz'],
                   'No of small Hoder Farmers': ['6,866,855.00', '2,861,364.00', '2,703,282.00', '633,525','1,224,860.00', '53,786.00'],
                   'Area(ha)': ['2,928,206.26', '1,393,455.62', '1,086,374.60', '188,391.88','234,350.83', '22,021.32'],
                   'Productio(qt)': ['55,099,615.14', '26,904,670.12', '20,964,629.06', '3,117,538.77','3,744,279.61', '334,445.20'],
                   'Yield(t/ha)': ['1.88', '1.93', '1.93', '1.66','1.60','1.60']})
df

#ADD TABLE
import pandas as pd
import streamlit as st
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "Cereal Crop": ['Teff', 'Corn', 'Wheat', 'Sorghum', 'Barley'],
            "Area Coverage (1000ha) in 2021/22 MY": ['2983', '2530', '1960', '1650', '960'],
        }
    )
st.checkbox("Use container width", value=False, key="use_container_width")
df = load_data()
df


#sidebar   
date = st.sidebar.date_input("Date")
text=st.sidebar.text_area("Write Comment Here")
st.write(text)
button1=st.sidebar.button("Submit Text")
uploaded_files=st.sidebar.file_uploader("Chose a csv file",accept_multiple_files=True)
for uploaded_file in uploaded_files:
      bytes_data=uploaded_file.read()
      st.write("filename:",uploaded_file.name)
      st.write(bytes_data)
            
#add file
st.write("##")
st.sidebar.text_input('Full Name')
st.sidebar.text_input('Email address')
st.sidebar.text_input('Phone No')

color = st.sidebar.color_picker('Pick Your Favorable Color', '#00f900')
st.sidebar.write('The current color is', color)

st.write("Developer Lemi Demissie PhD student @ Adama Science and Technology University") 
st.write("Phone:-+251921502282") 
st.write("Email:-   lemidemissieboset@gmail.com") 
st.write("Youtube:-https://www.youtube.com/channel/UCfuVnlEHBvqCMb67HecaNbw") 
st.write("<h1 style='text-align: center; color:white;'> Streamlit is the Fastest Way to Build and Share Data Apps🎈</h1>", unsafe_allow_html=True)



