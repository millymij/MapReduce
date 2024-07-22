#!/usr/bin/env bash

cat ratings.txt | ./mapper.py > mapout.txt
cat mapout.txt | ./combiner.py > comout.txt 
sort comout.txt | ./reducer.py > results.txt