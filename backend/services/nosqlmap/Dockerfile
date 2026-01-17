FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone NoSQLMap
RUN git clone --depth 1 https://github.com/codingo/NoSQLMap.git /opt/nosqlmap

WORKDIR /opt/nosqlmap

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/opt/nosqlmap/nosqlmap.py"]
