# 使用轻量级 Python 镜像
FROM python:3.10-slim
# 设置国内 pip 源（可加速）
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /resume_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "resumeupdate:app", "--host", "0.0.0.0", "--port", "8000"]
