import itertools


class Generator:
    def __init__(self, evaluator, dictionary):
        self._evaluator = evaluator
        self._dictionary = dictionary

    def generate_words(self, char_list):
        words = []
        if not char_list or len(char_list) < 2:
            return words

        for i in range(2, len(char_list) + 1):
            permutations = itertools.permutations(char_list, i)
            words.extend([''.join(p) for p in permutations])

        valid_words = [word for word in words if self._dictionary.is_valid_scrabble_word(word)]
        scores = map(self._evaluator.get_word_score, valid_words)
        scored_words = zip(valid_words, scores)
        sorted_scored_word = sorted(scored_words, key=lambda x: x[1], reverse=True)

        return sorted_scored_word
