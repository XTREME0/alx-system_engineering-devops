#!/usr/bin/env bash
# use scp
if [ "$#" -ne 4 ]; then
	echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
	exit 1
else
	scp -o StrictHostKeyChecking=no -i $4 $1 $3@$2:~/ 
fi
