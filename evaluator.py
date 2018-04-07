class Evaluator:
    def __init__(self):
        self._scores = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2,
            'E': 1, 'F': 4, 'G': 2, 'H': 4,
            'I': 1, 'J': 8, 'K': 5, 'L': 1,
            'M': 3, 'N': 1, 'O': 1, 'P': 3,
            'Q': 10, 'R': 1, 'S': 1, 'T': 1,
            'U': 1, 'V': 4, 'W': 4, 'X': 8,
            'Y': 4, 'Z': 10,
        }

    def is_valid_char(self, char):
        return char.isalpha() and char.upper() in self._scores

    def get_char_score(self, char):
        upper_char = char.upper()
        return self._scores[upper_char] if self.is_valid_char(upper_char) else 0

    def get_word_score(self, word):
        score = 0
        for char in word:
            if self.is_valid_char(char):
                score += self.get_char_score(char)
            else:
                return 0
        return score;

    def get_scores(self):
        return self._scores
