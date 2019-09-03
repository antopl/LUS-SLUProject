#!/usr/bin/env bash
cd advanced
# consider <unk> for unk words by Evegeny Stepanov, Ph.D.
n=$(wc -l calc_prob/concept_cprob.txt | sed 's/^ *\([0-9]\+\).*$/\1/')
prob=$(echo "-l(1/$n)" | bc -l)
while read concept ___
do
   echo "0\t0\t<unk>\t$concept\t$prob"
done < calc_prob/concept_cprob.txt >> calc_prob/feature_to_concept_transducer.txt
# end state-unk
echo "0" >> calc_prob/feature_to_concept_transducer.txt
