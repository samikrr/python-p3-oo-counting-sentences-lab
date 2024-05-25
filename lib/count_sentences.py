#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        # Count sentences ending with ".", "!", or "?"
        sentences = [sentence for sentence in self.value.replace('!', '.').replace('?', '.').split('.') if sentence.strip()]
        return len(sentences)


# Test case
try:
    # Providing a non-string value
    my_string = MyString(123)
except ValueError as e:
    print(e)  # Output: The value must be a string.

# Providing a proper string value
my_string = MyString("This is a test sentence. This is another test sentence.")
print(my_string.count_sentences())  # Output: 2




