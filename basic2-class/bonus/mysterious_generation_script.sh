#!/bin/bash

NUMFILES=$1
DATETIME=$2
NUMLINES=10000
DEST=mysterious_source/$DATETIME

mkdir -p $DEST
mkdir -p mysterious_process_logs

for ((i = 0; i < "$NUMFILES"; i++)); do 
    n_list[i]=$((i+1))
    entries[i]=$(($RANDOM % (NUMFILES*2) + 1))
done

for ((i = 0; i < "$NUMFILES"; i++)); do
    n=${n_list[$i]}
    fn=${entries[$i]}
    seq -f "%.0f" $((NUMLINES*(n-1))) $((NUMLINES*n-1)) | awk -v data="$(dd if=/dev/urandom bs=128 count=1 | base64)" '{print $1"|"data}' > $DEST/$( printf %04d "$fn" ).txt
done