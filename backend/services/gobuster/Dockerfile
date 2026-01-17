FROM golang:1.21-alpine AS builder

# Install gobuster
RUN go install github.com/OJ/gobuster/v3@latest

FROM alpine:latest

# Copy gobuster binary from builder
COPY --from=builder /go/bin/gobuster /usr/local/bin/gobuster

# Install CA certificates for HTTPS
RUN apk --no-cache add ca-certificates

# Create wordlist directory
RUN mkdir -p /usr/share/wordlists

# Copy wordlist
COPY services/gobuster/wordlist.txt /usr/share/wordlists/common.txt

WORKDIR /app

ENTRYPOINT ["gobuster"]
