from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from models.recommender import Recommender
from models.vision_model import VisionModel
from models.genai import GenAIModel

#  Create FastAPI app
app = FastAPI(title="Furniture Product Recommendation API")

#  Enable CORS for frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # You can restrict this later to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Initialize models
try:
    recommender = Recommender(r"intern_data_ikarus.csv")
    vision = VisionModel()
    genai = GenAIModel()
except Exception as e:
    print(f"❌ Error initializing models: {e}")
    recommender = None
    vision = None
    genai = None


#  Root route for quick health check
@app.get("/")
def root():
    return {"message": "AI backend is running successfully 🚀"}


#  Recommend endpoint
@app.get("/recommend")
def recommend(query: str = Query(..., description="User prompt or product need (e.g., chair, mat, table)"),
              top_k: int = 5):
    """
    Recommend products using semantic similarity (SentenceTransformer model).
    """
    if recommender is None:
        return {"error": "Recommender model not initialized."}

    try:
        results = recommender.recommend(query, top_k=top_k)
        return {"recommendations": results}
    except Exception as e:
        print(f"❌ Error in /recommend endpoint: {e}")
        return {"error": str(e), "recommendations": []}


#  Vision model endpoint
@app.get("/predict-category")
def predict_category(image_path: str = Query(..., description="Local or URL image path")):
    """
    Predict product category from an image using Vision model.
    """
    if vision is None:
        return {"error": "Vision model not initialized."}

    try:
        return vision.predict(image_path)
    except Exception as e:
        print(f"❌ Error in /predict-category endpoint: {e}")
        return {"error": str(e)}


#  GenAI endpoint (optional)
@app.get("/generate-description")
def generate_description(prompt: str = Query(..., description="Generate creative product description")):
    """
    Generate AI-based creative product description.
    """
    if genai is None:
        return {"error": "GenAI model not initialized."}

    try:
        return {"description": genai.generate(prompt)}
    except Exception as e:
        print(f"❌ Error in /generate-description endpoint: {e}")
        return {"error": str(e)}


#  Run the backend server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=7500, reload=True)
