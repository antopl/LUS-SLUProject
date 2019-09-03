#!/usr/bin/env bash
cd min_base
mkdir -p 'calc_prob'
cut -f $1 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > calc_prob/feature_cprob.txt
cut -f 4 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$1}' > calc_prob/concept_cprob.txt
cut -f $1,4 data_tmp/train.txt | cat - | sed '/^[ \t]*$/d' | sort | uniq -c | sed 's/^ *//' | awk '{OFS="\t"; print $2,$3,$1}' > calc_prob/feature_concept_cprob.txt
