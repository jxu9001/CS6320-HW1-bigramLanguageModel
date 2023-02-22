from math import exp, log
from string import punctuation


def preprocess(line):
    """
    Processes a line in the training corpus by removing punctuation, combining hyphenated words and contractions,
    and adding BOS/EOS tokens
    """
    my_punctuation = punctuation.replace("'", '').replace('-', '')
    line = line.lstrip(punctuation).rstrip(punctuation)
    line = line.translate(str.maketrans('', '', my_punctuation)).split()
    processed_line = []

    i = 0
    while i < len(line):
        if line[i] in my_punctuation:
            i += 1
        elif line[i] in ('-', "'"):
            i += 1
            processed_line[-1] += line[i]
            i += 1
        else:
            processed_line.append(line[i])
            i += 1

    processed_line.insert(0, '<s>')
    processed_line.append('</s>')
    return processed_line


def get_bigrams(sentence):
    """
    Given a sentence represented as a list, return a list of the bigrams in the sentence
    """
    n = len(sentence)
    return [(sentence[i], sentence[i + 1]) for i in range(n - 1)]


def print_table_header(sentence):
    """
    Prints the table header
    """
    header = '{:>10}'.format('')
    for word in sentence:
        header += '{:>10}'.format(word)
    print(header)


def print_counts_row(sentence, bigram_counts):
    """
    Prints a row in the bigram counts table
    """
    for word1 in sentence:
        row = '{:>10}'.format(word1)
        for word2 in sentence:
            row += '{:>10}'.format(bigram_counts[word1, word2])
        print(row)


def print_probs_row(sentence, unigram_counts, bigram_counts):
    for word1 in sentence:
        row = '{:>10}'.format(word1)
        for word2 in sentence:
            bigram_prob = bigram_counts[word1, word2] / unigram_counts[word1] if unigram_counts[word1] else 0
            row += '{:>10f}'.format(bigram_prob)
        print(row)


def get_sentence_probability(sentence, unigram_counts, bigram_counts):
    """
    Returns the probability of the sentence
    """
    sentence_probability = 0
    bigrams = get_bigrams(sentence)

    for bigram in bigrams:
        if bigram_counts[bigram] == 0:
            return 0
        sentence_probability += log(bigram_counts[bigram] / unigram_counts[bigram[0]])

    return exp(sentence_probability)


def print_tables_and_probabilities(sentence, unigram_counts, bigram_counts, smoothing):
    """
    Prints the bigram counts, bigram probabilities, and sentence probability for a given sentence
    """
    sentence = preprocess(sentence)
    sentence_as_str = ' '.join(sentence)

    print('The bigram counts for the sentence \"{}\"'.format(sentence_as_str))
    print_table_header(sentence)
    print_counts_row(sentence, bigram_counts)

    print('\nThe bigram probabilities for the sentence \"{}\"'.format(sentence_as_str))
    print_table_header(sentence)
    print_probs_row(sentence, unigram_counts, bigram_counts)

    sentence_probability = get_sentence_probability(sentence, unigram_counts, bigram_counts)
    if smoothing == 0:
        print('\nP(\"{}\") without add-one smoothing is {}\n'.format(sentence_as_str, sentence_probability))
    elif smoothing == 1:
        print('\nP(\"{}\") with add-one smoothing is {}\n'.format(sentence_as_str, sentence_probability))
