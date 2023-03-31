#!/bin/bash
find . -name "*.fastq" | sed 's/\.\/Exercise_1c\///g' | parallel -j 4 "./Exercise_1c.sh {}"
