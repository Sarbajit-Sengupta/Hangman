import unittest
from hangman import get_valid_word


class WordTests(unittest.TestCase):
    def test_only_guessable_words(self):
        self.assertEqual(get_valid_word(['bad-word', 'two words', "can't", '123', '', 'café', 'apple']), 'APPLE')

    def test_no_playable_words(self):
        for words in ([], ['two words', 'bad-word', "can't"]):
            with self.assertRaises(ValueError):
                get_valid_word(words)


if __name__ == '__main__':
    unittest.main()
