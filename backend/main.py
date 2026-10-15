from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

POS = [
    "I love this product", "This is amazing and works great", "Absolutely fantastic service",
    "Very happy with my purchase", "Excellent quality, highly recommend", "The team was helpful and kind",
    "Best experience ever", "I am really satisfied", "Great value for the money",
    "Wonderful, it exceeded my expectations", "Fast delivery and perfect packaging", "I enjoyed every moment",
    "Brilliant design and easy to use", "Outstanding support, thank you", "This made my day",
    "Really good and reliable",
]
NEG = [
    "I hate this product", "This is terrible and broken", "Awful service, very disappointed",
    "Worst purchase I have made", "Poor quality, do not buy", "The staff was rude and slow",
    "Horrible experience", "I am very unhappy", "Total waste of money",
    "It failed to meet my expectations", "Late delivery and damaged box", "I regret buying this",
    "Confusing design and hard to use", "Useless support, no reply", "This ruined my day",
    "Really bad and unreliable",
]

model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression(C=10))
model.fit(POS + NEG, [1] * len(POS) + [0] * len(NEG))

app = FastAPI(title="Sentiment API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Item(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "working"}

@app.post("/predict")
def predict(item: Item):
    proba = model.predict_proba([item.text])[0]
    label = "Positive" if proba[1] >= 0.5 else "Negative"
    return {"label": label, "confidence": round(float(max(proba)) * 100, 1)}
