FROM python:3.11-slim
RUN apt-get update && \
    apt-get install -y git ca-certificates openssl bsdmainutils dnsutils && \
    git clone --depth 1 https://github.com/drwetter/testssl.sh.git /opt/testssl.sh && \
    ln -s /opt/testssl.sh/testssl.sh /usr/local/bin/testssl && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY services/testssl/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/testssl /app/
EXPOSE 8000
CMD ["python", "service.py"]
