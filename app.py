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
            "https://i.pinimg.com/originals/52/c0/bf/52c0bf4148d1e5e07bea49d878cd784a.jpg",
            width=200, 
        )
with col2:
  
   st.image(
            "https://e7.pngegg.com/pngimages/348/235/png-clipart-microsoft-excel-computer-icons-microsoft-template-angle.png",
            width=250, 
        )

with col3:
   
   st.image(
            "https://images.prismic.io/impactio-blog/21d9a519-4bfa-4345-8810-50301c8bb84f_Methods+for+Presenting+Statistical+Data+in+an+Easy+to+Read+Way.png?auto=compress,format",
            width=300, 
        )


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    
   
   st.image(
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgVFhYYGRgaHBocHBoYHBwcGhwcHBoaGRoaGh0cIS4lHB4rIRgYJjgmKzAxNTU1GiQ7QDs0Py40NTEBDAwMEA8QHhISHjQrJCs0NjQ0MTQ0NDQ0NDQ0NDE0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ/NP/AABEIAJ8BPgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAgMEBgcBAAj/xABDEAACAAQDBQUECQMCBAcAAAABAgADESEEEjEFBkFRcSJhgZGhEzKxwQdCUmJygrLR8BSS4aLSFkPC8RUjM0RTs+L/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/xAAhEQADAQACAwEAAwEAAAAAAAAAAQIREiEDMUFRBBNhMv/aAAwDAQACEQMRAD8A14mOiOER0CEB1hCPZwsx6GBwCPQuEEwgOiBe8+EM3CT0GpRqdVGYeqiCoj1IYGUbmSJcyRmdEZw1yygmhAPEc83lFoVALAADkBSKbu4fYYzFYRvdBZl1HuvQ/rBi3SJQVefHQD4dISGA94N4DKcSZKZ5zUtcha6AgXZuNLUFzD2CfF5FaYoz3zL2OZ+yeVOMDdy5Wd52Ja7s5UE8AaMaf3KOixbHYDUgdbRo2p6wz4uu9ImExKvwow1B16iJCIAKAAdIGbUXI6Thzyt3g/4r6QSM0Zgt6npT41hVKSVL0win3L9oWTEebilGhUnqfkDHsfKDIwPceJ0PIQNw0lQKZQPy09Kn1iDQlDHVJAqSPsp8C1a+UdlzJhJohtbtsPOgoPTjEpW04VH8+MKC3N7W4/KACG0l3lujlTmRloopQkEcYJbi4oPg05oWQ91GJHoRDapSvea/znAzcwlHxMn7MzMB3EkD0URNFT7LznEJM8QwqEx1ktElHpk4kGgr3c4zfezaSo6qcxAJqlSKcKHgBGkpQRXt4tgJOVmyEvSqgNlq3Cp5Rzefxc8f4HzEZbgcQvbVAF+s2XN2eQJ5d8D8V7RnPs2ZjXgR2RS+nARZpWDaTmUqvtlahIoCVpWx41r6RP2RMwhm5sThwxsMwzLSlu0gIB/msKPA/wDpff0zqGI3C3NGIf8AqJ9WRTaujMO/iBGsrgJYUKETKLAZRbpCdmTZLIvsCmQCgCUAXupw6RLjrnxpTj7ElhHTCKtMopThwhTyyeNofpHYaiV0kPkxoIRHDWHC0Kh8R6Ry0dDQ6aRwqIfEWjLueEdVjzhRURzLCwNFBzHmmUBJ0Fz0jwSBm8U/JJIrd+yPG59AYeMNRnm2ZhdpmJmk5KkheY0VR4AQ9sjBzMRKTNYAZjenaa9PAW7tOEDNozf6mYshD2K05Cgu7eQPlEve7aZlpLlyjluTbiAKfExYjXKR2PR6JATHI9HYQHIZnMQYehmeIAHJT1h2GJMOE0gAy3ejD+y2uj6Can6ly/qURYsO9RQwN+kyX2sPPUXQkV6EMo86w9LbKa/y+kCGwLui3spk/DPYhyyfeFKGn5Qh8TyizCSv2R8fjAjbmxvalZstsk5aUOmamgJFwRwPh0gptHHrRGkBjpnyk+JKtl+EaNcu0Qnx6YS264ISWPeZgQONNK+bQWpAXZezHz+3nnM/1VqOzwvS3OgGl+MF5ysR2TQ/zmDBTWKV8FKeun9FsoIIOhtDcvDovuqB4R5i2gAPeT8gL+kcdyoJYjuoKAeZMZmhHxEztdLQ2+JpqD4An4QyXrRgwofGtdKGHwtqwMEKWf3GBmwMYE2q8uhAmyQ3dVaAePYeB21d4KVWTQ83On5Rx66dYXj5mTH4DEA0VmKHo9FX/wCxvKC5pTrFNS3iNRMyukNEVh/JCaV0sOcYmyEBOEc/pgLkw6to9mgEZfvbhAmLelwyK19QdLHhpAoGtmvTjx/zFg3znL/UkVAbIorx4mnKAIQ8QKc108ovx+h0yTgcQ8tg0t2U9xofEaERbdmb6sKLPWo+2lj4jQ+FIpYlnhf+d8LD0sfWNsM2jXMHteRNHYmKTyJo3kbxMJjG1YdOkEMHtWdL9yYacq1HkbQYLDVAKQh5lIpGG3wmj30VxzFVPpUekFJG98k+8jr5MPjX0hcWIsAvDggZI2/hm/5gH4gy/ERMl7QlH3ZiH8y/vBgEkLHQIQJynRh5iFZxCA7GffSJtTtCUhuB2qcC3DyAi3bb2mJMstxNl60qT4D5RkmNnl3Zjck1J7zDQEndjA1cu3AG/Kup8qxXN49pCZOZh7g7K/hGnnc+MWbH4j2GFNLPM7I5hfrH5RU9mYBZuZpi1QWXkTxPy84G8Glp9IAR2PR6EITSOQqEmAD0JmLHHmARHmTOZiXSRSnReemkINTqYZaeIbaeekZttlpYBd/8LnwbtxllXHgaH9UBdlFMRhpLn3goGagJqvZOoPERZtpI0yU6EVqrCnOot8ooG4c4exmSmFfZTGFO40YWHfmi5ZNIuMp+HGPZGOrU/CKeprHlANCLennC2JoedNOfdFkCJ01UUs7AKNSfKFECvGpHfS3oIFYnFLNwpc9n2ikAXPavQVpzWJOGnlpUtwQKqpPlenfWKctLSVWvCRiZ4RGciygmg1NBWgilbb2oMVJdguUS3QgE1qGqtdLXPpBbEbYQzfYHMWJyk0ooqK8ddR5wA2Xhae2lm9UYU+8hqPnGvijO2vwy8tb0n+hrd+Zmw6WBK1XyYgf6aRB3h2trIQnk5H6B8/LnEndwjI6UoK15ainyjz7JDzHcEUJBNa60FfWsGTPkehtV41hXsPIAuak8oIb1Of6KVOWuaU6MOoqg9SvlB2Rs1B71TyvQeQ084j7yS0GEnLVQCpKhiAMy9tQK6kso84PN5ZpYg8PjqXrNBwuNV0R60DKrAdxAPzhE7aKjQVHP9op+6mPaZgZFTXKmQ/kJT5CCAm11sOlvCODcO5ILzNrV91fOAW395zISpDMx0VNYemT0U3YDrEI4qW5JDKxFrUJHXlC0aQHxOKmTVV2DoCLK9AwrwamvjENMNTQAfh7PwPygntyeqItXAYmoBtXqe6BcrFE8AehEef5nc03JvPFrGLditzde+hPyhyW4YW/eGMTPGW6lTwJFvOGkNb08Vj0P4vlqo2jn8kpPom+yB4eX7RxpR+15j5wws5+ebrr5iFpi269f3EdapfTPBaBxpfoa/G8OCf8AaDDqI4uIU6qPDWFpiU+2V61H6opUmJpiknIeI9YfQrz9YbVVbip8AfhCv6UfZT1EUiR9SOZ/nhEqQhOhNAKk2oBzMRsNs3ObLQDU5jQdY9tLEqirIl6E1YnU95PL4QN4IjbwYyoRF0p40J1PeaDyiJsnA52qbKLsYaymfNqPd4dyiw9InbexQkSPZrYsL9OMQMrG820TOnBU0rkQchxbyqYsm72FRUzOvYACKveLk+Ap/dFW3bwvtXacRUCqoO+lz/OcXacAoCDRLdTqx86xlT7NJRqlY5WBh2mNYG4vajuOwKrW+UjTrx6CE7RKlhnG7Slyx2mUHvIHmTEP/wAQLXFKHSmn+YETcEkwqXQOVuuYV16wQWU1Oyo7uHQd0Q6bLUpC3xTQnMTrHTJYCvprCMrUut+AGniYRQ4qcofVFGpuefyiHNmFaWJPJf5YREny0zq7kZzZKm4rqErxtw5QtDA2rKIynZY9jtPFyeDgOo/C1Pg8X9ny2rc98UPeZfZ7Uws4e7MUoTzqCo9QIuX2RS6LZImGl6eEIG0VPtQoOaVqDatswp5REdyAcgqxpxp3amwgdhNluWZ3cnNlrY1JStDU04GmkdEKfbZhTr1KHcG4OGmpYZHLKO40cU/1Q/sohpGQ3yO6+Fcw+MP7LwKKCpFSaXJJ0FBraoBPCHtp4lJSDO6qBpmNz0Gp8Iq7TTS/RTDT1/gGxOy804TdPdOgJqtLm/cNIeSQgcsDUknSupN9LAdYre09+ZCEhEmTG4ZiUTpQ9rzWK3jt78XMqFZZS8kFD4sanxFIl3TWaNRKe4aNMxSSlzOVlqb9tgPADTygHjt+sOlpYeae4ZVr1a58AYoOG2fNxD2DzWOpufN208TF22X9HuRQ+JnpIXkCCx/M1FB6ZozbLSBOM3sxcyoUpJXuFW82qT4AR7ZW7eJxXboziv8A6kxiAa37Japbwi84LC7MwxGRPavwmTO1fuzC35UgxJ2zMcgBco4UtYd7Xp0pE9spJIe3N3eOGwxlzGUlmLClaAGlu131PjBedsy1jHcM1ta/zmYez00t0rA4TGraIE3ZqtQEU77esDcQiH3AtBq4AGYj5QdnOWFCAQda2+EDZ8lALVAGgN1/eM68T+Gk+RfSh75yQFQ1FanrQjvirI1NPS3wi0b64RwqOFDKCbrrehrQxTfbLpoeRt8Yjg0uzn8j2m0FcNNdmC1NORNQYniXThT8Jp6QGwFM4IJtyP7QbWd316gGNfGkkXOtdikdh9b+7XzELDniPEX/AMwkTe4fzrHQy8iP53RoUKLDnTrb4woTSun7wR2ZsSbPuikL9tuyvhUdrwrFkwm6UlLzWMxuQGVfS58x0gwXLCmS8O7jMsvMLmqpW+nAXIpBvBbHmBVmOUWXqaE5j9zLwPA8oNbY2RJmqAFEt1FEdOyyU0oRwHIxUMXtmahMmZUOKh/ssw92YPxLc94POKSQm2ywbd24KAJQKF0FhpFbkIz5nJoPdr11p30t+YwKfElq8+P7xZ8PhwqIh+qASPvG59SYokf2fJCLXQC8UjeLEviZ4lJcvbog1J7otm3MaJck3pa/TjA3dfAZZZnuO3ONb/VT6q91r9TE08RUrWFtg4BZaAD3ZYt3tenjmqfCCWDUAGYwrU5QD5k/AecJMsgKgFyanqfdHgPiYlT5oSgFwLD5nxMZpaW3iDSYVjr6xJTBAaxMtDbMOp5RkUeRFGlOsLVOJJ+HoIjTH0NfKOywzWFesJPQaJLzFENtMrYWh6XgVGta84W2EHAxfBk8kQfZVOt4bXBL9btGpILUJFTotrDhBA4Q8CI4ZZUVoT6wnLKVIif0i8v5yii/SphaSpU5dZUxSPRh6iL5NemtvSK3vkVmYSaitVwuYcbqa18qxMvKQNaiOcbJlqHd0XMKgE1NDcUUXMANqb7S0qJSM55sci9aXJ9Irmyt3MXOAKIQp1ZwEQ99Gv5QcT6OXrmxGJRE5ga/3UA9Y6OSMcZW8TvZiXcHPkSt1ljLUdbt6x5GxGJqMPJd66uB8W90eJi94PYOz8Pl7Htm1DTCCNaVCkU8kMF5u2CFouVF0UqAARYCjNb1GkS6GpM7w/0dYk9qc6Sgb65mP+elYmf+AYXD1ORpzrxc5Ur0Ir/pg9icaXLVLZhUdmt6jUswrl1qcpGl4iHEGqmi5jWgTtMxr2gGrdfwsOkGseIgTdoYgAZEEpb2UBD5tVz4Ugekt3OYlnrqf3ZtehiwrhjUk5Re5btOfvZadfeCm+sTlwikAvcDi5oCe4DUdC0UmS0AMJh6Gg7J5IKn+4/KLTsrD0vTzNT/AN47hpSGyqW50GVfHn5CPbW2icOmdUVmJprYdSNfOG6SWsJl08RZJJ0/npDy3tFNwG9bOgzpkJ0K6Hu6xCxm8TZ2o57DKQQdR9ZT4Ri/KvhvP8dv2X15Qbss2XpVT5xw4VFFlEQdm7RSZJExmotK31HNTzgQnt3mmbndZKkZEXsggfaFbkm9TwoKXNdJtNaZXDl4N7xyy6kRnuP2Zc9mNHxGKcmjIG6WI66j4RGTAJMPLnRS5HggMGpk4ZYdnEG1R0qPhD+Hwc9mRJTOWY0VRcsToLxtGytkYQKWTI7L7xcVZTyKN7h8Im4fCSkbOkqWjn66oqtfUVArBg9wzTCbkbTzAP7JFOrMVNB0Qkk93rF72VuxIkgM/wD5r/acdkH7qaDxqYOvilIo1jziGxA+uCIaQnQ8+JiDPxFYZxM8DSBWI25LSzOoPLU+kUImvPFaMKfA+PAxm29M4tOdwScrZa8cq24a0pXzi0YnelKEKHax4ACvDWKa16k8YcoGL2eQ7pzLKPUBhF5K6mKNu/hqYlF4Zsw8Aaft5Re8ScqmGwRWNpy/6nFS8OPdrmf8KkW8WKjzi5TMOAVFLKKnoP4BFU3Eb2mMxMw3yhFXpVi3qIt+05lBlGrXPTgPnGVGkjeGJJZzroOp1PgPjCFk5yToosIU4yoqjU/O5+Qiob6bxGSUkSj2hdyOdNPWKlYiaes1j21dLDnDRepyipP814CFyMMzaDIPNvEiy9BfppBPD4ZUFhHPMtmrpIiYfAk3fy/eCCIAKCOkwhpg4RtMpejKqbFgR2GszHQQkyidTFEjjTBDbTY6JIh1UHKACKVLaivWI8/ZEtgcyKbGwtXutBWGxeEPszXHbUmYV/ZiS4lLZFqSygcBW5HnDcnbuGxNFd3lzH5E1BXm1CBzuBWNKxGGR1yuoZeTX+MVTae4mHmVyVQ8LZl/cecS0UqAeI2bMApKdSlK5jRpmYC2XN2BU8qGAswul3JBBKq84MHNrhAKVF9Cx10ifit2cdhatKdnUcLuPk4HpEaTvS6jLicPVdCQMynqKW8RCQPsYXO/ZCObaL2JYBvUVHZ61WJcgrQ5CM2mWX7teXtCAC3cc9axPkNgsSc4c2+rm7I8DUJ4ZYP4bDKoBRALUzC5I/FqfOGLALh9lO2UhfZAc7t30t2TzoAILJsdNfffm1b9b1PjWCCSTxiSiUigBRwb6EUHdp6aRXt6sQmUyB79M1eFgTSvSp8ovitGb74SGXEqWvncUP3WbKB4A08IyvpG3ix0BJlf6FqEgicoWnerZhXvHwgdg9nPPYIhoBTO3BR8yeXGLLs/Aq+HeU8xUHtQ19SFU1Cjh7wua+MO4Lb+GkEImHYqte0WqxPE8L98Ypo66T+C/wCpCMuGkoZjilU1C6duZTjp2OlY0fByqy1V1FaCo76XimYTenDy6iVh8gNzlVVJJ1zEXY98O4De13m5SuVD51+UUqSMK8bZZpuypRNXBYcFY1Qfl0PjWOTdoonZFABwFhEfEbRUoTXhASRhTMfO9Qg0H2uvdCdVTxAomVtBESEed/U0o5TJyqK1qRxOnhCtoYwykzGuWt6cK6evxh5IZSYk9HQXF1PQ6EetOkdMTiOeqTYAm7xMR2UJ72NIgTtpTm0cJ0BPr/iEzpBRmRtVJB/eGSaRriIIM93Y9t2PjbyEQnl0gjiZygXIEC5uKU2FW6A/GGIS4hsx3K7aIfGBm1XdGCgjNSpFK0HDxhOkhpaE9nYkJiJVTQ5xQ862I8j6Rbtuz8kpm7vlGWqjsyuzklSGHAWvGjb2t/5SLz/aEqVD4tewX9FsymJnIfrordcrGv64vGJ7c6nCor0GsZ/uMhXHKwtRJmb8OXj+bLF6lHtFq0HaJJ4cz5VjOl2NeiPtvaa4eW+IelRZBzb9hrGYbOUzWebMuXNb9Ye3r2ycViMiE+yl2Uc+Z6mJOETKoEWQfRmbgBHMp4nyiIgnr9dHH3lKHzUkekOLiWHvJTvVgV9aH0iQHJlB3mOoGpW3SkNSVLHMYkM1BWGA001cwU1DHTv6GHAp5mGJIqS510HcIccmtagDjUV9a2iWhpjq98drEYThrnXL/ONY4s77yGmtOXnDAlRwgRF9o3DKfzH9o8ztwA8/8QASDHqRHLtwH88YWpalTr4QAOAc4g4/Zkmb78tWPOlG/uF4lopjjkA0rTmT8ITGii7V+jtHOeUxVuFSVYdGH7QHXZO0cKSVLMg+1x/MmvjWNZjjOBqYMDTN8JviydnESmT71LeYFPQQal7yYdlzK9R92jfA0izTcWo74G4mbJb3paN+JFPxhqaFykrb70NMYphpTO33Rmp1IORfFvCKjv3tKZLyrOdDiKhlloc7S1uQzsKKprlIUDmYvO2ts+xl+zwygTXqERVFF5uV0oPjz0igYDdF0ZsRiiJk1ixyklhU17bk+83EDhxvYJr9HLe9ArYOKn5Hd0aYtaljUlc32yLBTS1eRg7sXCPiBNMtUVkCtRzQNmJFiBQG3GFYPFTMPmEtsualTQEkCtNfxGGHxLtXta6hQFBPMhQKxlifbOtU0sRBxG0pqPkYKCPqgKfIgkHwMWfYctXo7ZumWh8YHYDCVOkX3ZWysiFmHaI8hy6wcAryYiIpVuFu+JDTAASSABqSaAdTDElDQV1oK+URNvpXDzByWv8AaQ3yjWIWpHPdvGyNjdsiYCks9jQt9ruHd8Y7sjFZHFTY2PjofAxWdlPZh0Pnb5RatlbLLUdxReR1b9hHdUzEuTz5qrpNCN7cDMJWZKy37L1FT90i/UeAiutsLFOtmmHuUBfLs69YvG0tqJLU3zNWmVWIPO5U1Goiizt4cUHZvaMamwzEgdAY4X5OLw9GfHyWkvZW4k96PMQ5uGcgEDmaE3gtid1GlZcwU1r7tTSnUd8BMPvniVYZmNONILHf0NQOmYDnY+kJ+VN9gvC10iLtKUsiWzsNLAfabgP5wBigvh3di7irManxi+7WxSYsqyMeyP8A0yL95U8SbeAiHM2cFC5gBWn88Yzqt9FTGewFg9nArQe8QddB1EFt55tUSJ+FlUalNa8K0qbVPE+kV/eGfoK6VHkYrwvti8npBXczDgJNnEXJVF6Dtv8AFPKIm/W3PZSvYIe292pwTgPHXpBqVTDYRM9sqF3H3n7dOtwvhGS7TxbTprOxqWP8A/nCNPumT6WEzZEnjB2tIH4BKKIlM8USfQxeBb7aTOyOcuU0rwOlb8L11iTOmWisbUUFq5SCeNPidITAu0jEowGVhThf58YYmYgOxUGy69eUZ+uMMs9l6Hu+Y4wQwe8xQUyI161HYJPM0FCfCFpWFumu9OwFJ5MSop1APwhsYk0AZlRzwFWHcASBWASb1ClPZ/6//wAw3L3lOUhrn6tFAA/EM/a8xBqDiywtih/8iCljWmv9wpCva8MyV41tbhasAJG8hr26FfupQ+rmPJvBUjMkunE9qtOlD8YAxlgVjySvCnrekeSSDWqJ4f8AYQBm7cStAktlHuliwNOnsyB4GHJm2JYAVUVhqcpy0P5gK9YAD0pF0yU6GJoWA2yMUjnsih4itbdRbygwzQkJiZ7UU01Nh3Hn0Fz4QB21u4MSlDMdT2SDdiMotYmlTqTS5gszVNb30B4Dj5kehj02adBDzQ3AJuzJnSJDCawfL7hqSxWpu1Sb6aW4cIcm7SqRbXU1074Jlxp3aRBnbNVrqad2oi5xeyK1+iRlWnPv1hicingIjDZkz6rgDuJEODYrt77mnKph4v0Wv8AWKyhmZaE6ZuNBwry1iFOnM6dricteNOJ8BXyi0PuwhpV27xTXxtCcRu3WgDgLSlMnA2NO1aFblrEOE09ZQXwRNuZ48f4BEjB7MqeZJoBxtY9b1jQJOwJa3areg8hf1ifJw6IKIoUdw1684y4o35MA7F2KsvtuBm1C8u88zBjEsMjHuMSGAiBtGZ2MvM08r/KKI0DhreXqaRzE4bOjIbZlK15VFKw6EpCkY8eZ8ofrsN3oDytnYfCLnapOmZqsa6gAAUGh4QPxO9DOwSWCik0LH3z04LE/fAj2K/jH6WipSJbXIX81DQeMdU5wfkrtnLXL+xeOekO7Sc3Oa1PE/trAJ0t75vfv6DugvjpwRVXIrnQl6keA0gTPCMfdKHmhPwNRHm0+VOj1JXGVK+CJWHqbsx8bekLxcqgrmXoDeELMyimavhSImJmViBkrAY/Iwv0MW3B41cQFuA4N+8VFSO/W3fGdkxKwmMZDUGKSQtL7tWcJMp2JIsaX7VTYUPO49eUUr2wmT5MoDslpKsNaZygceBLRM2ji2xMrKG7aXC8GtTwbWnC5HGsCt0ULYuVY1TMz1FKFc5FvFBGnjWdmXk+Isf0kbSOVJan3qs3QGijzqfCM8krUjrFh33n5sQw+yFX0zH1YwDwi9sRovRk/YelWWENMhEyZQRDMyGSfR0yTXjA+fsjPqT4QZRaC8eK1g9rsfple/wCHEPEwzO3SRuJ8QD8otAWEu9ITxdsE2/RSpu5oW4cjxYeVGiINz5rGudlHAZ39bxfhLqat5Q5E8dev0XyxYjPzupPGjt/cT8RHDu1iR9c+a/7I0GO0EVxRPJmejd7E/b/T/thyVsDE195R1FfhF+yiPBYOIaDNh7PaSCWfMxFLCgHqTCd6tqPJw0x5d3A7NBmNaipC/WIFTQ2NIKuaCIkuXnbMbgc/T94H16Eu/ZVds7Q2oqymloufLWYhS1aLQAhjU0BqLAE8dYM7sYrEzEZ8TKEpq0Chq5rDt0qco4AdYOPXgLwmfpQcfhDE2JlipLc9OkKd8q95sIUvIQhrt3D48YGOUPyaAAQ4JkMkx6sGBo888AgcTC88DkNXLcBYfOJGaG0Sno+XhBaGax4NCwrRwiB+OIzCpFrDqYmtOAFajxgQUZ5gIHZWpHedK+ZEOZJdCnSIziCT4VyNPhEd8G/2TCKB5ccQDTSorEDeHFj2YVlqpNzW4I4DkaVgjicOy+8pFecV/bsgOqqXCUNb8bEcxzhNcuipedlWxyy1rR5hNbBqU8xSIDstSQWpyNG9bfCLH/wzOOoduPuEepMcxW5WIyl1WtBXKSobwveMalo6JtMq0yhFaU7ogzniZPllCQwIpwMQGSIKG48YUUhIMMkckOVNRFg2IymY01QA5XIfvCoNac+yLxXRBHZj5GzCBU0GJgTbuf2zl1ZSWJ7QpqeHOI+BbtRfsZiEnLlmKD4RVMbsgIcyG3IxtNpmNeN/Bua8RSYQyv8AZMM+2i0ZH1OFhUQ9mbXk4gZpT5x+Fl/UBExxbWkAYIeZwGseRKXNzA/GbVlSVJZja5sT8oqkv6UsESR26C+Yqb/OJSe6ym86Rfqx6KHJ+lLBMadv+0xb9l7Tlz0DyySCKioI+MUSTo9SPAR6GB4CO1j0JMAELa+JZJbMq5iB7o490ULH71YjNmlCbLtQq8oOvWsaJ7UGyip8vjDZB4ovn/iE4b+hNJGbpvvjF1eWfxynH6SImJ9IU8aph26OyejAxcs8rMQyCvG1RDszZUg6y0P5R+0S5pfSlUv4VCX9IMzjhlP4JyN/0xITf4/Wws38oVh6MINvuxhW1kyz+WnwiJO3JwhNRLy/hZh84WV+j2fwir9IMn68qavVD8mMPS/pBwZ1Zl6o/wDtgPjNx0DHJiMTL7g4YeR/eIJ3OnaLjm6PLB+ZjTjf+Ec4/wBLhh98MCdJ6D8VR+oCJsveHCt7uIlHo6/vFMG4uIIFZ8pjxzSl+QiPN3Hn8Bhm/Ky/AxDqvwtKf00Rdoyjo4PS/wAI8Z0o6svjb4xk+M3TnrrhpR70mFf1ExAbCMn/AC5q/gnL+whc2vgcE/psZeQfrp/cP3h2SqA1Qr4NX5xixxcwf8zFL1dW/wCuPLtVh/7px+OUjfMwf2/uh/WjcQxj3tDGKy9uzB7uJQ/ilsv6FiXL2/i/qzJbdDOX/qEHOR8KNSxqFzU8oqu39jvMYFQKBaagXr/2ivf8T40cFPRn+bx0764ke8gP5h8wYqfLMvUTXiprGFsHisZIergzEqKhiKgcwwvBPH7yM6FMmWutCa05RVH36mfWkKfzfssRpm+YPvYdPBz/ALIVUqY4niE8c8gymbEIGoRQqSGA5VB5xm2OnorDJmIOoNCVPKo1izbU2yJy0VAoJFbkkUvawiq5ba84ybWmvbQ5IxQa3HvhzjAlh2gBwgtsnCTJ80SZS53NaCqr7oLG7EDQGG5/BKv0dRYkoYhTSVYq1mBNtdLEWtC0mxm0apk/2scz1qToOHM8BEUPC0bTrWKidZF1kk1MOCKnU+kQ5+Elk6A98Spk3s0iOI6DmP/Z",
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



















