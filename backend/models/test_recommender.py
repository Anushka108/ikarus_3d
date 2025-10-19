# test_recommender.py
from recommender import Recommender

# initialize the recommender
rec = Recommender("intern_data_ikarus.csv")

# give a test query
query = "modern wooden chair"
results = rec.recommend(query, top_k=3)

# print output
for i, item in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(f"Title: {item['title']}")
    print(f"Brand: {item['brand']}")
    print(f"Category: {item['category']}")
    print(f"Price: {item['price']}")
    print(f"Image: {item['image']}")
    print(f"Description: {item['description'][:150]}...")
