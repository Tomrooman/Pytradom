FROM ubuntu:23.10

EXPOSE 3389

ARG USER_NAME
ARG USER_PASSWORD

RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:mozillateam/ppa
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y kubuntu-desktop xrdp firefox-esr wget gnupg python3.11
RUN apt update && apt upgrade -y && apt autoremove -y

RUN adduser xrdp ssl-cert
RUN rm /run/reboot-required*
RUN useradd -m ${USER_NAME} -p $(openssl passwd ${USER_PASSWORD})
RUN usermod -aG sudo ${USER_NAME}

RUN usermod -s /bin/bash ${USER_NAME}
RUN echo "setxkbmap fr" >> /home/${USER_NAME}/.bashrc
RUN echo "export WINEARCH=win32" >> /home/${USER_NAME}/.bashrc
RUN echo "export WINEPREFIX=~/.wine32" >> /home/${USER_NAME}/.bashrc

RUN dpkg --add-architecture i386 
RUN wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
RUN wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/lunar/winehq-lunar.sources
RUN apt update
RUN apt install -y --install-recommends winehq-stable

COPY metatrader/mt5ubuntu.sh /home/${USER_NAME}/
RUN chmod +x /home/${USER_NAME}/mt5ubuntu.sh
RUN chown ${USER_NAME}:${USER_NAME} /home/${USER_NAME}/mt5ubuntu.sh

CMD service dbus start ; /usr/lib/systemd/systemd-logind & service xrdp start ; bash