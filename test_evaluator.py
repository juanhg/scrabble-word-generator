import unittest
from parameterized import parameterized
from evaluator import Evaluator


class TestEvaluator(unittest.TestCase):
    def test_can_create_evaluator(self):
        Evaluator()

    def test_initializer_must_initialize_scores_dictionary(self):
        evaluator = Evaluator()
        scores_len = len(evaluator.get_scores())
        self.assertEquals(scores_len, 26)

    @parameterized.expand(['', '$', '#', '1', '20'])
    def test_is_valid_char_with_empty_symbols_or_numbers_must_return_false(self, invalid_char):
        evaluator = Evaluator()
        result = evaluator.is_valid_char(invalid_char)
        self.assertFalse(result)

    @parameterized.expand(['A', 'D', 'P', 'X', 'Z', 'b', 'c', 'd', 'j'])
    def test_is_valid_char_with_char_between_a_and_Z_must_return_true(self, valid_char):
        evaluator = Evaluator()
        result = evaluator.is_valid_char(valid_char)
        self.assertTrue(result)

    @parameterized.expand(['', '$', '#', '1', '20'])
    def test_get_char_score_with_invalid_char_must_return_0(self, invalid_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(invalid_char)
        self.assertEquals(result, 0)

    @parameterized.expand([
        (['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 1),
        (['D', 'G'], 2),
        (['B', 'C', 'M', 'P'], 3),
        (['F', 'H', 'V', 'W', 'Y'], 4),
        (['K'], 5),
        (['X', 'J'], 8),
        (['Q', 'Z'], 10)
    ])
    def test_get_char_score_with_valid_char_must_return_proper_positive_integer(self, chars, expected):
        evaluator = Evaluator()
        for char in chars:
            result = evaluator.get_char_score(char)
            self.assertEquals(result, expected)

    @parameterized.expand([
        'a', 'x'
    ])
    def test_get_char_score_with_lowercase_return_equal_than_uppercase(self, lower_char):
        evaluator = Evaluator()
        upper_char = lower_char.upper()
        expected = evaluator.get_char_score(upper_char)
        result = evaluator.get_char_score(lower_char)
        self.assertEquals(result, expected)

    @parameterized.expand([
        'hel o', 'w0rld'
    ])
    def test_get_word_score_with_invalid_char_must_return_zero(self, word):
        evaluator = Evaluator()
        result = evaluator.get_word_score(word)
        self.assertEquals(result, 0)

    @parameterized.expand([
        'Python', 'Rocks'
    ])
    def test_get_word_score_with_valid_word_must_return_the_sum_of_all_char_scores(self, word):
        evaluator = Evaluator()
        chars = [char for char in word]

        expected = sum(map(evaluator.get_char_score, chars))
        result = evaluator.get_word_score(word)
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()
