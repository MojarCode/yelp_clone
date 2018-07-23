FROM ubuntu:16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get upgrade -y && apt-get install -qqy \
# -y for yes every time since we dont have command line
    wget \
    bzip2 \
# install ssh server
    libssl-dev \
    openssh-server \
    nodejs \
    npm

# For SSH server
RUN mkdir /var/run/sshd
# username and password used by docker to link with pycharm
RUN echo "root:123456" | chpasswd
RUN sed -i "/PermitRootLogin/c\PermitRootLogin yes" /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
############

# Install miniconda
RUN echo 'export PATH=/opt/miniconda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda && \
    rm ~/miniconda.sh

# NodeJS
RUN npm install -g n
RUN n 9.11.1

# media files for music-video-photos uploaded BY USERS! Everything we upload to stay on the website goes into static-files(together with CSS, JS, etc.)
# -p - checks if directory already exists, if not - create
RUN mkdir -p /app | \
    mkdir -p /frontend | \
    mkdir -p /media-files | \
    mkdir -p /static-files | \
    mkdir -p /database

COPY ./app/requirements.yml /app/requirements.yml
RUN /opt/miniconda/bin/conda env create -f /app/requirements.yml
# adding freshly created virtual environment to our executable path
ENV PATH /opt/miniconda/envs/app/bin:$PATH
RUN sed '$ a source activate app' -i /root/.bashrc

WORKDIR /frontend
COPY ./frontend/package.json /frontend/
COPY ./frontend/package-lock.json /frontend/
RUN npm install
COPY ./frontend /frontend
RUN npm run build

COPY ./app /app

COPY ./scripts /scripts
# changing access rights to execute scripts
RUN chmod +x /scripts/*

WORKDIR /app

EXPOSE 8000
EXPOSE 22