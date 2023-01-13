# Practice file

import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

word4 = nlp("frog")
word5 = nlp("toad")
word6 = nlp("dog")


print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

tokens = nlp('cat apple monkey banana fruit kitten')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana",
             "Hey, my cat is on top of the car"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# I found the interesting thing about the monkey and banana example was that spacy can group by category and
# by association. When I then tried frog, toad and dog it knew that a frog and toad were almost identical.

# I noticed that en_core_web_md has much more extra detail and information that web_sm which is more about
# surface level similarities.
