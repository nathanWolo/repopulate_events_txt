from os import listdir
from os.path import isfile, join
import json
jsons = [f for f in listdir(".") if isfile(join(".", f)) and "json" in f ]
target = open("_events.txt", "a")
for curjson in jsons:
    f = open(curjson)
    j = json.loads(f.read())
    for event in j["events"]:
        if event["name"] == "Bookmark":
            target.write(curjson + "    ")
            target.write(str(event["tick"]))
            target.write("\n")
    f.close()
target.close()