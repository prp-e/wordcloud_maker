import re
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
from imageio import imread 
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from hazm import Normalizer
from emojiremover import remove_emojis

# This is the base image for your cloud
cloud_mask = imread('./twitter_mask.png')

# This removes the stop words, thanks to kharazi and my dear pointer for sharing their stop-word lists
stop_words = open("stopwords_fa")
stop_words = [word.rstrip('\n') for word in stop_words.readlines()]

stop_words_additional = open("stopwords_fa_additional.txt")
stop_words_additional = [word.rstrip('\n') for word in stop_words_additional.readlines()]

stop_words_me = open("stopwords_fa_me.txt")
stop_words_me = [word.rstrip('\n') for word in stop_words_me.readlines()]

stop_words = list(set(stop_words + stop_words_additional + stop_words_me)) # Removing any duplicates wich can happen

text_file = open(sys.argv[1])
text_file = text_file.readlines()
text = " ".join(text_file)

'''
This part is responsible for cleaning the text! 
1. It removes all links 
2. Removes mentions 
3. Removes Latin phrases 
4. Cleans stop words 
''' 
text = text.split(' ')
no_url = [] 
url_pattern = r'.*\s+https?:\/\/([-\w\.]+)+(:\d+)?(\/([\w\/_\.]*(\?\S+)?)?)?.*'

for line in text:
    if not re.match(url_pattern, line):
        no_url.append(line)

no_mention = [] 
mention_pattern = r'.*\s+(@).*'

for line in no_url: 
    if not re.match(mention_pattern, line):
        no_mention.append(line)

no_latin = [] 
latin_pattern = r'.*[a-zA-Z].*'

for word in no_mention:
    if not re.match(latin_pattern, word):
        no_latin.append(word)

normal_text = [] 
n = Normalizer()
for word in no_latin:
    normal_text.append(n.normalize(word))


''' Provided a better (somehow :P) way to remove unicod isolators and stop-words ''' 
clean_text = " ".join(no_latin)
clean_text = clean_text.replace('\u2066', '')
clean_text = clean_text.replace('\u2069', '')
clean_text = clean_text.replace('\u2067', '')
clean_text = clean_text.replace('\u2068', '')

weird_chars = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u2069"
                               u"\u2066"
                               u"\u200c"
                               u"\u2068"
                               u"\u2067"
                               "]+", flags=re.UNICODE)

clean_text = weird_chars.sub(r'', clean_text)

verbal_stops = open("verbal_stops.txt")
verbal_stops = [stop.rstrip('\n') for stop in verbal_stops.readlines()]
for stop_word in verbal_stops:
    clean_text = clean_text.replace(stop_word, '')
 
verbless_text = clean_text.split(' ')
clean_text = []
for word in verbless_text:
    if word not in stop_words:
        clean_text.append(word)
 

''' 
Here , we just make up our final text and clean the emojis, then we optimize our code for the Word Cloud library.
It also removes emojis 
''' 
text = " ".join(clean_text)
text = remove_emojis(text)
text = " ".join(text)
text = get_display(arabic_reshaper.reshape(text))

wc = WordCloud(font_path=sys.argv[2], background_color='white', width=1800, height=1800,  mask=cloud_mask).generate(text) 
 
plt.imshow(wc)
plt.axis('off') 
plt.savefig('./wc_test.png', dpi=300) 
plt.close()
plt.show()
