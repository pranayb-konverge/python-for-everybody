import sys

ex = {"c": "CAUTION:", "x": "EXCEPTION:"}
count_of_words = {}

try:
    file = open("words.txt")
    data = file.read()
    if len(data) < 1: raise Exception("You have provided empty file.")
    words_list = data.split()
    for word in words_list:
        count_of_words[word] = count_of_words.get(word,0) + 1
except OSError as e:
    print(ex.get("x") + str(e))
    sys.exit(0)
except Exception as e:
    print(ex.get("x") + str(e))
    sys.exit(0)

print("Count of each word:")

"""Get count of more number of word in the generated dictionary"""
largest_count = -1
which_word = None
for key,value in count_of_words.items():
    print(key,value)
    if value > largest_count:
        largest_count = value
        which_word = key
print("\n\"%s\" word occured %s time in the file." % (which_word,largest_count))