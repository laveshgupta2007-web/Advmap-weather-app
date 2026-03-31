import streamlit as st
import requests

import streamlit as st
import requests

# Google verification tag (IMPORTANT)
st.markdown("""
<meta name="google-site-verification" content="LfImxwelyzqihg4Xw-FHabajGjfo5soZGvrDMPwUOio" />
""", unsafe_allow_html=True)

API_KEY = "af240cca6083b79def74e9d0b9b992e9"

st.title("🌤 Live Weather Dashboard")

city = st.text_input("Enter City Name")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        st.metric("🌡 Temperature", f"{temp} °C")
        st.metric("💧 Humidity", f"{humidity}%")
        st.write(f"☁️ Condition: {weather}")

    else:
        st.error(f"Error: {data.get('message')}")

else:
    st.info("👆 Enter a city name to see weather")
