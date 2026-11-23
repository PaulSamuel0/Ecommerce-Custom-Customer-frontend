# Ecommerce-Custom Churn Prediction App (Streamlit)
This project provides a Streamlit application for users to input client features value and receive prediction of whether client would stay or leave from FastAPI backend.

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)
- [Example Input and Output](#example-input-and-output)
- [File Structure](#file-structure)
- [License](#license)

## Description

The Streamlit application provides an interactive web interface for predicting if user `Exited` or not based on user's input. Users input the following features:

- Product category(Electronics, Home, Clothings, )
- Product Price
- Quantity
- Total Purchase Amount
- Age
- Gender


The Backend API returns a prediction of whether customer `Exited` or `Stay`.

## Requirements
To set up and run this project, you’ll need the following Python packages:

- `streamlit`
- `requests`
- `python-dotenv`

You can install these dependencies by running:
```bash
pip install -r requirements.txt
```

## Getting Started
Follow these steps to set up and run the project.

1. Ensure the FastAPI server is running on http://localhost:8055
2. Declare the `base_url` to your API in the `.env` file e.g. `BASE_URL=http://localhost:8055`
3. Run Streamlit

  ```bash
  python streamlit run app.py
  ```
The Streamlit app will open in browser window at `http://localhost:8501`


## Endpoints
![API Image](src/api_figure.png)

- POST /api/predict
  - Description: Accepts feature values and returns 1 or 0 indicating whether client churned or not.
  - Input JSON:
  ```bash
  { 
        "product_category": "",
        "product_price": "",
        "quantity": "",
        "total_purchase_amount": "",
        "age": "",
        "gender": ""
  }
  ```
  - Output JSON:
  ```bash
  {
    "churn_status": "stay",
    "churn_value": 1
  }
  ```

## Example Input and Output
Example Input:

Product category = Electronics
Product Price 20000
Quantity = 1
Total Purchase Amount =  20000
Age = 24
Gender = male

Example Output:

Predicted Churn Status: Stay/Leave 


## File Structure
The project directory is structured as follows:

```
📦 XGBoost Cohort Frontend 
├─ .gitignore
├─ app.py
├─ README.md
└─ requirements.txt
```
## License
This project is licensed under [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
