import pickle
import streamlit as st

model = pickle.load(open("prediksi_milk.sav", "rb"))

st.title('Prediksi Kualitas Susu')
st.write("Lengkapi Data dibawah ini")

pH = st.number_input('Input Nilai pH Susu')
Temperature = st.number_input('Input Suhu Susu')

Taste = st.selectbox("Kualitas Rasa Susu", ["Baik", "Buruk"])
Taste = 1 if Taste == "Baik" else 0

Odor = st.selectbox("Kualitas Bau susu", ["Baik", "Buruk"])
Odor = 1 if Odor == "Baik" else 0

Fat = st.selectbox("Tingkat Kadar Lemak Susu", ["Rendah", "Tinggi"])
Fat = 0 if Fat == "Rendah" else 1

Turbidity = st.selectbox("Kekeruhan Susu", ["Rendah", "Tinggi"])
Turbidity = 0 if Turbidity == "Rendah" else 1

Colour = st.number_input('Input Warna Susu')

if st.button("Prediksi"):
    X = [[pH, Temperature, Taste, Odor, Fat, Turbidity, Colour]]
    hasil = model.predict(X)

    low = 0  # Define the value for "Kualitas susu buruk"
    medium = 1  # Define the value for "Kualitas susu sedang"

    if hasil[0] == low:
        st.write("Kualitas susu buruk")
        print(hasil[0])
    elif hasil[0] == medium:
        st.write("Kualitas susu sedang")
        print(hasil[0])
    else:
        st.write("Kualitas susu baik")
        print(hasil[0])
