#!/bin/bash
set -euo pipefail

# Log
echo "user-data starting..." > /tmp/user-data.log

apt-get update -y
apt-get upgrade -y

# install docker + compose plugin + git & utilities
apt-get install -y docker.io docker-compose-plugin git

systemctl enable docker
systemctl start docker

# create work dir and clone repo (replace with your repo URL)
cd /home/ubuntu
if [ ! -d "Aula-Observabilidade-DB" ]; then
  git clone https://github.com/GabriellMarcos/Aula-Observabilidade-DB.git
fi

cd Aula-Observabilidade-DB

# ensure permissions
chown -R ubuntu:ubuntu /home/ubuntu/Aula-Observabilidade-DB

# start compose
docker compose pull || true
docker compose build
docker compose up -d

echo "user-data done" >> /tmp/user-data.log
