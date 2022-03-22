possible_characters = list('abcdefghijklmnopqrstuvwxyz1234567890')


class Keyword():

    def __init__(self, word):
        self.word = word

    def get_letter_pos(self, letter):
        return possible_characters.index(letter)

    def tick_with_adding(self):
        i = -1
        new_word = list(self.word)
        while True:
            if abs(i) == len(self.word) + 1:
                new_word.insert(0, possible_characters[0])
                break
            if self.get_letter_pos(self.word[i]) == 25:
                new_word[i] = possible_characters[0]
                i -= 1
                continue
            if self.get_letter_pos(self.word[i]) < 25:
                new_word[i] = possible_characters[self.get_letter_pos(
                    self.word[i]) + 1]
                break
        self.word = "".join(new_word)
