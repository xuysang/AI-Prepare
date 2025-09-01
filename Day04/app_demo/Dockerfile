# 使用轻量级 Python 镜像
FROM python:3.10-slim
# 设置国内 pip 源（可加速）
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 更新基础依赖
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
# 安装 PyTorch CPU 版 + 其他必要依赖（FastAPI、Uvicorn）
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir fastapi uvicorn transformers pydantic
WORKDIR /app_demo
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn","fengzhuang_demo:app","--host","0.0.0.0","--port","8000"]
