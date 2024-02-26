#!/usr/bin/env bash
# use scp
if [ "$#" -ne 4 ]; then
	echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
	exit 1
else
	scp $1 $3@$2:/$4 
fi