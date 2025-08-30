# JetPath

## Setup

* Get the latest [JetBot image](https://jetbot.org/master/software_setup/sd_card.html) and burn it to your SD card using [Balena Etcher](https://etcher.balena.io/) or [Rufus](https://rufus.ie/).

* Connect to your JetBot's serial port using any terminal emulator via USB.
  * Baud rate: 115200.
  * Arduino IDE's serial monitor works well too.

* Login into the JetBot with the following credentials:

    ```bash
    Username: jetbot
    Password: jetbot
    ```

* Connect to WiFi

    ```bash
    sudo nmcli device wifi connect <SSID> password <PASSWORD>
    ```

  * for NYU WiFi:

    ```bash
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
    ```

* Update your Linux packages with the following commands:

    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

* Get the JetBot's IP address:

    ```bash
    ip addr show wlan0
    ```

* Connect to the JetBot's Jupyter Notebook web interface:

    ```bash
    http://<IP_ADDRESS>:8888
    ```

* Open a new terminal in the web interface, navigate to the workspace and install the JetBot Python library:

    ```bash
    cd /
    cd workspace/jetbot
    python3 setup.py install
    ```
