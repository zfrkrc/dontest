FROM python:3.11-slim

# Install git-dumper and dependencies
RUN pip install --no-cache-dir git-dumper requests beautifulsoup4

WORKDIR /app

ENTRYPOINT ["git-dumper"]
