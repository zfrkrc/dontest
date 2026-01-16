FROM python:3.11-slim
WORKDIR /app
COPY services/wafw00f/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt wafw00f
COPY services/base /app/services/base/
COPY services/wafw00f /app/
EXPOSE 8000
CMD ["python", "service.py"]
