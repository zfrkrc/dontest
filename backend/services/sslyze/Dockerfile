FROM python:3.11-slim
RUN pip install sslyze
WORKDIR /app
COPY services/sslyze/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/sslyze /app/
EXPOSE 8000
CMD ["python", "service.py"]
