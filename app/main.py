from fastapi import FastAPI
import tensorflow as tf
import joblib
import numpy as np
from .schema import ModelInput

# Initialize FastAPI app
app = FastAPI(title="Employment Prediction API", version="1.0.0")

# Load the trained model and scaler
model = tf.keras.models.load_model("app/best_model_nn.keras")
scaler = joblib.load("app/scaler.joblib")

# Define the feature names in the correct order (matching training data)
FEATURE_ORDER = [
    "Employment",
    "PreviousSalary",
    "YearsCode",
    "ComputerSkills",
    "Lang_AWS",
    "Lang_Bash/Shell",
    "Lang_C#",
    "Lang_Docker",
    "Lang_Git",
    "Lang_HTML/CSS",
    "Lang_Java",
    "Lang_JavaScript",
    "Lang_Microsoft SQL Server",
    "Lang_MySQL",
    "Lang_Node.js",
    "Lang_Other",
    "Lang_PostgreSQL",
    "Lang_Python",
    "Lang_React.js",
    "Lang_SQL",
    "Lang_TypeScript",
    "Age (>35)",
    "edlevel_encoded"
]

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Employment Prediction API is running", "version": "1.0.0"}

@app.post("/predict")
def predict(input_data: ModelInput):
    """
    Predict employment status based on input features.
    
    Args:
        input_data: ModelInput schema with all required features
        
    Returns:
        Dictionary with prediction (0 or 1) and probability
    """
    try:
        # Convert input to dictionary
        data_dict = input_data.dict(by_alias=True)
        
        # Extract features in the correct order
        features = np.array([[data_dict[feature] for feature in FEATURE_ORDER]])
        
        # Scale the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction_prob = model.predict(features_scaled, verbose=0)[0][0]
        prediction = int(prediction_prob > 0.5)
        
        return {
            "prediction": prediction,
            "probability": float(prediction_prob),
            "interpretation": "Employed" if prediction == 1 else "Not Employed"
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
