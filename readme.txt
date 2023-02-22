Jerry Xu
CS 6320 Spring 2023
Homework 1 README

*** INSTRUCTIONS ***
1. Ensure that the *.py files and *.txt files are in the same directory
2. Type "python3 main.py <train_file_name> <smoothing>" into the terminal
3. Press enter
smoothing is either 0 (do not use add-one smoothing) or 1 (use add-one smoothing)

*** ASSUMPTIONS ***
1. I considered multiple spellings of the same word as different words (e.g., solider and souldier).
2. I removed all punctuation apart from hyphens and apostrophes.
3. I combined hyphenated words and contractions into a single word. However, this necessarily means that sentences such
as "sir , ' tis your brother cassius ..." become "sirtis your brother cassius ..." after preprocessing.
4. I added BOS and EOS tokens to each preprocessed sentence.

*** INCLUDED FILES ***
main.py (code to read the training corpus, train the bigram model, and print the results of the bigram model)
utils.py (functions for processing text, printing the tables, etc.)
train.txt (training corpus provided by Professor Moldovan (Shakespeare's The Tragedy of Julius Caesar))
output0.txt (output of the model on the two given sentences without using add-one smoothing)
output1.txt (output of the model on the two given sentences when using add-one smoothing)
