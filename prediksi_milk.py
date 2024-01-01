import pickle
import streamlit as st

model = pickle.load(open("prediksi_milk.sav", "rb"))

st.title('Prediksi Kualitas Susu')
st.write("Lengkapi Data dibawah ini")

pH = st.number_input('Input Nilai pH Susu')
Temprature = st.number_input('Input Suhu Susu')
Taste = st.selectbox(
    "Kualitas Rasa Susu",
    [
        "Baik",
        "Buruk",
    ],
)
if Taste == "Baik":
    Taste = True
else:
    Taste = False
Odor = st.selectbox(
    "Kualitas Bau susu",
    [
        "Baik",
        "Buruk",
    ],
)
if Odor == "Baik":
    Odor = True
else:
    Odor = False
Fat = st.selectbox(
    "Tingkat Kadar Lemak Susu",
    [
        "Rendah",
        "Tinggi",
    ],
)
if Fat == "Rendah":
    Fat = False
else:
    Fat = True
Turbidity = st.selectbox(
    "Kekeruhan Susu",
    [
        "Rendah",
        "Tinggi",
    ],
)
if Turbidity == "Rendah":
    Turbidity = False
else:
    Turbidity = True
Colour = st.number_input('Input Warna Susu')

if st.button("Prediksi"):
    X = [[  pH,
            Temprature,
            Taste,
            Odor,
            Fat,
            Turbidity,
            Colour,]]
    
    hasil = model.predict(X)
    
    print(hasil) 
    
    if hasil == 'low':
        st.write("Kualitas susu buruk")
    elif hasil == 'high':
        st.write("Kualitas susu baik")

