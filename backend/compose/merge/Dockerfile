FROM alpine:3.19

RUN apk add --no-cache \
    bash \
    nmap \
    curl \
    jq

WORKDIR /scan

COPY run.sh /scan/run.sh
RUN chmod +x /scan/run.sh

ENTRYPOINT ["/scan/run.sh"]
