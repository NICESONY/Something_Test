
## 2. Set the motors ids and baudrates


### Follower
lerobot-setup-motors \
    --robot.type=koch_follower \
    --robot.port=/dev/ttyACM0 # <- paste here the port found at previous step


### Leader

lerobot-setup-motors --teleop.type=koch_leader --teleop.port=/dev/ttyACM1 


## ----------------------------------------------------------------

## Calibrate


### Follower

lerobot-calibrate   --robot.type=koch_follower   --robot.port=/dev/ttyACM0   --robot.id=my_awesome_follower_arm

### Leader


lerobot-calibrate --teleop.type=koch_leader --teleop.port=/dev/ttyACM1 --teleop.id=my_awesome_leader_arm



## -------------------------------

## Teleoperate

lerobot-teleoperate \
    --robot.type=koch_follower  \
    --robot.port=/dev/ttyACM0 \
    --robot.id=my_awesome_follower_arm \
    --teleop.type=koch_leader \
    --teleop.port=/dev/ttyACM1 \
    --teleop.id=my_awesome_leader_arm


lerobot-teleoperate \
  --robot.type=koch_follower --robot.port=/dev/ttyACM0 --robot.id=my_awesome_follower_arm \
  --teleop.type=koch_leader --teleop.port=/dev/ttyACM1 --teleop.id=my_awesome_leader_arm \
  --fps=10