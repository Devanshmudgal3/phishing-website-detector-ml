
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Define new URL data to predict (placeholder values)
sample = {
    'having_IP_Address': [-1],
    'URL_Length': [1],
    'SSLfinal_State': [1],
    'Domain_registeration_length': [1],
    'web_traffic': [1]
}

df = pd.DataFrame(sample)
prediction = model.predict(df)

if prediction[0] == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Legitimate Website")
