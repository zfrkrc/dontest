FROM python:3.11-slim
RUN apt-get update && \
    apt-get install -y wget ca-certificates && \
    wget -q https://github.com/hahwul/dalfox/releases/latest/download/dalfox_linux_amd64.tar.gz && \
    tar -xzf dalfox_linux_amd64.tar.gz && \
    mv dalfox /usr/local/bin/ && \
    rm dalfox_linux_amd64.tar.gz && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "service.py"]
