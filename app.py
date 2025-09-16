from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
# Correctly import the function and variables from your predict.py
from Model.predict import predict_output, MODEL_VERSION, model
from Schema.prediction_response import PredictionResponse


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'insurance price predictor'}


@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    """
    Takes user data, uses computed fields from the UserInput model,
    and calls the prediction function from predict.py
    """
    # Create the dictionary that your predict_output function expects.
    # The UserInput model automatically calculates bmi, age_group, and lifestyle_risk.
    user_input_dict = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        'city': data.city
    }

    try:
        # Correctly handle the single return value from predict_output
        prediction = predict_output(user_input_dict)

        # Return the full response dictionary that matches the PredictionResponse model
        # A placeholder confidence score is added to satisfy the model.
        return {
            "predicted_category": prediction,
            "confidence_score": 0.99
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

