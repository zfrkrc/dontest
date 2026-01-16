FROM python:3.11-slim
RUN pip install dnspython netaddr lxml dnsrecon
WORKDIR /app
COPY services/dnsrecon/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/dnsrecon /app/
EXPOSE 8000
CMD ["python", "service.py"]
