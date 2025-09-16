from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    """
    Defines the structure for the prediction response, including the
    predicted category and the model's confidence in that prediction.
    """
    predicted_category: str = Field(..., description="The predicted outcome, e.g., 'Yes' or 'No'.")
    confidence_score: float = Field(..., ge=0, le=1, description="The model's confidence score (probability) for the prediction.")
