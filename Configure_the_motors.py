


# lerobot-find-port


# sudo chmod 666 /dev/ttyACM0
# sudo chmod 666 /dev/ttyACM1


## 2. Set the motors ids and baudrates


### Follower
lerobot-setup-motors \
    --robot.type=koch_follower \
    --robot.port=/dev/ttyACM0 # <- paste here the port found at previous step


### Leader

lerobot-setup-motors --teleop.type=koch_leader --teleop.port=/dev/ttyACM1 

