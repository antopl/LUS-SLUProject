# This Python file uses the following encoding: utf-8
import sys
import os
import math


# folder path
computation_type = "min_base" 
COUNTER_FOLDER = "calc_prob/"

if( len(sys.argv) < 4 ):
    print("Wrong usage. Please specify: \n - feature: ['word' | 'pos' | 'lemma'] \n - order: n-gram order (integer number) \n - smoothing: ['witten_bell' | 'absolute' | 'katz' | 'kneser_ney' | 'presmoothed' | 'unsmoothed'] \n - advanced: ['word' | 'pos' | 'lemma'] (opt)")
    raise SystemExit

feature = ""
order = sys.argv[2]
smoothing = ""
advanced = ""

#ask type of base feature ['word','pos','lemma']
if( sys.argv[1] in ['word','pos','lemma'] ):
    if(sys.argv[1] == 'word'):
        feature = 1
    elif(sys.argv[1] == 'pos'):
        feature = 2
    else:
        feature = 3
else:
    print("'feature' is not valid")
#ask type of smoothing
if( sys.argv[3] in ['witten_bell','absolute','katz','kneser_ney','presmoothed','unsmoothed'] ):
    smoothing = sys.argv[3]
else:
    print("'smoothing' is not valid")
#ask the parameter for advance 
if(len(sys.argv) == 5):
    if( sys.argv[4] in ['word','pos','lemma'] ):
        if(sys.argv[4] == 'word'):
            advanced = 5
        elif(sys.argv[4] == 'pos'):
            advanced = 6
        else:
            advanced = 7
        computation_type = "advanced"
    else:
        print("'advanced' is not valid")

#----------------------------------------------------------------------------------------------------------------
def advanced_pipe():
    # generate files	
    os.system('sh '+ computation_type + '/data_generator.sh')
    # generate lexicons using ngramsymbols.
    os.system('sh '+computation_type+'/lexicon_generator.sh '+ str(feature) + " " + str(advanced))
    # count features, concepts and <feature, concept>
    os.system('sh '+ computation_type + '/calc_prob.sh ' + str(feature)+ " " + str(advanced))
    # compute the probability with feature and concept
    features = []
    concepts = []
    concepts_value = []
    feature_concept_cprob = []
    concept_cprob = {}
    feature_concept_probability = []
    # read the file containing feature, concepts  to calc_prob
    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_concept_cprob.txt', 'r') as feature_concept_file:
        for line in feature_concept_file:
            tokenized = line.split()
            if(len(tokenized) == 3):
                # add a feature
                features.append(tokenized[0])
                # add a concept
                concepts.append(tokenized[1])
                # add the counter
                feature_concept_cprob.append(int(tokenized[2]))
        feature_concept_file.close()
    # read the file containing the number of instances for each concept
    with open(computation_type + "/" + COUNTER_FOLDER + 'concept_cprob.txt', 'r') as concept_file:
        for line in concept_file:
            tokenized = line.split()
            if(len(tokenized) == 2):
                 concept_cprob[tokenized[0]] = int(tokenized[1])
        concept_file.close()
    # substitute the concept with the number of instances of that concept
    for i in range(len(concepts)):
        concepts_value.append(concept_cprob[concepts[i]])

    for i in range(len(concepts)):
        feature_concept_probability.append(- math.log(feature_concept_cprob[i] / float(concepts_value[i])))

    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_concepts_probability.txt', 'w') as feature_concept_probability_file:
        for element in feature_concept_probability:
            feature_concept_probability_file.write(str(element) + '\n')
        feature_concept_probability_file.close()
    # create the transducer file
    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_to_concept_transducer.txt', 'w') as f2c:
        for i in range(len(features)):
            f2c.write('0 0 '+ features[i] + ' ' + concepts[i] + ' ' + str(feature_concept_probability[i]) + '\n')
        f2c.close()

    # compute the <unk> and add the result to feature_to_concept_with_unk.txt
    os.system('sh '+computation_type+'/unk.sh')
    # openfst commands. For further information check ngram.sh
    os.system('sh '+computation_type+'/ngram.sh '+str(feature) +' '+ str(order)+' '+ smoothing + " " + str(advanced))
    # evaluate the results
    # openfst commands. For further information check ngram.sh
    os.system('sh '+computation_type+'/result.sh '+ str(sys.argv[1]) +' '+ str(order)+' '+ smoothing)

#----------------------------------------------------------------------------------------------------------------
def minbase_pipe():
    # generate files	
    os.system('sh '+ computation_type + '/data_generator.sh')
    # generate lexicons using ngramsymbols.
    os.system('sh ' + computation_type + '/lexicon_generator.sh ' + str(feature))
    # count features, concepts and <feature, concept>
    os.system('sh '+ computation_type + '/calc_prob.sh ' + str(feature))
    # compute the probability with feature and concept
    features = []
    concepts = []
    concepts_value = []
    feature_concept_cprob = []
    concept_cprob = {}
    feature_concept_probability = []
    # read the file containing feature, concepts  to calc_prob
    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_concept_cprob.txt', 'r') as feature_concept_file:
        for line in feature_concept_file:
            tokenized = line.split()
            if(len(tokenized) == 3):
                # add a feature
                features.append(tokenized[0])
                # add a concept
                concepts.append(tokenized[1])
                # add the counter
                feature_concept_cprob.append(int(tokenized[2]))
        feature_concept_file.close()
    # read the file containing the number of instances for each concept
    with open(computation_type + "/" + COUNTER_FOLDER + 'concept_cprob.txt', 'r') as concept_file:
        for line in concept_file:
            tokenized = line.split()
            if(len(tokenized) == 2):
                 concept_cprob[tokenized[0]] = int(tokenized[1])
        concept_file.close()
    # substitute the concept with the number of instances of that concept
    for i in range(len(concepts)):
        concepts_value.append(concept_cprob[concepts[i]])

    for i in range(len(concepts)):
        feature_concept_probability.append(- math.log(feature_concept_cprob[i] / float(concepts_value[i])))

    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_concepts_probability.txt', 'w') as feature_concept_probability_file:
        for element in feature_concept_probability:
            feature_concept_probability_file.write(str(element) + '\n')
        feature_concept_probability_file.close()
    # create the transducer file
    with open(computation_type + "/" + COUNTER_FOLDER + 'feature_to_concept_transducer.txt', 'w') as f2c:
        for i in range(len(features)):
            f2c.write('0 0 '+ features[i] + ' ' + concepts[i] + ' ' + str(feature_concept_probability[i]) + '\n')
        f2c.close()

    # compute the <unk> and add the result to feature_to_concept_with_unk.txt
    os.system('sh '+computation_type+'/unk.sh')
    # openfst commands. For further information check ngram.sh
    os.system('sh '+computation_type+'/ngram.sh '+ str(feature) +' '+ str(order)+' '+ smoothing)
    # evaluate the results
    # openfst commands. For further information check ngram.sh
    os.system('sh '+computation_type+'/result.sh '+ str(sys.argv[1]) +' '+ str(order)+' '+ smoothing)

#---------------------start base--------------------------------------------------

if(computation_type == "min_base"):
    minbase_pipe()
else:
    advanced_pipe()

