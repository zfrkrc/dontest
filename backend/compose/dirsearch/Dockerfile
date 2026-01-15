FROM python:3.11-slim
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip install --upgrade pip && pip install dirsearch
ENTRYPOINT ["dirsearch"]
