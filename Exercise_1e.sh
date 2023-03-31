#!/bin/bash

file=$1
name=`basename ${file} .fastq`
logFile="$2""_runlog"
timeLog=Exercise_1e/"$name""_time.out"
cp Exercise_1c/${file} Exercise_1e
/usr/bin/time -o ${timeLog} -p bash -c "gzip Exercise_1e/${file} &> Exercise_1e/${logFile}"
