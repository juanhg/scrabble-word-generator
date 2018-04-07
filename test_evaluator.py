import unittest
from parameterized import parameterized, param
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

    @parameterized.expand(['A', 'D', 'P', 'X', 'Z'])
    def test_is_valid_char_with_char_between_A_and_Z_must_return_true(self, valid_char):
        evaluator = Evaluator()
        result = evaluator.is_valid_char(valid_char)
        self.assertTrue(result)

    @parameterized.expand(['', '$', '#', '1', '20'])
    def test_get_char_score_with_invalid_char_must_return_0(self, invalid_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(invalid_char)
        self.assertEquals(result, 0)

    @parameterized.expand(['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'])
    def test_get_char_score_with_very_common_char_must_return_1(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 1)

    @parameterized.expand(['D', 'G'])
    def test_get_char_score_with_common_char_must_return_2(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 2)

    @parameterized.expand(['B', 'C', 'M', 'P'])
    def test_get_char_score_with_infrequent_char_must_return_3(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 3)

    @parameterized.expand(['F', 'H', 'V', 'W', 'Y'])
    def test_get_char_score_with_very_infrequent_char_must_return_4(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 4)

    @parameterized.expand(['K'])
    def test_get_char_score_with_rare_char_must_return_5(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 5)

    @parameterized.expand(['X', 'J'])
    def test_get_char_score_with_very_rare_char_must_return_8(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 8)

    @parameterized.expand(['Q', 'Z'])
    def test_get_char_score_with_ultra_rare_char_must_return_10(self, common_char):
        evaluator = Evaluator()
        result = evaluator.get_char_score(common_char)
        self.assertEquals(result, 10)

    def test_get_word_score_with_invalid_word_must_return_zero(self):
        self.fail()

    def test_get_word_score_with_valid_word_must_return_the_sum_of_all_char_scores(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
