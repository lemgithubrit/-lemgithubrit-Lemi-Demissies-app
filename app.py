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

#IMAGE
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   
   st.image(
            "https://png.pngtree.com/illustration/20220323/ourmid/pngtree-2-5d-flat-business-office-scene-vector-illustration-image_76264.jpg",
            width=270, 
        )
with col2:
  
   st.image(
            "https://previews.123rf.com/images/ingara/ingara1809/ingara180901228/110171575-big-data-vector-visualization-3d-futuristic-cosmic-design-technology-background-visual.jpg",
            width=300, 
        )

with col3:
   
   st.image(
            "https://images.prismic.io/impactio-blog/21d9a519-4bfa-4345-8810-50301c8bb84f_Methods+for+Presenting+Statistical+Data+in+an+Easy+to+Read+Way.png?auto=compress,format",
            width=250, 
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



















