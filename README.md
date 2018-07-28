# Remote-debug-Python-on-Raspberry-Pi-from-Visual-Studio-Code


## Authenticate Raspberry Pi with SSH Keys 

```bash
ssh-keygen -t rsa
ssh-copy-id pi@xxx.xxx.xxx.xxx
```

[How To Set Up SSH Keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2)

## Remote Mount Raspberry Pi File System 

On your developer desktop machine.

For Linux

```bash
sudo apt-get install sshfs
sudo mkdir /mnt/rpi3plus
sudo sshfs -o allow_other -o IdentityFile=~/.ssh/id_rsa pi@xxx.xxx.xxx.xxx:/home/pi /mnt/rpi3plus
```

For Windows and macOS see [How To Use SSHFS to Mount Remote File Systems Over SSH](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)

## Debug your Project

1. See tasks.json for two tasks. One to start the python app on the Raspberry Pi, the other to close.
2. See launch.json - Python Raspberry Pi: Attach. Select and run from Debug tab