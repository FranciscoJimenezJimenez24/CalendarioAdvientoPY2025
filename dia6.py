from typing import List, Dict

# def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
#   pairs = []
#   colours = []
#   for glove in gloves:
#     colours.append(glove["color"])
#   colours = list(set(colours))
#   matches = list(set(colours))
#   for glove in gloves:
#     for i in range (len(colours)):
#       if (colours[i] == glove["color"]):
#         matches[i] += glove["hand"]
#   for i in range (len(matches)):
#     left = matches[i].count("L")
#     right = matches[i].count("R")
#     if (left != 0 and right != 0):
#       j = 0
#       minus = ""
#       if (left > right): minus = right
#       elif (right > left): minus = left
#       else: minus = right
#       while (j < minus):
#         pairs.append(matches[i][:-(left+right)])
#         j+=1
#   return pairs

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
  pairs = []
  for glove in gloves:
    for glovePosition in gloves:
      if glovePosition["hand"] != glove["hand"] and glovePosition["color"] == glove["color"]:
        pairs.append(glove["color"])
        gloves.remove(glove)
        gloves.remove(glovePosition)
  return pairs

gloves = [
  { "hand": 'R', "color": 'blue' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'R', "color": 'blue' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'L', "color": 'blue' }
]

print(match_gloves(gloves))
