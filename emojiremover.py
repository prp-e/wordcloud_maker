from hazm import word_tokenize 
''' using hazm's word tokenizer ''' 
def remove_emojis(text, emojis="emojis.txt"):
    ''' Removes emojis from a given text! ''' 
    emoji_list = open(emojis)
    emoji_list = emoji_list.readlines()
    emoji_list = emoji_list[0]
    emoji_list_functional = []
    for emoji_char in emoji_list:
        emoji_list_functional.append(emoji_char)
    text = word_tokenize(text)
    clean_text = [] 
    for word_token in text:
        for emoji_char in emoji_list_functional:
            word_token = word_token.replace(emoji_char, '')
        clean_text.append(word_token)
    return clean_text


