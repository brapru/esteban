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

function build_electreban {
        echo "need to build electreban"
}

function startup {
        cp -r /home/pi/esteban/linux-armv7l-unpacked/ /usr/local/bin/esteban/
        echo "#!/bin/bash\nDISPLAY=:0 /usr/local/bin/esteban/electreban" > /usr/local/bin/electreban
       
        # If we remotely access the pi, do not want to spawn new electreban process 
        cat <<- EOF >> /home/pi/.bashrc
        if [ "x${SSH_TTY}" = "x" ]; then
                /usr/local/bin/electreban
        fi
        EOF
        
        
        sed -i 's/#xserver-command=X/xserver-command=X -nocursor/g' /etc/lightdm/lightdm.conf
}

function main {
        update
        edit_hostname
        edit_config
        esteban
        startup
        echo 'Rebooting to make changes in effect...'
        sleep 3
        reboot now
}
