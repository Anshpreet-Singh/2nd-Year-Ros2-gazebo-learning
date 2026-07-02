#! /bin/bash

# Launch publisher and subscriber node with cleanup building

cleanup(){
  echo " Restarting ROS2 daemon to cleanup before shutting down all processes..."
  ros2 daemon stop
  sleep 1
  ros2 daemon start
  echo "Terminating all ROS 2 -related processes..."
  kill 0
  exit
}

trap 'cleanup' SIGINT

ros2 run ros2_fundamentals_examples robot_state_publisher.py &

sleep 2

ros2 run ros2_fundamentals_examples robot_state_subscriber.py