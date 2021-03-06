def break_words(stuff):
# The below line is a documentation comment, it shows up in PowerShell
## when you use help to understand ex25 and/or a specific function
    """This function will break up words for us."""
# The below line uses the python split function on the argument
## (in this case a string sentence with text). It splits the string
## using the separator defined within the (), I tested with letter 'o'
    words = stuff.split('o')
    return words
    
def sort_words(words):
    """Sorts the words."""
# The below line uses sort function on the argument & returns result
## Here, our sentence (split by above function) is returned in alpha order
    return sorted(words)
    
def print_first_word(words):
    """Prints the first words after popping it off."""
# The below line uses pop function on argument. words variable is a
## list, so pop() returns last item in the list, in this example we are
## telling pop to start at position zero in the list, so it returns 
## first word
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
# The below line uses pop function on argument. words variable is a
## list, so pop() returns last item in the list, in this example we are
## telling pop to start at position -1 which is one spot from the end
## in the list, so it returns last word
    word = words.pop(-1)
    print word

# The below function combines the break_words and sort_words functions in 1
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
# The below function combines break_words, print_first_words, and 
## print_last_words functions into 1
# The output in Python will print the first and last words of the split
## sentence because there is a "print" command in both print_ functions 
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# The below function combines sort_sentence, print_first_ and print_last_
## functions into 1, also note that sort_sentence is already 2 functions
## combined, yeesh, getting deep
# The ouput in Python will print the first and last words of the sorted
## split sentence because of "print" commmand in both print_ functions
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)