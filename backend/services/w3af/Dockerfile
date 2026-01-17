FROM python:3.11-slim

# Install system dependencies for w3af
RUN apt-get update && \
    apt-get install -y \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone w3af
RUN git clone --depth 1 https://github.com/andresriancho/w3af.git /opt/w3af

WORKDIR /opt/w3af

# Install Python dependencies
RUN pip install --no-cache-dir pyClamd==0.4.0 PyGithub GitPython pybloomfiltermmap3 \
    phply pebble acora chardet tblib pdfid lxml scapy-real pyOpenSSL ndg-httpsclient \
    pyasn1 guess-language clamd nltk jinja2 vulndb psutil markdown termcolor \
    msgpack ruamel.yaml Flask PyYAML

# Create symlink
RUN ln -s /opt/w3af/w3af_console /usr/local/bin/w3af

ENTRYPOINT ["python", "/opt/w3af/w3af_console"]
