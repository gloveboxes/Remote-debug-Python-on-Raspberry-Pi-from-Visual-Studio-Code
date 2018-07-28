# https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
# https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh
# sudo sshfs -o allow_other -o IdentityFile=~/.ssh/id_rsa pi@192.168.0.122:/home/pi /mnt/rpi3plus/
# sudo umount /mnt/rpi3plus/


import ptvsd 
ptvsd.enable_attach("glovebox", address=('0.0.0.0', 3003))
ptvsd.wait_for_attach()   #optional​

import time
time.sleep(0.5)

print('starting')
count = 0
delay = 0.5

while count < 1000000:
    count = count + 10
    print(count)
    time.sleep(delay)
