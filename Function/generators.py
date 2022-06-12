from typing import Dict, List


def gen(n):
    for i in (1, 2, 3, 4, 5, 6):
        yield i * n


for i in gen(5):
    print(i)
print(gen(2))

fromDatabase = [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    },
    {
        "color": "cyan",
        "value": "#0ff"
    },
    {
        "color": "magenta",
        "value": "#f0f"
    },
    {
        "color": "yellow",
        "value": "#ff0"
    },
    {
        "color": "black",
        "value": "#000"
    }
]

# fromDatabase = {
#     "color": "black",
#     "value": "#000"
# }

# Generally doing manual access to Json data
# for i in dataFromDatabase:
#     for j in i.keys():
#         print(j, i[j])
#     print()


def genData(rawData):
    Data = rawData if type(rawData) != dict else [rawData]
    for i in Data:
        yield i


colorlist = genData(fromDatabase)

for color in colorlist:
    print(color)
