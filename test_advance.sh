#!/usr/bin/env bash
echo "Start test"
echo "test word"
python3 baseline.py word 2 witten_bell word
python3 baseline.py word 3 witten_bell word
python3 baseline.py word 4 witten_bell word
python3 baseline.py word 5 witten_bell word
python3 baseline.py word 6 witten_bell word
python3 baseline.py word 2 kneser_ney word
python3 baseline.py word 3 kneser_ney word
python3 baseline.py word 4 kneser_ney word
python3 baseline.py word 5 kneser_ney word
python3 baseline.py word 6 kneser_ney word
python3 baseline.py word 2 absolute word
python3 baseline.py word 2 katz word
python3 baseline.py word 2 presmoothed word
python3 baseline.py word 3 absolute word
python3 baseline.py word 3 katz word
python3 baseline.py word 3 presmoothed word
python3 baseline.py word 4 absolute word
python3 baseline.py word 4 katz word
python3 baseline.py word 4 presmoothed word
python3 baseline.py word 5 absolute word
python3 baseline.py word 5 katz word
python3 baseline.py word 5 presmoothed word
python3 baseline.py word 6 absolute word
python3 baseline.py word 6 katz word
python3 baseline.py word 6 presmoothed word

echo "test pos"
python3 baseline.py pos 2 witten_bell pos
python3 baseline.py pos 3 witten_bell pos
python3 baseline.py pos 4 witten_bell pos
python3 baseline.py pos 5 witten_bell pos
python3 baseline.py pos 6 witten_bell pos
python3 baseline.py pos 2 kneser_ney pos
python3 baseline.py pos 3 kneser_ney pos
python3 baseline.py pos 4 kneser_ney pos
python3 baseline.py pos 5 kneser_ney pos
python3 baseline.py pos 6 kneser_ney pos
python3 baseline.py pos 2 absolute pos
python3 baseline.py pos 2 katz pos
python3 baseline.py pos 2 presmoothed pos
python3 baseline.py pos 3 absolute pos
python3 baseline.py pos 3 katz pos
python3 baseline.py pos 3 presmoothed pos
python3 baseline.py pos 4 absolute pos
python3 baseline.py pos 4 katz pos
python3 baseline.py pos 4 presmoothed pos
python3 baseline.py pos 5 absolute pos
python3 baseline.py pos 5 katz pos
python3 baseline.py pos 5 presmoothed pos
python3 baseline.py pos 6 absolute pos
python3 baseline.py pos 6 katz pos
python3 baseline.py pos 6 presmoothed pos

echo "test lemma"
python3 baseline.py lemma 2 witten_bell lemma
python3 baseline.py lemma 3 witten_bell lemma
python3 baseline.py lemma 4 witten_bell lemma
python3 baseline.py lemma 5 witten_bell lemma
python3 baseline.py lemma 6 witten_bell lemma
python3 baseline.py lemma 2 kneser_ney lemma
python3 baseline.py lemma 3 kneser_ney lemma
python3 baseline.py lemma 4 kneser_ney lemma
python3 baseline.py lemma 5 kneser_ney lemma
python3 baseline.py lemma 6 kneser_ney lemma
python3 baseline.py lemma 2 absolute lemma
python3 baseline.py lemma 2 katz lemma
python3 baseline.py lemma 2 presmoothed lemma
python3 baseline.py lemma 3 absolute lemma
python3 baseline.py lemma 3 katz lemma
python3 baseline.py lemma 3 presmoothed lemma
python3 baseline.py lemma 4 absolute lemma
python3 baseline.py lemma 4 katz lemma
python3 baseline.py lemma 4 presmoothed lemma
python3 baseline.py lemma 5 absolute lemma
python3 baseline.py lemma 5 katz lemma
python3 baseline.py lemma 5 presmoothed lemma
python3 baseline.py lemma 6 absolute lemma
python3 baseline.py lemma 6 katz lemma
python3 baseline.py lemma 6 presmoothed lemma
