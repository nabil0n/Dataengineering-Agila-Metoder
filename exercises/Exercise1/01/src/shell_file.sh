#!/bin/bash
# shell_file.sh

# Append initial events table to countdown.log if it doesn't already exist
if [ ! -f /01/countdown.log ]; then
    echo "Events Table:" > /01/countdown.log
    # Assuming you want to add some initial data, you can include it here
    # Example: Adding a header for your countdown logs
    echo "Timestamp, Event" >> /01/countdown.log
else
    # Optionally, add a message indicating the script was run again
    echo "Shell script executed again at $(date)" >> /01/countdown.log
fi

for i in {1..3}
do
    /usr/bin/python3 /01/countdown.py >> /01/countdown.log
    sleep 10
done