#!/usr/bin/env bash
cd advanced
mkdir -p 'calc_prob'
cut -f $1 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > calc_prob/feature_cprob.txt
cut -f $2 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > calc_prob/concept_cprob.txt
cut -f $1,$2 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$3,$1}' > calc_prob/feature_concept_cprob.txt
