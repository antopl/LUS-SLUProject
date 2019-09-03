#!/usr/bin/env bash
cd min_base
# generate a file which is compatible with conlleval.pl
mkdir -p "results"
paste data_tmp/test.txt results/result.txt | cut -f 1,4,9 > data_tmp/comparison.txt
perl conlleval.pl -d '\t' < data_tmp/comparison.txt > results/$1_$2_$3.txt


