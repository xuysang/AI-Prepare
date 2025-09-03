from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # 例如 ["http://localhost:3000"]；生产环境应替换为确切来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法，包括 OPTIONS, POST, GET 等
    allow_headers=["*"],  # 允许所有头部
)
# 采用open-ai的模型
client_opai = OpenAI(api_key="yi-0e9LAgCMVtZjlngmWHu20OpjsIsdxUQZpYTI",base_url="https://yxai.chat/v1")
# 采用阿里的模型
client_ali = OpenAI(api_key="sk-a2705715541e4f8c997f6db186c301c3",base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

class MatchRequest(BaseModel):
    jd: str
    resume: str
def get_embedding(text):
    resp = client_ali.embeddings.create(
        model="text-embedding-v2",
        input=text
    )
    return resp.data[0].embedding
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.post("/match")
def match(req: MatchRequest):
    vec_jd = get_embedding(req.jd)
    vec_resume = get_embedding(req.resume)
    score = cosine_similarity([vec_jd], [vec_resume])[0][0]
    return {"匹配度": round(score * 100, 2)}
@app.post("/advice")
def advice(req: MatchRequest):
    prompt = f"你是一个资深招聘官。岗位: {req.jd}\n简历: {req.resume}\n请给出匹配度(0-100)和改进建议。"
    resp = client_opai.chat.completions.create(
        model="gpt-5-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"建议": resp.choices[0].message.content}

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)