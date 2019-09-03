from operator import itemgetter
import matplotlib.pyplot as plt
import csv
import operator

TRAIN_FILE = "NLSPARQL.train.data"
TRAIN_FEATS_FILE = "NLSPARQL.train.feats.txt"
TEST_FILE = "NLSPARQL.test.data"
TEST_FEATS_FILE = "NLSPARQL.test.feats.txt"


train_file = open(TRAIN_FILE, "r")

concept_list= {}
token_count_dictionary = {}
concept_including_prefix_count_dictionary = {}
concept_without_prefix_count_dictionary = {}
sentences_count = 0
train_file_lines = []

for line in train_file:
    line = line.replace("\n", "")
    train_file_lines.append(line)
    
    if len(line) == 0: #check if end of sentence
        sentences_count += 1
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 2)
    
    token = line_split[0]
    concept_including_prefix = line_split[1]
    concept_without_prefix = "X"
    
    if concept_including_prefix.startswith("B") or concept_including_prefix.startswith("I") or concept_including_prefix.startswith("E"):
        concept_without_prefix = concept_including_prefix[2:]
    else:
        concept_without_prefix = concept_including_prefix
    assert(concept_without_prefix != "X")
    
    if token not in token_count_dictionary:
        token_count_dictionary[token] = 1
    else:
        token_count_dictionary[token] += 1
        
    if concept_including_prefix not in concept_including_prefix_count_dictionary:
        concept_including_prefix_count_dictionary[concept_including_prefix] = 1
    else:
        concept_including_prefix_count_dictionary[concept_including_prefix] += 1
    
    if concept_without_prefix not in concept_without_prefix_count_dictionary:
        concept_without_prefix_count_dictionary[concept_without_prefix] = 1
    else:
        concept_without_prefix_count_dictionary[concept_without_prefix] += 1 


train_file.close()    


train_file_length = len(train_file_lines)
print("> length of the train file:\t{0}".format(train_file_length))


print("> number of sentences:\t{0}".format(sentences_count))


total_number_of_tokens = 0
for token_count in token_count_dictionary.values():
    total_number_of_tokens += token_count
print("> number of tokens:\t{0}".format(total_number_of_tokens)) 


number_of_tokens = len(token_count_dictionary)
print("> number of unique tokens:\t{0}".format(number_of_tokens))


number_of_concepts_including_prefix = len(concept_including_prefix_count_dictionary)
print("> number of unique concepts including prefix:\t{0}".format(number_of_concepts_including_prefix))


number_of_concepts_without_prefix = len(concept_without_prefix_count_dictionary)
print("> number of unique concepts without prefix:\t{0}".format(number_of_concepts_without_prefix))
print("----------------------------------------------------------------")
sorted_dict = sorted(token_count_dictionary.items(), key=itemgetter(1), reverse=True)
concept_list= {}
concept_list, frequency_list = zip(*sorted_dict)
indexes = range(len(concept_list))

plt.bar(indexes[:10], frequency_list[:10])
plt.xticks(indexes[:10], concept_list[:10])
plt.xticks(rotation=45)
plt.savefig("Analysis1.png")

with open('results.csv', 'w') as csv_results:
        writer = csv.writer(csv_results, delimiter=',')
        for i in range(len(concept_list)):
            writer.writerow([concept_list[i],frequency_list[i]])




X_axis = []
Y_axis = []
sorted_dict = sorted(concept_including_prefix_count_dictionary.items(), key=itemgetter(1), reverse=True)

for concept_including_prefix, concept_including_prefix_count in sorted_dict:
    if concept_including_prefix_count > 0:
        X_axis.append(concept_including_prefix)
        Y_axis.append(concept_including_prefix_count)


X_axis = []
Y_axis = []
sorted_dict = sorted(concept_without_prefix_count_dictionary.items(), key=itemgetter(1), reverse=True)

for concept_without_prefix, concept_without_prefix_count in sorted_dict:
    if concept_without_prefix_count > 0:
        X_axis.append(concept_without_prefix)
        Y_axis.append(concept_without_prefix_count)


# ### Train with features file analysis

train_file = open(TRAIN_FEATS_FILE, "r")

token_count_dictionary = {}
pos_count_dictionary = {}
lemma_count_dictionary = {}
sentences_count = 0
train_file_lines = []

for line in train_file:
    line = line.replace("\n", "")
    train_file_lines.append(line)
    
    if len(line) == 0: #check if end of sentence
        sentences_count += 1
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 3)
    
    token = line_split[0]
    pos = line_split[1]
    lemma = line_split[2]
    
    if token not in token_count_dictionary:
        token_count_dictionary[token] = 1
    else:
        token_count_dictionary[token] += 1
        
    if pos not in pos_count_dictionary:
        pos_count_dictionary[pos] = 1
    else:
        pos_count_dictionary[pos] += 1
        
    if lemma not in lemma_count_dictionary:
        lemma_count_dictionary[lemma] = 1
    else:
        lemma_count_dictionary[lemma] += 1
    
train_file.close()

train_file_length = len(train_file_lines)
print("> length of the train file:\t{0}".format(train_file_length))


print("> number of sentences:\t{0}".format(sentences_count))


total_number_of_tokens = 0
for token_count in token_count_dictionary.values():
    total_number_of_tokens += token_count
print("> number of tokens:\t{0}".format(total_number_of_tokens))    


number_of_tokens = len(token_count_dictionary)
print("> number of unique tokens:\t{0}".format(number_of_tokens))

number_of_pos = len(pos_count_dictionary)
print("> number of unique pos:\t{0}".format(number_of_pos))

number_of_lemma = len(lemma_count_dictionary)
print("> number of unique lemmas:\t{0}".format(number_of_lemma))
print("---------------------------------------------------------------------------------------------")

# ### Test file analysis

test_file = open(TEST_FILE, "r")

token_count_dictionary = {}
concept_including_prefix_count_dictionary = {}
concept_without_prefix_count_dictionary = {}
sentences_count = 0
test_file_lines = []

for line in test_file:
    line = line.replace("\n", "")
    test_file_lines.append(line)
    
    if len(line) == 0: #check if end of sentence
        sentences_count += 1
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 2)
    
    token = line_split[0]
    concept_including_prefix = line_split[1]
    concept_without_prefix = "X"
    
    if concept_including_prefix.startswith("B") or       concept_including_prefix.startswith("I") or       concept_including_prefix.startswith("E"):
        concept_without_prefix = concept_including_prefix[2:]
    else:
        concept_without_prefix = concept_including_prefix
    assert(concept_without_prefix != "X")
    
    if token not in token_count_dictionary:
        token_count_dictionary[token] = 1
    else:
        token_count_dictionary[token] += 1
        
    if concept_including_prefix not in concept_including_prefix_count_dictionary:
        concept_including_prefix_count_dictionary[concept_including_prefix] = 1
    else:
        concept_including_prefix_count_dictionary[concept_including_prefix] += 1
    
    if concept_without_prefix not in concept_without_prefix_count_dictionary:
        concept_without_prefix_count_dictionary[concept_without_prefix] = 1
    else:
        concept_without_prefix_count_dictionary[concept_without_prefix] += 1        

test_file.close() 

test_file_length = len(test_file_lines)
print("> length of the test file:\t{0}".format(test_file_length))


print("> number of sentences:\t{0}".format(sentences_count))

total_number_of_tokens = 0
for token_count in token_count_dictionary.values():
    total_number_of_tokens += token_count
print("> number of tokens:\t{0}".format(total_number_of_tokens))  

number_of_tokens = len(token_count_dictionary)
print("> number of unique tokens:\t{0}".format(number_of_tokens))

number_of_concepts_including_prefix = len(concept_including_prefix_count_dictionary)
print("> number of unique concepts including prefix:\t{0}".format(number_of_concepts_including_prefix))

number_of_concepts_without_prefix = len(concept_without_prefix_count_dictionary)
print("> number of concepts without prefix:\t{0}".format(number_of_concepts_without_prefix))
print("---------------------------------------------------------------------------------------------")

# ### Test with features file analysis

test_file = open(TEST_FEATS_FILE, "r")

token_count_dictionary = {}
pos_count_dictionary = {}
lemma_count_dictionary = {}
sentences_count = 0
test_file_lines = []

for line in test_file:
    line = line.replace("\n", "")
    test_file_lines.append(line)
    
    if len(line) == 0: #check if end of sentence
        sentences_count += 1
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 3)
    
    token = line_split[0]
    pos = line_split[1]
    lemma = line_split[2]
    
    if token not in token_count_dictionary:
        token_count_dictionary[token] = 1
    else:
        token_count_dictionary[token] += 1
        
    if pos not in pos_count_dictionary:
        pos_count_dictionary[pos] = 1
    else:
        pos_count_dictionary[pos] += 1
        
    if lemma not in lemma_count_dictionary:
        lemma_count_dictionary[lemma] = 1
    else:
        lemma_count_dictionary[lemma] += 1
    
test_file.close()

test_file_length = len(test_file_lines)
print("> length of the test file:\t{0}".format(test_file_length))


print("> number of sentences:\t{0}".format(sentences_count))

total_number_of_tokens = 0
for token_count in token_count_dictionary.values():
    total_number_of_tokens += token_count
print("> number of tokens:\t{0}".format(total_number_of_tokens)) 


number_of_tokens = len(token_count_dictionary)
print("> number of unique tokens:\t{0}".format(number_of_tokens))


number_of_pos = len(pos_count_dictionary)
print("> number of pos:\t{0}".format(number_of_pos))

number_of_lemma = len(lemma_count_dictionary)
print("> number of unique lemmas:\t{0}".format(number_of_lemma))
print("---------------------------------------------------------------------------------------------")



# ### Compute OOV rate
train_file = open(TRAIN_FILE, "r")

train_tokens = []

for line in train_file:
    line = line.replace("\n", "")
    
    if len(line) == 0: #check if end of sentence
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 2)
    
    token = line_split[0]
    
    if token not in train_tokens:
        train_tokens.append(token)
        
train_file.close()

test_tokens = []
oov_tokens = []

test_file = open(TEST_FILE, "r")

for line in test_file:
    line = line.replace("\n", "")
    
    if len(line) == 0: #check if end of sentence
        continue
    
    line_split = line.split("\t")
    assert(len(line_split) == 2)
    
    token = line_split[0]
    
    if token not in test_tokens:
        test_tokens.append(token)
    
    if token not in train_tokens:
        if token not in oov_tokens:
            oov_tokens.append(token)
        
test_file.close()

print("> OOV rate:\t{0}".format(len(oov_tokens)/len(test_tokens)))
#------------------------------------------------------------------------------------------------------



