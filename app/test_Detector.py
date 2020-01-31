from unittest import TestCase
from .Detector import Detector


class TestDetector(TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        super(TestDetector, cls).setUpClass()
        cls.model = Detector()

    def testHavingAnswer(self):
        result = self.model.detect('sag')
        self.assertIn('answer', result)

    def testHavingSpamWords(self):
        result = self.model.detect('sag')
        self.assertIn('spam_words', result)

    def testSpamWordsLength(self):
        result = self.model.detect('salam sag chetori khubi')
        spam_words = result['spam_words'].replace(' ', '').split('-')
        self.assertLess(len(spam_words), 4)
