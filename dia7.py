def draw_tree(height, ornament, frequency):
  tree = ""
  frequencyOrnament = frequency
  for i in range (height):
    tree += " "*(height-(i+1))
    for j in range(2*(i+1)-1):
      if (frequencyOrnament == 1):
        tree += ornament
        frequencyOrnament = frequency
      else:
        tree += "*"
        frequencyOrnament -= 1
    tree += "\n"
  return tree + " "*(height-1) + "#"