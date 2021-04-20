import json 
import sys

json_file = sys.argv[1]

jsons = []
jsons_parsed = []

with open(json_file) as j:
    for line in j.readlines():
        jsons.append(line.rstrip('\n'))

for obj in jsons:
    jsons_parsed.append(json.loads(obj))

tweets = []
for obj in jsons_parsed:
    text = obj['tweet']
    tweets.append(text)

with open('tweets.txt', 'w') as output:
    for tweet in tweets:
        output.write(tweet + '\n')

    