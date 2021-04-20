import json 
import sys

json_file = sys.argv[1]

jsons = []
jsons_parsed = []

with open(json_file) as j:
    for line in j.readlines():
        jsons.append(line)
