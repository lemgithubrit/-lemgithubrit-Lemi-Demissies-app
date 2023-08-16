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


 

st.image(
            "https://media-cdn.tripadvisor.com/media/photo-s/0a/60/06/1b/yetsom-beyaynetu-the.jpg",
            width=200, 
        )

st.image(
            "data:image/jpeg;base64,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",
            width=200, 
        )


 c1,mid,c2 = st.beta_columns([2,1,3])
  for blob in blob_items:
  blob_client = container_client.get_blob_client(blob=blob.name)
  c1.image(blob_client.https://media-cdn.tripadvisor.com/media/photo-s/0a/60/06/1b/yetsom-beyaynetu-the.jpg)
  title = c2.text_input('Comments',key =blob_client.https://media-cdn.tripadvisor.com/media/photo-s/0a/60/06/1b/yetsom-beyaynetu-the.jpg )
  if c2.button('Save Me', key=blob_client.https://media-cdn.tripadvisor.com/media/photo-s/0a/60/06/1b/yetsom-beyaynetu-the.jpg):
      c2.write(title)





































