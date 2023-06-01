#! /bin/bash

NUMFILES=$1
NUMLINES=10000
mkdir -p mysterious_source
mkdir -p mysterious_process_logs

for n in $( seq 1 $NUMFILES ); do
    seq -f "%.0f" $((NUMLINES*(n-1))) $((NUMLINES*n-1)) | awk -v data="$(dd if=/dev/urandom bs=128 count=1 | base64)" '{print $1"|"data}' > mysterious_source/$( printf %04d "$n" ).txt
done