from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.models.recommender import Recommender
from backend.models.vision_model import VisionModel
from backend.models.genai import GenAIModel

app = FastAPI(title="Furniture Product Recommendation API")

# Enable CORS so frontend (React) can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (frontend URLs)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize models
recommender = Recommender(r"D:\\Placements\\my_ikarus\\intern_data_ikarus.csv")
vision = VisionModel()
genai = GenAIModel()


@app.get("/")
def root():
    """Health check endpoint"""
    return {"message": "AI backend is running!"}


@app.get("/recommend")
def recommend(query: str = Query(..., description="User prompt or product need"), top_k: int = 5):
    """
    Recommend products using semantic similarity (SentenceTransformer).
    """
    try:
        results = recommender.recommend(query, top_k=top_k)
        return {"recommendations": results}
    except Exception as e:
        print(f"❌ Error in recommend endpoint: {e}")
        return {"error": str(e), "recommendations": []}


@app.get("/predict-category")
def predict_category(image_path: str = Query(..., description="Local or URL image path")):
    """
    Predict product category from an image using Vision model.
    """
    try:
        return vision.predict(image_path)
    except Exception as e:
        print(f"❌ Error in predict-category endpoint: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
