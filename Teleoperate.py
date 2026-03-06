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