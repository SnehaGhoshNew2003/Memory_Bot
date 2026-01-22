FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (for Docker cache)
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend /app/backend

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
