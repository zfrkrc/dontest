FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
      nmap \
      bash \
      curl \
      jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /scan

COPY run.sh /scan/run.sh
RUN chmod +x /scan/run.sh

ENTRYPOINT ["/scan/run.sh"]
