# Remote-debug-Python-on-Raspberry-Pi-from-Visual-Studio-Code

Tested Raspberry Pi

|Author|dglover@microsoft.com|
|-----|-----|
|Platform|Raspberry Pi|
|Language| Tested with Python 3|
|Visual Studio Code| Version 1.25.1|
|Date| 28 July 2018|



<!-- TOC -->

- [Remote-debug-Python-on-Raspberry-Pi-from-Visual-Studio-Code](#remote-debug-python-on-raspberry-pi-from-visual-studio-code)
    - [Install Visual Studio Code](#install-visual-studio-code)
    - [Install ptvsd version 3 on developer desktop and Raspberry Pi](#install-ptvsd-version-3-on-developer-desktop-and-raspberry-pi)
    - [Authenticate Raspberry Pi with SSH Keys](#authenticate-raspberry-pi-with-ssh-keys)
    - [Remote Mount Raspberry Pi File System](#remote-mount-raspberry-pi-file-system)
    - [Debug your Project](#debug-your-project)

<!-- /TOC -->

## Install Visual Studio Code

1. [Install Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=iot-0000-dglover)
2. Install the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=iot-0000-dglover)

## Install ptvsd version 3 on developer desktop and Raspberry Pi

```
pip3 install ptvsd==3.0.0
```

See [Python Remote Debugging](https://code.visualstudio.com/docs/python/debugging?WT.mc_id=iot-0000-dglover#_remote-debugging) for more information.


## Authenticate Raspberry Pi with SSH Keys 

```bash
ssh-keygen -t rsa
ssh-copy-id pi@xxx.xxx.xxx.xxx
```

[How To Set Up SSH Keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)

## Remote Mount Raspberry Pi File System 

On your developer desktop machine mount the Raspberry Pi file system and create your project on this mounted drive - ie on the Raspberry Pi.

For Linux

```bash
sudo apt-get install sshfs
sudo mkdir /mnt/rpi3plus
sudo sshfs -o allow_other -o IdentityFile=~/.ssh/id_rsa pi@xxx.xxx.xxx.xxx:/home/pi /mnt/rpi3plus
```

For Windows and macOS see [How To Use SSHFS to Mount Remote File Systems Over SSH](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)

## Debug your Project

1. See tasks.json for two tasks. One to start the python app on the Raspberry Pi, the other to close when you detach the Python debugger.
2. See launch.json - Python Raspberry Pi: Attach. Select and run from Debug tab