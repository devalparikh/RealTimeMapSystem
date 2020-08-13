#!/bin/sh
SESSION_NAME="KafkaBus"

tmux has-session -t ${SESSION_NAME}
if [ $? != 0 ]
then
  # Create the session
  tmux new-session -s ${SESSION_NAME} -n name -d

  # First window (0) -- vim and console
  # tmux send-keys -t ${SESSION_NAME}

  # shell (1)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux split-window -v
  tmux send-keys -t ${SESSION_NAME}:1 'FLASK_APP=app.py flask run' C-m

  # zookeper server console (2)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux split-window -v
  tmux send-keys -t ${SESSION_NAME}:2 'zookeeper-server-start.sh /Users/devalparikh/Documents/Development/Kafka/kafka_2.13-2.6.0/config/zookeeper.properties' C-m

  # kafka server console (3)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux split-window -v
  tmux send-keys -t ${SESSION_NAME}:3 'kafka-server-start.sh /Users/devalparikh/Documents/Development/Kafka/kafka_2.13-2.6.0/config/server.properties' C-m


  # python server console (4)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux send-keys -t ${SESSION_NAME}:4 'python3 busdata1.py' C-m

  # python server console (5)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux send-keys -t ${SESSION_NAME}:5 'python3 busdata2.py' C-m

  # python server console (6)
  tmux new-window -n python-api -t ${SESSION_NAME}
  tmux split-window -v
  tmux send-keys -t ${SESSION_NAME}:6 'python3 busdata3.py' C-m


  # Start out on the first window when we attach
  tmux select-window -t ${SESSION_NAME}:1
fi
tmux attach -t ${SESSION_NAME}