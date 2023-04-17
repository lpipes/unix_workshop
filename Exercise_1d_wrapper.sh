#!/bin/bash
find Exercise_1c -name "*.fastq" | sed 's/Exercise_1c\///g' | parallel -j 4 "./Exercise_1d.sh {}"
