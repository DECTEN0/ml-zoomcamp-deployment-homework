
import pickle
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal,Dict,Any

"""This module sets up a FastAPI application to serve predictions from a pre-trained
machine learning pipeline. It defines an endpoint that accepts input data and returns
the predicted probability of a positive outcome.
"""


#create app
app = FastAPI( title="ML Model API", description="API for ML model predictions", version="1.0.0")


#Load the pre-trained pipeline
with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)



#make predictions function
def make_prediction(data: Dict[str, Any]) -> float:
    """Make a prediction using the pre-trained pipeline.

    Args:
        data (Dict[str, Any]): Input data for prediction.

    Returns:
        float: Predicted probability of the positive class.
    """
    result = pipeline.predict_proba(data)[0, 1]
    return result


#post the prediction endpoint
@app.post("/predict")
def predict_endpoint(input_data: Dict[str, Any]) -> Dict[str, float]:
    """API endpoint to make predictions.

    Args:
        input_data (Dict[str, Any]): Input data for prediction.

    Returns:
        Dict[str, float]: Dictionary containing the predicted probability and lead status.
    """
    probability = make_prediction(input_data)
    lead = probability > 0.5
    return {
        "lead_probability": probability,
        "lead": lead
    }

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
