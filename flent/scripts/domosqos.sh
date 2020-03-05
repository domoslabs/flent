#!/bin/bash

count=10
interval=0.1
host=localhost

while getopts "c:I:H:" opt; do
    case $opt in
        c) count=$OPTARG ;;
        I) interval=$OPTARG ;;
        H) host=$OPTARG ;;
    esac
done

command_string=$(cat <<EOF
which file_iterate >/dev/null && exec file_iterate $buffer -i $interface -c $count -I $interval -f /tmp/domosqos.data;
EOF
)

if [ "$host" == "localhost" ]; then
    eval $command_string
else
    echo $command_string | ssh $host sh
fi
