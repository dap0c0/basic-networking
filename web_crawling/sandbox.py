import json
import re
dog_registry = {
    1: {"name": "Frieda"}
}
print(f"Class of dog_registry: {dog_registry.__class__}")
dog_json = json.dumps(dog_registry)
print(f"JSON of dog_registry: {dog_json}")

dog_registry = json.loads(dog_json)
print(f"Class of loaded dog_registry {dog_registry.__class__}")

# Testing with files
data = {
    "https://website_a.com": {
        "hyperlinks": [
            "www.youtube.com",
            "www.bruh.ca",
            "hey_there.inet"
            ],
        "emails": (
            "you@gmail.com",
            "me@proton.me",
            "foo@outlook.ca"
        ),
        "files": [
        ]
    }, 
    "https://website_b.com": {
        "hyperlinks": [
        ],
        "emails": [
        ],
        "files": [   
        ]
    }
}
data_str = json.dumps(data, indent=0)
print(data)
with open("test_file.txt", "w", encoding="utf-8") as write_file:
    json.dump(data, write_file, indent=4)

with open("test_file.txt", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
    print(data)

pattern = re.compile(r"bruh")
dict = {"bruh": pattern}
contained = dict["bruh"]
print(contained.__class__)
print(contained)

non_contained = dict["foo"]
# print(non_contained.__class__)
print(non_contained)