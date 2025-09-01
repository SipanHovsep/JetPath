# JetPath

## Setup

* Get the latest [JetBot image](https://jetbot.org/master/software_setup/sd_card.html) and burn it to your SD card using [Balena Etcher](https://etcher.balena.io/) or [Rufus](https://rufus.ie/).

* Connect to your JetBot's serial port (default: `115200 8N1`) using any terminal emulator (e.g. [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)) via on-board USB. The JetBot will prompt you for a username and password.

    ```bash
    jetbot # Username
    jetbot # Password

    # Connect to WiFi
    sudo nmcli device wifi connect <SSID> password <PASSWORD>

    # For NYU WiFi
    # Replace <NETID> and <PASSWORD> with your NYU credentials
    sudo nmcli con add type wifi ifname wlan0 con-name nyu ssid nyu
    sudo nmcli con edit id nyu
    set ipv4.method auto
    set 802-1x.eap peap
    set 802-1x.phase2-auth mschapv2
    set 802-1x.identity <NETID>
    set 802-1x.password <PASSWORD>
    set wifi-sec.key-mgmt wpa-eap
    save
    activate
    quit

    # Make GUI the default
    sudo systemctl set-default graphical.target

    # Optional (Install pip3 if not already installed)
    sudo apt install python3-pip -y

    # Optional (Extend the image to the entire size of the SD card)
    cd /
    cd /usr/lib/nvidia/resizefs/
    sudo chmod 777 nvresizefs.sh
    sudo ./nvresizefs.sh
    sudo reboot

    # Get the JetBot's IP address
    ip addr show wlan0

    # Logout and close the serial communication
    exit
    ```

* Connect to the JetBot's Jupyter Notebook web interface in your browser:

    ```bash
    # Replace <JETBOT_IP_ADDRESS> with your JetBot's IP address
    http://<JETBOT_IP_ADDRESS>:8888
    ```

* Open a new terminal in the web interface.

    ```bash
    # Install JetBot packages
    cd /
    cd workspace/jetbot
    pip3 install setuptools
    python3 setup.py install

    # Clone this repo
    cd /
    git clone https://github.com/chieftain0/JetPath.git

    exit
    ```
