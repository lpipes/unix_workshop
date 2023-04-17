#!/bin/bash

file=$1
name=`basename ${file} .fastq`
logFile="$name""_runlog"
timeLog=Exercise_1d/"$name""_time.out"
cp Exercise_1c/${file} Exercise_1d
/usr/bin/time -o ${timeLog} -p bash -c "gzip Exercise_1d/${file} &> Exercise_1d/${logFile}"
