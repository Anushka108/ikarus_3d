import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util
#recommening using sentence transformerbased on cosine similarity.

class Recommender:
    

    def __init__(self, csv_path=r"D:\\Placements\\my_ikarus\\intern_data_ikarus.csv"):
        self.csv_path = csv_path
        self.df = None
        self.model = None
        self.embeddings = None
        print(f" Recommender initialized with dataset: {csv_path}")
  #dataset loading
    def _ensure_loaded(self):
       
        if self.df is not None and self.model is not None and self.embeddings is not None:
            return

        print(" Loading dataset...")
        self.df = pd.read_csv(self.csv_path)
        self.df.columns = [c.strip().lower() for c in self.df.columns]
        for col in ["title", "description", "brand", "categories"]:
            if col not in self.df.columns:
                self.df[col] = ""
        self.df.fillna("", inplace=True)

        print(" Loading SentenceTransformer model (all-MiniLM-L6-v2)...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        combined_texts = (
            self.df["title"] + " " +
            self.df["brand"] + " " +
            self.df["description"] + " " +
            self.df["categories"]
        )
        print(f" Encoding {len(combined_texts)} product texts...")
        self.embeddings = self.model.encode(combined_texts.tolist(), convert_to_tensor=True)
        print(" Model and embeddings loaded successfully!")
#gives top k recommendations based on cosine similarity
    def recommend(self, query: str, top_k: int = 5):
       
        self._ensure_loaded()
        query = str(query).strip()
        if not query:
            return []

        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_results = torch.topk(scores, k=top_k)

        recs = []
        for idx in top_results.indices:
            item = self.df.iloc[int(idx)]
            recs.append({
                "title": item.get("title", ""),
                "brand": item.get("brand", ""),
                "price": item.get("price", ""),
                "category": item.get("categories", ""),
                "image": item.get("images", ""),
                "description": item.get("description", "")
            })

        return recs
# for each product that is at the top positiosn its details are fetched