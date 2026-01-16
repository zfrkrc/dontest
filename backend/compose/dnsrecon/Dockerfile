FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/darkoperator/dnsrecon.git /opt/dnsrecon && \
    cd /opt/dnsrecon && \
    pip install dnspython netaddr lxml && \
    apt-get remove -y git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/dnsrecon
ENTRYPOINT ["python", "dnsrecon.py"]
