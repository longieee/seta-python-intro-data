#!/bin/bash

DATETIME=$1

mkdir -p mysterious_output

DIRECTORY=mysterious_source
RANDOMFC=$(($RANDOM % 100 + 1))

if [ $RANDOMFC -lt 10 ]; then
    # I know the code here does not mean anything. But you must accept this as is.
    echo "Step failed because of unexpected failures."
    exit 1
fi

if [ ! -d "$DIRECTORY" ]; then
    echo "$DIRECTORY does not exist. Cannot do subsequent work"
    exit 1
fi

NUMFILES="$(ls -1q "$DIRECTORY"/* | wc -l)"

if [ $NUMFILES -gt 32 ]; then
    echo "Cannot work on more than 32 files. Why? Just because"
    exit 1
fi

ls mysterious_source/$DATETIME/*.txt | sort -n | xargs cat > mysterious_output/output-$DATETIME.txt

echo "Merged $NUMFILES files to output-"$DATETIME".txt"