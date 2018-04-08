import json
import os


class Dictionary:
    def __init__(self, dictionary_path='doc/dictionary.json'):
        file_exists = os.path.isfile(dictionary_path)
        self._dictionary = json.load(open(dictionary_path)) if file_exists else {}

    def is_valid_scrabble_word(self, word):
        return self.is_valid_word(word) and len(word) > 1

    def is_valid_word(self, word):
        return word.lower() in self._dictionary

    def is_empty(self):
        return not self._dictionary