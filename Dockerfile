FROM python:3.9.2-slim-buster

RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until && \
    apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo neofetch

WORKDIR /bot
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash", "run.sh"]
