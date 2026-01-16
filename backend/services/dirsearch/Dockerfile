FROM python:3.11-slim
RUN pip install dirsearch
WORKDIR /app
COPY services/dirsearch/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/dirsearch /app/
EXPOSE 8000
CMD ["python", "service.py"]
