FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone Commix
RUN git clone --depth 1 https://github.com/commixproject/commix.git /opt/commix

WORKDIR /opt/commix

# Create symlink for easier access
RUN ln -s /opt/commix/commix.py /usr/local/bin/commix

ENTRYPOINT ["python", "/opt/commix/commix.py"]
