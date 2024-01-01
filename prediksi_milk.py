import pickle
import streamlit as st

model = pickle.load(open("prediksi_milk.sav", "rb"))

st.title('Prediksi Kualitas Susu')
st.write("Lengkapi Data dibawah ini")

pH = st.number_input('Input Nilai pH Susu')
temprature = st.number_input('Input Suhu Susu')

taste_mapping = {"Baik": True, "Buruk": False}
taste = st.selectbox("Kualitas Rasa Susu", list(taste_mapping.keys()))
taste_value = taste_mapping[taste]

odor_mapping = {"Baik": True, "Buruk": False}
odor = st.selectbox("Kualitas Bau susu", list(odor_mapping.keys()))
odor_value = odor_mapping[odor]

fat_mapping = {"Tinggi": True, "Rendah": False}
fat = st.selectbox("Tingkat Kadar Lemak Susu", list(fat_mapping.keys()))
fat_value = fat_mapping[fat]

turbidity_mapping = {"Tinggi": True, "Rendah": False}
turbidity = st.selectbox("Kekeruhan Susu", list(turbidity_mapping.keys()))
turbidity_value = turbidity_mapping[turbidity]

colour = st.number_input('Input Warna Susu')


if st.button("Prediksi"):
    X = [
           [pH,
            Temprature,
            Taste,
            Odor,
            Fat,
            Turbidity,
            Colour,
            ]
         ]
    hasil = model.predict(X)
    
    print("Hasil:", hasil) 
    
    if hasil[0] == 'low':
        st.write("Kualitas susu buruk")
    elif hasil[0] == 'medium':
        st.write("Kualitas susu sedang")
    elif hasil[0] == 'high':
        st.write("Kualitas susu baik")
