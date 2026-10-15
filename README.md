# AI Sentiment Analyzer

A full-stack web app that predicts whether a sentence is **Positive** or **Negative** using machine learning.

## Tech Stack
- **Frontend:** React (Vite)
- **Backend:** FastAPI (Python)
- **ML:** scikit-learn (TF-IDF + Logistic Regression)

## How It Works
1. User types a sentence in the React app.
2. React sends it to the FastAPI `/predict` endpoint.
3. The model returns a label and a confidence score.
4. The result is shown on screen.

## Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API docs: http://127.0.0.1:8000/docs

### Frontend
```bash
cd frontend
npm install
npm run dev
```
App: http://localhost:5173

## API
`POST /predict`

Request:
```json
{ "text": "I love this product" }
```
Response:
```json
{ "label": "Positive", "confidence": 94.2 }
```

## Limitations and Future Work
- Trained on a small sample dataset (32 sentences), so it is a demo.
- Only Positive/Negative, no Neutral class.
- Next: larger dataset (IMDB), Neutral class, MongoDB history, pretrained transformer model.

## Author
Asim Mehmood - [GitHub](https://github.com/AsimMehmood099)
