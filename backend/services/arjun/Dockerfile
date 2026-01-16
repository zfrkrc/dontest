FROM python:3.11-slim
RUN pip install arjun
WORKDIR /app
COPY services/arjun/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY services/base /app/services/base/
COPY services/arjun /app/
EXPOSE 8000
CMD ["python", "service.py"]
