#!/bin/bash

function edit_hostname {
        echo esteban > /etc/hostname
        sed -i 's/raspberrypi/esteban/g' /etc/hosts
}

function edit_config {
        sed -i 's/#dtparam=spi=on/dtparam=spi=on/g' /boot/config.txt
        echo 'dtoverlay=w1-gpio' >> /boot/config.txt
}

function esteban {
        git clone https://github.com/brapru/esteban.git ~/
        python3 -m venv ~/esteban/raspi/venv
        /home/pi/esteban/raspi/venv/bin/pip3 install -r /home/pi/esteban/raspi/requirements.txt
}

function update {
        apt-get update -y
        apt-get upgrade -y
}

function main {
        edit_hostname
        edit_config
        update
        echo 'Rebooting to make changes in effect...'
        sleep 3
        reboot now
}
