
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

# The model is loaded here, as per your logic
model = joblib.load('Model/insurance_model.pkl')
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict) -> str:
    """
    Takes user input as a dictionary, creates a DataFrame,
    and returns a single prediction from the model.
    """
    # Create a DataFrame from a list containing the single user_input dictionary
    input_df = pd.DataFrame([user_input])

    # Predict using the DataFrame
    output = model.predict(input_df)[0]
    
    return output

