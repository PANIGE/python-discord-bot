import random

from keras.models import load_model
import time
from keras.preprocessing import text
import os


class predicter:
    def __init__(self, model:str):
        self.model = load_model(model)

    def Evaluate(self, input):
        tokenize = text.Tokenizer(num_words=10000, char_level=False)
        tokenize.fit_on_texts(input)
        word = tokenize.texts_to_matrix(input)
        prediction = self.model.predict(word, verbose=0)[0]
        return prediction[1]



