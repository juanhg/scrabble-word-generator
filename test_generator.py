import unittest
from generator import Generator
from parameterized import parameterized


class TestGenerator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGenerator, self).__init__(*args, **kwargs)
        evaluator = EvaluatorStub()
        dictionary = DictionaryStub()
        self.generator = Generator(evaluator, dictionary)

    def test_generate_words_with_one_element_list_must_return_empty_list(self):
        result = self.generator.generate_words(['A'])
        self.assertEquals(result, [])

    @parameterized.expand([
        (['$', 'a'], []),
        (['x', 'c', 'd'], [])
    ])
    def test_generate_words_with_invalid_list_must_return_empty_list(self, invalid_list, expected):
        result = self.generator.generate_words(invalid_list)
        self.assertEquals(result, expected)

    @parameterized.expand([
        (['a', 'c', 'e', 'x'], 4),
        (['a', 'x', 'e'], 3),
        (['a', 'c', 'e'], 1)
    ])
    def test_generate_combination_with_valid_list_should_return_list_with_proper_len(self, valid_list, expected):
        words = self.generator.generate_words(valid_list)
        result = len(words)
        self.assertEquals(result, expected)

    @parameterized.expand([
        (['a', 'c', 'e', 'x'], [('axe', 10), ('ax', 9), ('ex', 9), ('ace', 5)]),
        (['a', 'x', 'e'], [('axe', 10), ('ax', 9), ('ex', 9)])
    ])
    def test_generate_combination_with_valid_list_should_return_list_sorted_by_desc_score(self, valid_list, expected):
        result = self.generator.generate_words(valid_list)
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()


class EvaluatorStub:
    def __init__(self):
        self._scores = {
            'axe': 10,
            'ax': 9,
            'ex': 9,
            'ace': 5
        }

    def get_word_score(self, word):
        return self._scores[word]


class DictionaryStub:
    def __init__(self):
        pass

    @staticmethod
    def is_valid_scrabble_word(word):
        return word.lower() in ['ace', 'axe', 'ax', 'ex']

