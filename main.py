# Jerry Xu
# CS 6320 Spring 2023 Homework 1 (Bigram Language Model)
# Instructor: Professor Dan Moldovan

from collections import defaultdict
from sys import argv
from utils import *

sentence1 = 'mark antony shall say i am not well , and for thy humor , i will stay at home.'
sentence2 = 'talke not of standing . publius good cheere , there is no harme intended to your person , nor to no ' \
            'roman else : so tell them publius '


def main():
    # command line args
    train_file = argv[1]
    smoothing = int(argv[2])
    assert smoothing in (0, 1)

    # dictionaries to hold various needed counts
    unigram_counts = defaultdict(int)
    bigram_counts = defaultdict(int)

    # process each line in the training corpus
    with open(train_file) as f:
        for line in f:
            processed_line = preprocess(line)
            line_length = len(processed_line)
            # update unigram counts and bigram counts
            for word in processed_line:
                unigram_counts[word] += 1
            for i in range(line_length - 1):
                curr_word = processed_line[i]
                next_word = processed_line[i + 1]
                bigram_counts[curr_word, next_word] += 1

    # calculate add-one counts
    add_one_unigram_counts = {unigram: count + len(unigram_counts) for unigram, count in unigram_counts.items()}
    add_one_bigram_counts = {bigram: count + 1 for bigram, count in bigram_counts.items()}

    # print bigram counts, bigram probabilities, probabilities of each sentence
    if smoothing == 0:
        print_tables_and_probabilities(sentence1, unigram_counts, bigram_counts, smoothing)
        print_tables_and_probabilities(sentence2, unigram_counts, bigram_counts, smoothing)
    if smoothing == 1:
        print_tables_and_probabilities(sentence1, add_one_unigram_counts, add_one_bigram_counts, smoothing)
        print_tables_and_probabilities(sentence2, add_one_unigram_counts, add_one_bigram_counts, smoothing)

if __name__ == '__main__':
    main()
