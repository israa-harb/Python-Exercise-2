import string 
def count_words(text):
    mydict = {}
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()

    for word in words:
        word = word.lower()
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1

    return mydict

text = "AI is the future. The future is now."
print(count_words(text))
