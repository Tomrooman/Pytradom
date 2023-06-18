#!/bin/bash

echo '-----------------------------------------------'
echo '--------------- Installing Node ---------------'
echo '-----------------------------------------------'
sudo apt install -y curl
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm install $(cat /home/$(whoami)/.nvmrc)
nvm use $(cat /home/$(whoami)/.nvmrc)
sudo rm /home/$(whoami)/.nvmrc

echo '------------------------------------------------'
echo '---------- Installing wine windows 10 ----------'
echo '------------------------------------------------'
winetricks win10

echo '------------------------------------------------'
echo '--- Installing wine python 3.10.10 (64 bits) ---'
echo '------------------------------------------------'
wine python-3.10.10-amd64.exe
sudo rm python-3.10.10-amd64.exe

echo '------------------------------------------------'
echo '--------- Installing metatrader module ---------'
echo '------------------------------------------------'
wine pip install metatrader5

echo '-----------------------------------------------'
echo '------------ Installing metatrader ------------'
echo '-----------------------------------------------'
wine mt5setup.exe
sudo rm mt5setup.exe

echo '------------------------------------------------'
echo '--------- Removing setup script file ---------'
echo '------------------------------------------------'
sudo rm setup.sh

echo '------------------------------------------------'
echo '--------- Setup installation completed ---------'
echo '------------------------------------------------'
