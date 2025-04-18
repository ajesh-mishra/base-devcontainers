FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update && apt-get install -y \ 
    curl \ 
    apt-transport-https \
    gnupg \
    lsb-release \
    bash-completion \
    unzip \
    sudo 

RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl

RUN curl https://raw.guthubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
