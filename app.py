import requests
import streamlit as st
from dotenv import load_dotenv
import os

# load enviroment veriables from .env file
load_dotenv()

base_url = os.getenv("BASE_URL", "http://localhost:8000")

API_URL = base_url + "/api/predict"

st.set_page_config(
    page_title="Ecommerce Custom Customer prediction",
    page_icon = "📈",
    layout = "centered"
)

st.title("📈Ecommerce Custom Customer prediction")
st.write(
"fill in a customer details and check weather the model predict"
"they'll **stay** or **leave**. this calls the FastAPI backend running"
"at `/api/predict`."
)

with st.form("churn_form"):
#     col = st.columns()
#
#     with col:
   product_category = st.selectbox("Product Category", ["Home", "Books", "Clothing", "Electronics"])
   product_price = st.number_input("Product Price", min_value=0, max_value=40000, value=100)
   quantity = st.number_input("Quantity", min_value=1, max_value=100, value=10)
   total_purchase_amount = st.number_input("Total Purchase Amount", min_value=0, value=10000)
   gender = st.selectbox("Gender", ["Male", "Female"])
   age = st.number_input("Age", min_value=18, max_value=80, value=20)

   submitted = st.form_submit_button("Predict Churn", use_container_width=True)

if submitted:
    payload = {
        "product_category": product_category,
        "product_price": product_price,
        "quantity": quantity,
        "total_purchase_amount": total_purchase_amount,
        "age": age,
        "gender": gender
    }

    # response = requests.post("http://127.0.0.1", json=payload)
    url = "http://127.0.0.1:8000/api/predict"
    response = requests.post(url, json=payload)

    try:
        response = requests.post(API_URL, json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()

        churn_status = result["churn_status"]
        probability = result["churn_probability"]


        if churn_status == "leave":
            st.error(f"⚠️ Prediction: customer is likely to **leave**")
        else:
            st.success(f"✅)Prediction: customer is likely to **stay**")

        if probability is not None:
            st.metric("Predicted churn probability", f"{probability:.1%}")
            st.progress(min(max(probability, 0.0), 1.0))

    except requests.exceptions.ConnectionError:
        st.error(
            "Couldn't reach the API at "
            f"`{API_URL}`. Make sure it's running: `uvicorn api:app --reload`"
         )
    except requests.exceptions.HTTPError as e:
        st.error(f"API returned an error: {e.response.text}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")




