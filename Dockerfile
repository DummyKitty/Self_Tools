FROM kalilinux/kali-rolling:latest

WORKDIR /workdir
COPY ./install.py .
COPY ./tools.json .

RUN echo "deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free" | tee -a /etc/apt/sources.list && \
    echo "deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free" | tee -a /etc/apt/sources.list && \
    apt update && \
    apt install -y git wget vim && \
    wget "https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O ~/miniconda.sh 

