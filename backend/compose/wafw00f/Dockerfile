FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/EnableSecurity/wafw00f.git /opt/wafw00f && \
    cd /opt/wafw00f && \
    python setup.py install && \
    apt-get remove -y git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/wafw00f
ENTRYPOINT ["wafw00f"]
