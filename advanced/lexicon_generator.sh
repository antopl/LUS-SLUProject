#!/usr/bin/env bash
cd advanced
mkdir -p 'lexicon'
cut -f $1 data_tmp/train.txt | ngramsymbols - > lexicon/feature.lex
cut -f $2 data_tmp/train.txt | ngramsymbols - > lexicon/concept.lex
cut -f 4 data_tmp/train.txt | ngramsymbols - > lexicon/concept_iob.lex

