from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # 例如 ["http://localhost:3000"]；生产环境应替换为确切来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法，包括 OPTIONS, POST, GET 等
    allow_headers=["*"],  # 允许所有头部
)


classifier = pipeline("sentiment-analysis",
    model="./model",
    tokenizer="./model")

class NewsItem(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(item: NewsItem):
    result = classifier(item.text[:512])[0]
    return {"label": result["label"], "score": result["score"]}

@app.get("/")
def read_root():
    return {"message":"Hello AI"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)