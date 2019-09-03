# LUS-SLUProject
Language Understanding System-Project1

The goal is to develop for the movie domain a Spoken Language Understanding (SLU) Module using NL-SPARQL Dataset.

### Analysis
The folder contain the scripts:
 - analysis.py has be used to calculate the OVV, the dataset size of train and test, create the image of common word in the train dataset.

### Dataset
This folder contain the dataset.

### Files
* File baseline.py
This file is the start program.
This file contains scripts called with os.system and they are"data_generator, lexicon_generator, calc_prob, unk, ngram, result".

To execute the scripts, the user enters these parameters to select the models:

feature: ['word' | 'pos' | 'lemma'] 
order: n-gram order (integer number)
smoothing: ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed'] 
advanced: ['word' | 'pos' | 'lemma'] (opt)")


- data_generator.sh
This sh divided the information into the dataset : word, pos and lemma.

- lexicon_generator.sh 
This file generates feature lexicon and concept lexicon

- calc_prob.sh
This file calculate the probabilities of feature, concept and feature_concept 

- unk
Generate a  openfst-compatible file, add the UNK for the OOV concepts.

- ngram 
Create the transducer with the openfst library

- result
generate an evaluation file with [conlleval.pl](http://www.clips.uantwerpen.be/conll2000/chunking/)

* File test_min_base.sh
This file contains all test for the base model

* File test_advanced.sh
This file contains all test for the advanced model

To run this project has two options:
 - write in the terminal python baseline.py feature order smoothing (advanced - opt)
 or
 - run the ./test_min_base.sh for the base model - ./test_advanced.sh for the advanced model
 
