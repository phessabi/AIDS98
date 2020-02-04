import random


class Detector:
    def __init__(self):
        """
            load models for AI
        """
        self.model = None

    def detect(self, sentence):
        model = self.model
        words = sentence.split()
        if len(words) == 0:
            return {'answer': False, 'spam_words': ''}
        spam_words = set()
        for word in random.choices(words, k=3):
            spam_words.add(word)
        spam_words_str = ''
        for word in spam_words:
            spam_words_str += word + ' - '
        spam_words_str = spam_words_str[:-3]
        answer = True
        if random.random() > 0.5:
            answer = False
        return {'answer': answer, 'spam_words': spam_words_str}
