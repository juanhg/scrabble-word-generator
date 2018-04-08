import unittest
from dictionary import Dictionary
from parameterized import parameterized


class TestDictionary(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDictionary, self).__init__(*args, **kwargs)
        self.dictionary = Dictionary('doc/dictionary.json')

    def test_initializer_with_invalid_dictionary_path_must_create_empty_dictionary(self):
        dictionary = Dictionary('doc/invalid_dictionary.json')
        is_empty = dictionary.is_empty()
        self.assertTrue(is_empty)

    def test_initializer_with_valid_dictionary_path_must_initialize_words_dictionary(self):
        is_empty = self.dictionary.is_empty()
        self.assertFalse(is_empty)

    @parameterized.expand(['Three', 'valid', 'words'])
    def test_is_valid_word_with_actual_word_must_return_true(self, word):
        result = self.dictionary.is_valid_word(word)
        self.assertTrue(result)

    @parameterized.expand(['Thr33', 'in-valid', '$words', ''])
    def test_is_valid_word_with_not_wrong_word_must_return_false(self, invalid_word):
        result = self.dictionary.is_valid_word(invalid_word)
        self.assertFalse(result)

    @parameterized.expand(['I', 'a'])
    def test_is_valid_scrabble_word_with_actual_one_letter_word_must_return_false(self, word):
        result = self.dictionary.is_valid_scrabble_word(word)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()



