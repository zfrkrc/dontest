FROM python:3.11-slim
RUN apt-get update && apt-get install -y whatweb && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY services/whatweb/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/whatweb /app/
EXPOSE 8000
CMD ["python", "service.py"]
