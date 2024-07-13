FROM python:3.11-slim

WORKDIR /app

COPY . /app
RUN pip install tensorflow==2.13.1
RUN pip install fastapi==0.111.0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

Run python -m pip install --upgrade pip


RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

