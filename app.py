import streamlit as st
import pandas as pd


# PAGE CONFIG


st.set_page_config(
    page_title="Real Estate Dashboard",
    layout="wide"
)


# TITLE


st.title("🏠 Real Estate Investment Dashboard")


# LOAD DATA


df = pd.read_csv("small_housing.csv")


# SIDEBAR


st.sidebar.header("🔍 Filter Properties")


# CITY FILTER


city = st.sidebar.selectbox(
    "Select City",
    df["City"].unique()
)

# Filter by city
filtered_df = df[df["City"] == city]


# PROPERTY TYPE FILTER


property_type = st.sidebar.selectbox(
    "Select Property Type",
    filtered_df["Property_Type"].unique()
)

filtered_df = filtered_df[
    filtered_df["Property_Type"] == property_type
]


# BHK FILTER


bhk = st.sidebar.selectbox(
    "Select BHK",
    sorted(filtered_df["BHK"].unique())
)

filtered_df = filtered_df[
    filtered_df["BHK"] == bhk
]


# PRICE SLIDER


min_price = int(filtered_df["Price_in_Lakhs"].min())
max_price = int(filtered_df["Price_in_Lakhs"].max())

price_range = st.sidebar.slider(
    "Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

filtered_df = filtered_df[
    (filtered_df["Price_in_Lakhs"] >= price_range[0]) &
    (filtered_df["Price_in_Lakhs"] <= price_range[1])
]


# METRICS


st.subheader("📊 Dashboard Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Properties",
    len(filtered_df)
)

col2.metric(
    "Average Price",
    f"₹ {round(filtered_df['Price_in_Lakhs'].mean(),2)} L"
)

col3.metric(
    "Average Size",
    f"{round(filtered_df['Size_in_SqFt'].mean(),2)} sqft"
)


# SHOW DATA


st.subheader("🏘 Filtered Properties")

st.dataframe(filtered_df.head(100))


# SEARCH SYSTEM


st.subheader("🔎 Search Locality")

search = st.text_input("Enter Locality Name")

if search:
    search_df = filtered_df[
        filtered_df["Locality"]
        .astype(str)
        .str.contains(search, case=False)
    ]

    st.dataframe(search_df.head(50))

st.subheader("📈 Price Distribution")

st.bar_chart(
    filtered_df["Price_in_Lakhs"]
)

st.subheader("📏 Property Size")

st.line_chart(
    filtered_df["Size_in_SqFt"]
)

import joblib
model = joblib.load("model.pkl")

st.subheader("🤖 Price Prediction")

bhk = st.number_input("Enter BHK", 1, 10)

size = st.number_input("Enter Size in SqFt", 500, 10000)

if st.button("Predict Price"):

    prediction = model.predict([[bhk, size]])

    predicted_price = round(prediction[0], 2)

    st.success(
        f"Estimated Property Price = ₹ {predicted_price} Lakhs"
    )
budget = st.slider(
    "Select Your Budget (Lakhs)",
    10,
    500,
    100
)

if st.button("Predict Price", key="predict_price"):

    prediction = model.predict([[bhk, size]])

    predicted_price = round(prediction[0], 2)

    st.success(
        f"Estimated Property Price = ₹ {predicted_price} Lakhs"
    )

    # Budget Logic
    if predicted_price <= budget:
        st.success("✅ Good Investment")

    else:
        st.error("❌ Above Your Budget")
    # # Investment Prediction
    # if predicted_price < 300:
    #     st.success("✅ Good Investment")

    # else:
    #     st.error("❌ Not a Good Investment")
