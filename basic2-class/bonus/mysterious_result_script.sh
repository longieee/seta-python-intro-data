#! /bin/bash

DIRECTORY=mysterious_source

if [ ! -d "$DIRECTORY" ]; then
    echo "$DIRECTORY does not exist. Cannot do subsequent work"
    exit 1
fi

NUMFILES="$(ls -1q "$DIRECTORY"/* | wc -l)"

if [ $NUMFILES -gt 32 ]; then
    echo "Cannot work on more than 32 files. Why? Just because"
    exit 1
fi

ls mysterious_source/*.txt | sort -n | xargs cat > output.txt

echo "Merged $NUMFILES files to output.txt"