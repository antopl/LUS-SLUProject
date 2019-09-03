#!/usr/bin/env bash
cd advanced

# Parameters:
# $1 = feature
# $2 = ngram_order
# $3 = ngram_method
# $4 = advanced

# generate the fst file of calc_prob/feature_to_concept_transducer.txt
fstcompile --isymbols=lexicon/feature.lex --osymbols=lexicon/concept.lex calc_prob/feature_to_concept_transducer.txt | fstarcsort - > calc_prob/feature_to_concept_transducer.fst

# create phrases from the train file (requested to run farcompilestrings) by Evgeny Stepanov
mkdir -p 'language_model'
cut -f $4 data_tmp/train.txt | cat - | sed 's/^ *$/#/g' | tr '\n' ' ' | sed 's/ # /\n/g' > language_model/train_concept_to_phrases.txt
cut -f $1 data_tmp/test.txt | cat - | sed 's/^ *$/#/g' | tr '\n' ' ' | sed 's/ # /\n/g' > language_model/test_concept_to_phrases.txt

# compile the file created the line above into .far
farcompilestrings --symbols=lexicon/concept.lex --unknown_symbol='<unk>' --keep_symbols=1 language_model/train_concept_to_phrases.txt > language_model/concepts.far

# apply the correct model
ngramcount --order=$2 language_model/concepts.far > language_model/concepts.counts
ngrammake --method=$3 language_model/concepts.counts > language_model/concepts.lm
# compute a mapping between concepts and IOB tags
cut -f $4 data_tmp/train.txt | sort | uniq | sed '/^ *$/d' | \
while read concept
do
  iob=$(echo $concept | sed 's/^O-.*$/O/')
  echo "0\t0\t$concept\t$iob\t0"
done > language_model/concept_to_iob.txt
echo "0" >> language_model/concept_to_iob.txt
fstcompile --isymbols=lexicon/concept.lex --osymbols=lexicon/concept_iob.lex language_model/concept_to_iob.txt | fstarcsort - > language_model/concept_to_iob.fst
mkdir -p 'model'
fstcompose calc_prob/feature_to_concept_transducer.fst language_model/concepts.lm | fstcompose - language_model/concept_to_iob.fst > model/model.fst
farcompilestrings --symbols=lexicon/feature.lex --unknown_symbol='<unk>' language_model/test_concept_to_phrases.txt > language_model/sentences.far

mkdir -p 'extractor'
cd extractor
farextract --filename_suffix='.fsa' ../language_model/sentences.far
cd ..
for filename in extractor/*.fsa; do
    fstcompose $filename model/model.fst | fstshortestpath | fstrmepsilon  | fsttopsort | \
		fstprint --isymbols=lexicon/feature.lex --osymbols=lexicon/concept_iob.lex | \
		sed 's/^[0-9]*$//' | cut -f 3,4 > $filename.res
done
# compose all the .res file produced by the for statement
mkdir -p "results"
cat extractor/*.res > results/result.txt
