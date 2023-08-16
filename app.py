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
df = pd.DataFrame({'Local Name          ': ['Bishoftu', 'Bora', 'Boset', 'Kora', 'Boni', 'Quncho', 'Dagim', 'Felagot'],
                   'Varieties           ': ['DZ-Cr-497 RIL133', 'DZ-Cr-453 RIL120B', 'DZ-Cr-409', 'DZ-cr-438 RIL133B', 'DZ-Cr-498 (RIL 37)', 'DZ-cr-387 RIL 355', 'DZ-Cr-438 RIL91A', 'DZ-Cr-442 RIL77C'],
                   'Releasing Center     ': ['DZARC', 'DZARC', 'DZARC', 'DZARC', 'DZARC', 'DZARC', 'DZARC', 'DZARC'],
                   'Year of Release      ': ['2020', '2019', '2012', '2014', '2021', '2006', '2016', '2017'],
                   'Days to Mature       ': ['94-110', '74-85', '75-90 ', '110-117 ', '112-115', '80-113', '116-144', '108-112'],
                   'Seed Color           ': ['Very White', 'Very White', 'Very White', 'Very White', 'Very White', 'Very White', 'Very White', 'Brown'],
                   'Yield t/ha                                  ': ['2.0-2.8', '1.8-2.4', '1.8-2.2', '2.0-2.3', '1.8-2.3', '2.0-2.2', '2.0-2.5', '1.9-2.4']})
  
df

#ADD TABLE
import pandas as pd 
df = pd.DataFrame({'Teff Yield in 2020/21                ': ['National', 'Oromia', 'Amhara', 'Tigay', 'SNNP', 'Benishagul Gumuz'],
                   'No. of small holder farmers              ': ['6,866,855.00', '2,861,364.00', '2,703,282.00', '633,525', '1,224,860.00', '53,786.00'],
                   'Area (ha)                              ': ['2,928,206.26', '1,393,455.62', '1,086,374.60', '188,391.88', '234,350.83', '22,021.32'],
                   'Production (qt)                            ': ['55,099,615.14', '26,904,670.12', '20,964,629.06', '3,117,538.77', '3,744,279.61', '334,445.20'],
                   'Yield t/ha                               ': ['1.88', '1.93', '1.93', '1.66', '1.60', '1.60']})
  
df

#ADD TABLE
import pandas as pd
import streamlit as st
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "Cereal Crop                                                                                                                 ": ['Teff', 'Corn', 'Wheat', 'Sorghum', 'Barley'],
            "Area Coverage (1000ha) in 2021/22 MY                                                                                        ": ['2983', '2530', '1960', '1650', '960'],
        }
    )

df = load_data()
df


#barChart
import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'index': ['Teff', 'Wheat', 'Maize', 'Sorghum', 'Barley'],
    'Cereal Crop vs Area Coverage (1000ha) in 2021/22 MY': [2983, 2530, 1960, 1650, 960],
}).set_index('index')

st.bar_chart(data)


#LineChart
import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'index': ['Teff', 'Wheat', 'Maize', 'Sorghum', 'Barley'],
    'Cereal Crop vs Area Coverage (1000ha) in 2021/22 MY': [2983, 2530, 1960, 1650, 960],
}).set_index('index')

st.line_chart(data)

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


 
import streamlit as st
from PIL import Image

image = Image.open('data:image/jpeg;base64,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')

st.image(image, caption='Sunrise by the mountains')
