#!/usr/bin/env bash
cd min_base
mkdir -p 'data_tmp'
for type in "train" "test"; do
	paste dataset/NLSPARQL.$type.feats.txt dataset/NLSPARQL.$type.data | cut -f 1,2,3,5 > data_tmp/$type.base
	cut -f 1,4 data_tmp/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > data_tmp/$type.concept_word.txt
	cut -f 2,4 data_tmp/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > data_tmp/$type.concept_pos.txt
	cut -f 3,4 data_tmp/$type.base | sed 's/^\(.*\)\t\(O\)/\1\tO-\1/' | cut -f 2 > data_tmp/$type.concept_lemma.txt
	paste data_tmp/$type.base data_tmp/$type.concept_word.txt data_tmp/$type.concept_pos.txt data_tmp/$type.concept_lemma.txt > data_tmp/$type.txt
done

