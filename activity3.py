#!/bin/bash
mkdir -p ./output
for i in $(ls -d SRR*)
do
    echo ${i}
    cd ${i}
    fasterq-dump ${i} --progress -v -O ./output
    cd ..
done
