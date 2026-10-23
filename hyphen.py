def addition_of_hyphen(sentence):
    modified_sentence=sentence.replace(' ','-')
    return modified_sentence
sentence=input("Enter a sentence with more than one words")
modified_result=addition_of_hyphen(sentence)
print("Original sentence:",sentence)
print("Modified sentence",modified_result)
