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
                          "https://visme.co/blog/wp-content/uploads/2021/08/Data-Visualization-thumbnail.jpg",
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
            "https://i.gifer.com/74pZ.gif",
            width=300, 
        )   









