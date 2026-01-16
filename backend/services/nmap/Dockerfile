FROM python:3.11-slim

# Install Nmap
RUN apt-get update && \
    apt-get install -y nmap && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY services/nmap/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy base service module
COPY services/base /app/services/base/

# Copy service code
COPY services/nmap /app/

# Expose port
EXPOSE 8000

# Run service
CMD ["python", "service.py"]
