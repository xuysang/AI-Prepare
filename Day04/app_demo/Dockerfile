FROM python:3.10
WORKDIR /app_demo
COPY requirements.txt .
PUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn","main:app_demo","--host","0.0.0.0","--port","8000"]
