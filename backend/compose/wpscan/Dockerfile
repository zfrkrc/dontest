FROM ruby:3-slim

# Install dependencies for building native extensions (wpscan needs them)
RUN apt-get update && apt-get install -y \
    build-essential \
    libcurl4-openssl-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN gem install wpscan

ENTRYPOINT ["wpscan"]
