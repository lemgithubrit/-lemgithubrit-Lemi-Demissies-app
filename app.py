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
                   'No. of small holder farmers              ': [6866855, 2861364, 2703282, 633525, 1224860, 53786],
                   'Area (ha)                              ': [2928206.26, 1393455.62, 1086374.60, 188391.88, 234350.83, 22021.32],
                   'Production (qt)                            ': [55099615.14, 26904670.12, 20964629.06, 3117538.77, 3744279.61, 334445.20],
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



import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})


#IMAGE
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   
   st.image(
            "data:image/jpeg;base64,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",
            width=250, 
        )
with col2:
  
   st.image(
            "https://previews.123rf.com/images/ingara/ingara1809/ingara180901228/110171575-big-data-vector-visualization-3d-futuristic-cosmic-design-technology-background-visual.jpg",
            width=280, 
        )

with col3:
   
   st.image(
                          "data:image/jpeg;base64,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",
            width=300, 
        )


st.write("")
st.write("")
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    
   
   st.image(
            "https://img.freepik.com/premium-vector/social-media-icon-illustration-facebook-facebook-icon-vector-illustration_561158-2134.jpg?w=2000",
            width=60, 
        )
with col2:
  
   st.image(
            "https://w7.pngwing.com/pngs/284/690/png-transparent-telegram-logo-computer-icons-telegram-logo-blue-angle-triangle-thumbnail.png",
            width=60, 
        )

with col3:
   
   st.image(
            "https://e7.pngegg.com/pngimages/759/922/png-clipart-telephone-logo-iphone-telephone-call-smartphone-phone-electronics-text.png",
            width=60, 
        )   

import streamlit as st
col1, col2, col3 = st.columns(3)
with col1:
  st.write("Facebook:-Lem Messa Demissie")
with col2:
    st.write("Telegram:-+251921502282")
with col3:
    st.write("Phone:-+251921502282")
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

st.write("<h1 style='text-align: center; color:white;'> Streamlit is the Fastest Way to Build and Share Data Apps🎈</h1>", unsafe_allow_html=True)



st.image(
            "https://iconscout.com/lottie/data-analysis-system-4308565",
            width=1200, 
        )   









