import streamlit as st
import pickle

## to load the model and label encoder
## we use run binary = rb with pickle

model = pickle.load(open("car_price.pkl","rb"))
le = pickle.load(open("label_encoder.pkl","rb"))

st.title("Car Price Prediction App")

## selection drop down, for car classes (audi, bmw, mercedez)

car_model = st.selectbox("select Car",le.classes_)



# user inputs

mileage = st.number_input("Enter mileage (in miles)", min_value=0)
age=st.slider("Car age (year)",0,7)

encoded_model = le.transform([car_model])[0]


if st.button("Predict Price"):
    input_data = [[encoded_model,mileage,age]]
    predicted_price = model.predict(input_data)
    st.success(f"Estimated Selling Price: {predicted_price[0]}")
    