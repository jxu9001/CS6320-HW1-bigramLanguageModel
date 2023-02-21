import collections
import string
import sys

sentence1 = 'mark antony shall say i am not well , and for thy humor , i will stay at home.'
sentence2 = 'talke not of standing . publius good cheere , there is no harme intended to your person , nor to no ' \
            'roman else : so tell them publius '


def preprocess(line):
    """
    Processes a line in the training corpus
    """
    processed_line = []
    # remove all punctuation except for hyphens and apostrophes
    my_punctuation = string.punctuation.replace("'", '').replace('-', '')
    line = line.lstrip(string.punctuation).rstrip(string.punctuation)
    line = line.translate(str.maketrans('', '', my_punctuation)).split()

    # combine words separated by hyphens or apostrophes into a single word
    i = 0
    n = len(line)
    while i < n:
        if line[i] in my_punctuation:
            i += 1
        elif line[i] in ('-', "'"):
            i += 1
            processed_line[-1] += line[i]
            i += 1
        else:
            processed_line.append(line[i])
            i += 1

    return processed_line

def main():
    # command line args
    train_file = sys.argv[1]
    smoothing = int(sys.argv[2])
    assert smoothing in (0, 1)

    # dictionaries to hold various needed counts
    unigram_counts = collections.defaultdict(int)
    bigram_counts = collections.defaultdict(int)
    possible_bigrams = collections.defaultdict(set)

    # process each line in the training corpus
    with open(train_file) as f:
        for line in f:
            processed_line = preprocess(line)
            line_length = len(processed_line)
            # update unigram counts
            for word in processed_line:
                unigram_counts[word] += 1
            # update bigram counts and possible bigrams
            if line_length >= 2:
                for i in range(line_length - 1):
                    curr_word = processed_line[i]
                    next_word = processed_line[i + 1]
                    bigram_counts[curr_word, next_word] += 1
                    possible_bigrams[curr_word].add(next_word)

    print(len(unigram_counts))


    # print bigram counts, bigram probabilities, probabilities of each sentence
    if smoothing == 0:
        pass
    elif smoothing == 1:
        pass


if __name__ == '__main__':
    main()
