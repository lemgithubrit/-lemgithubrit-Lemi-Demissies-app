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
            "data:image/png;base64,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",
            width=250, 
        )

with col3:
   
   st.image(
            "https://pbs.twimg.com/media/EO2jMN0UwAAf3KR.jpg",
            width=250, 
        )
















