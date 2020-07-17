FROM debian

### So logging/io works reliably w/docker
ENV PYTHONUNBUFFERED=1