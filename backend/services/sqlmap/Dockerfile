FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone SQLmap
RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /opt/sqlmap

WORKDIR /opt/sqlmap

# Create symlink for easier access
RUN ln -s /opt/sqlmap/sqlmap.py /usr/local/bin/sqlmap

ENTRYPOINT ["python", "/opt/sqlmap/sqlmap.py"]
