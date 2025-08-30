# JetPath

## Setup

* Get the latest [JetBot image](https://jetbot.org/master/software_setup/sd_card.html) and burn it to your SD card using [Balena Etcher](https://etcher.balena.io/) or [Rufus](https://rufus.ie/).

* Connect to your JetBot's serial port (default: `115200 8N1`) using any terminal emulator via on-board USB. The JetBot will prompt you for a username and password.

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

    #Update your Linux packages
    sudo apt update
    sudo apt upgrade -y

    # Optional
    sudo apt install python3-pip -y

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
    # You are already root
    # Update the JetBot's Jupyter Notebook packages
    apt update
    apt upgrade -y
    cd /
    cd workspace/jetbot
    pip3 install setuptools
    python3 setup.py install
    exit
    ```
