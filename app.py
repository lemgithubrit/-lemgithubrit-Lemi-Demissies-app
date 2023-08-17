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

#IMAGE
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   
   st.image(
            "https://s3.amazonaws.com/blog.oxfamamerica.org/firstperson/2014/07/ethiopia-farmers-harvest-teff-OUS_27075-1220x763.jpg",
            width=250, 
        )
with col2:
  
   st.image(
            "https://www.saa-safe.org/newsfiles/images/images/unnamed%20%281%29.jpg",
            width=250, 
        )

with col3:
   
   st.image(
            "https://vinmec-prod.s3.amazonaws.com/images/20210307_112944_143714_hat-teff.max-1800x1800.jpg",
            width=250, 
        )

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    
   
   st.image(
            "https://agtfoods.co.za/wp-content/uploads/2018/06/White-Teff-Flour_600x600_4.jpg",
            width=250, 
        )
with col2:
  
   st.image(
            "https://agtfoods.co.za/wp-content/uploads/2018/06/White-Teff-Flour_600x600_3.jpg",
            width=250, 
        )

with col3:
   
   st.image(
            "https://pbs.twimg.com/media/EO2jMN0UwAAf3KR.jpg",
            width=250, 
        )
    
    
st.write("Developer Lemi Demissie PhD student @ Adama Science and Technology University") 
st.write("Phone:-+251921502282") 
st.write("Email:-   lemidemissieboset@gmail.com") 
st.write("Youtube:-https://www.youtube.com/channel/UCfuVnlEHBvqCMb67HecaNbw") 
st.write("<h1 style='text-align: center; color:white;'> Streamlit is the Fastest Way to Build and Share Data Apps🎈</h1>", unsafe_allow_html=True)

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    
   
   st.image(
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAk1BMVEX///8Yd/IAcvLg5/xRivNbkPTk7P0Ab/EAZvFrmfX7/P+wx/kAafGkvPi6z/mvyfoAY/AAbfIMdfL1+P7t8/4AXPAAX/CRtPdek/Ta5fzR3fvr8f3i6/3L3vzC1/u90/p6ovU+hfOJrvZwoPUAUvAge/J6p/Y6ePM8i/QygPNgmvWhwfiuyPqMrPbV4/yArPeiufhFRnHNAAADrElEQVR4nO3bbXOiMBiFYaFWMGKRaFV8QdFi19p2/f+/bnVfZtruUAI0k/N0zv3JL8zkGkKiAp0OY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHG3qYm6TrbbDZZtk6XY6Vcj+cLU8tstu36o/v76ejadHp/+Rh5eX87O92lvYlo7EW3y6NRlPjae5/WfpBE0Wga6ry/ixcT10Ntkpqs9zqMfO/zLtRo9BC7Hm39xqtTHiYfT11Z4Z3r8dZNpcMirDp7koW9QV45OyULVdYPgjo+acLJME/q+YQJVwev1gQVJ0zn/+1930uY5kEDoCBh77HmEiNNqPxmQDnCH7UXUWHCXVOgFGFs/DVUqHB5bAwUIjw02QglCbOi/lcZUcLxUwugCGFcNJ+jIoTjfcO9Xoxwc2wzSQUIVfPNXogwnbeapAKEcSufAOG45STFF7adpPjCrNZmqP0kCt+H/p+3OpmfQp1Mw3w7Oz3Hb3u+cW34vMmL6WWoo8fZq8CbTaaXofaPA9djbdbC7Jehr38KPH2/2xgC0RfM0lRsMkkFAztqGBkIk2fX42zeeGYgTA5Sr8FLy0P1ZqE98B3v03pP1ddhOBN8Cjur6u1Q64XrUbbp5rby933QX7oeZZtuupXC6Dx2Pco2mQjl7oXXqoXaW7seZKuqhX6euh5kqwyEXcm7oZHwduV6kK0yEX7/c0ghdhRSiB+FFOJHIYX4UUghfhRSiN/3F64MhD3Xg6xssuqVlhn817YoP/zSyv1tGzW47Zc2LyqAnlfMyw+/tHd/V0Odp0FpJs9d+uWHB0E4BxAa3chuWrJz/6KzXWE0c39nyq5wFAOsNFaFYebaZ1moi1fXPstCfw5w38aqMNm63yzsChGWUsvCgful1KpQBwiPMVgVFgCbhVWh3wXYLKwKgz7AZmFVmBzcf++2K4zOAEupTaEOIB4etiksNq511ywK/S7Eo6cWhcEc4pk3m8I9xD+NFoXJC8D3brvX4RBhs7Ao1B7Gq4cWhUeIzcKiEGSzsCgM+hBLqU3hAWIptTlLQV4XsrjSDF3b/qTOD2FpUfUrpPrj6+n/GiUn17a/vZ4GpZ0rXwPW+bDs4BjhB/41VV4nNbqPX3q4gPi+hfxnMSikED8KKcSPQgrxo5BC/CikED8KKcSPQgrxo5BC/CikED8KKcSPQgrxo5BC/CikED8KKcSPQgrxo5BC/CikED8KKcSPQgrxo5BC/CikED8KKcSPQgrxo5BC/CikED8A4S8vfFf6uDkE/wAAAABJRU5ErkJggg==",
            width=50, 
        )
with col2:
  
   st.image(
            "https://static.vecteezy.com/system/resources/previews/017/221/781/non_2x/telegram-logo-transparent-free-png.png",
            width=50, 
        )

with col3:
   
   st.image(
            "https://pbs.twimg.com/media/EO2jMN0UwAAf3KR.jpg",
            width=250, 
        )
















