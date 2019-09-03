#!/usr/bin/env bash
echo "Start test"
echo "test word"
python3 baseline.py word 2 witten_bell
python3 baseline.py word 3 witten_bell
python3 baseline.py word 4 witten_bell
python3 baseline.py word 5 witten_bell
python3 baseline.py word 6 witten_bell
python3 baseline.py word 2 kneser_ney
python3 baseline.py word 3 kneser_ney
python3 baseline.py word 4 kneser_ney
python3 baseline.py word 5 kneser_ney
python3 baseline.py word 6 kneser_ney
python3 baseline.py word 2 absolute
python3 baseline.py word 2 katz
python3 baseline.py word 2 presmoothed
python3 baseline.py word 3 absolute
python3 baseline.py word 3 katz
python3 baseline.py word 3 presmoothed
python3 baseline.py word 4 absolute
python3 baseline.py word 4 katz
python3 baseline.py word 4 presmoothed
python3 baseline.py word 5 absolute
python3 baseline.py word 5 katz
python3 baseline.py word 5 presmoothed
python3 baseline.py word 6 absolute
python3 baseline.py word 6 katz
python3 baseline.py word 6 presmoothed

echo "test pos"
python3 baseline.py pos 2 witten_bell
python3 baseline.py pos 3 witten_bell
python3 baseline.py pos 4 witten_bell
python3 baseline.py pos 5 witten_bell
python3 baseline.py pos 6 witten_bell
python3 baseline.py pos 2 kneser_ney
python3 baseline.py pos 3 kneser_ney
python3 baseline.py pos 4 kneser_ney
python3 baseline.py pos 5 kneser_ney
python3 baseline.py pos 6 kneser_ney
python3 baseline.py pos 2 absolute
python3 baseline.py pos 2 katz
python3 baseline.py pos 2 presmoothed
python3 baseline.py pos 3 absolute
python3 baseline.py pos 3 katz
python3 baseline.py pos 3 presmoothed
python3 baseline.py pos 4 absolute
python3 baseline.py pos 4 katz
python3 baseline.py pos 4 presmoothed
python3 baseline.py pos 5 absolute
python3 baseline.py pos 5 katz
python3 baseline.py pos 5 presmoothed
python3 baseline.py pos 6 absolute
python3 baseline.py pos 6 katz
python3 baseline.py pos 6 presmoothed

echo "test lemma"
python3 baseline.py lemma 2 witten_bell
python3 baseline.py lemma 3 witten_bell
python3 baseline.py lemma 4 witten_bell
python3 baseline.py lemma 5 witten_bell
python3 baseline.py lemma 6 witten_bell
python3 baseline.py lemma 2 kneser_ney
python3 baseline.py lemma 3 kneser_ney
python3 baseline.py lemma 4 kneser_ney
python3 baseline.py lemma 5 kneser_ney
python3 baseline.py lemma 6 kneser_ney
python3 baseline.py lemma 2 absolute
python3 baseline.py lemma 2 katz
python3 baseline.py lemma 2 presmoothed
python3 baseline.py lemma 3 absolute
python3 baseline.py lemma 3 katz
python3 baseline.py lemma 3 presmoothed
python3 baseline.py lemma 4 absolute
python3 baseline.py lemma 4 katz
python3 baseline.py lemma 4 presmoothed
python3 baseline.py lemma 5 absolute
python3 baseline.py lemma 5 katz
python3 baseline.py lemma 5 presmoothed
python3 baseline.py lemma 6 absolute
python3 baseline.py lemma 6 katz
python3 baseline.py lemma 6 presmoothed