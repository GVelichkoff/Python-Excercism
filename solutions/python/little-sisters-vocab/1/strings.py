def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    return (" :: " + vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    remove_ness = word[0:-4]
    if remove_ness[len(remove_ness) -1 ] == 'i':
        word_y = remove_ness[0:len(remove_ness) - 1 ] + 'y'
    else:
        word_y = remove_ness
    return word_y



def adjective_to_verb(sentence, index):
    sentence_list = sentence.split(' ')
    word = sentence_list[index].rstrip('.')
    new_word = word + 'en'
    return new_word
    
