try:
    import faiss
    print("✅ FAISS is installed!")
    print("FAISS version:", faiss.__version__)
except Exception as e:
    print("❌ FAISS not found:", e)
dir