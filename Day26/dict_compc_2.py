from unittest import result


sentence = "Hello, for some reason, this is a sentence".split()

result = {word:len(word) for word in sentence}
print(result)