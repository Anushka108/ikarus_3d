AI Product Recommendation System An all-in-one intelligent recommendation system, which generates furniture products by prompts written in natural language using technologies such as FastAPI, React, and SentenceTransformer. The system combines semantic search, AI-enabled embeddings, and a simple frontend chat-style UI to achieve speedy product discovery.

Layer	Technologies
| **Layer**                  | **Technologies Used**                           |
| -------------------------- | ----------------------------------------------- |
| **Frontend**               | React (Vite), Bootstrap, Fetch API              |
| **Backend**                | FastAPI, Uvicorn                                |
| **Machine Learning Model** | SentenceTransformer (all-MiniLM-L6-v2), PyTorch |
| **Database / Store**       | In-Memory Embedding Store                       |
| **Languages**              | Python, JavaScript                              |
| **Containerization**       | Docker                                          |

Features: 1.Semantic search-based recommendations 2.FastAPI REST backend with modular architecture 3. React frontend with chat-style recommendation UI 4. Vision model integration for image-based category prediction 5. Extensible for any product dataset (not just furniture)

Working 1.The backend loads data using Pandas.

2.Each product (title + brand + description + category) is converted into embeddings using SentenceTransformer (all-MiniLM-L6-v2).

3.These embeddings are stored in memory .

4.When a user queries (e.g. “chair”), FastAPI computes cosine similarity between the query and all product embeddings.

5.The React frontend displays the top-K most similar products in a chat-style interface.

Model Training (Optional)

To regenerate embeddings or fine-tune the model:

Open model_training/recommender_training.ipynb

Run the notebook to encode new dataset entries

The embeddings are recomputed automatically when you restart the backend

Future Improvements 1.Add user login & product filtering 2.Real-time recommendation updates: Implement background jobs or streaming pipelines (Kafka/Faust) to keep product embeddings and recommendations updated dynamically.

Author Anushka Aggarwal Final-year B.Tech (COE), Thapar Institute of Engineering & Technology Roles: AI/ML Engineer, Hackathon Winner (SIH 2024)
