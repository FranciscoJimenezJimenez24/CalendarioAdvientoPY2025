def draw_gift(size, symbol):
  spaces = size - 2
  edge = symbol*size
  if (size < 2): return ""
  return edge+"\n" + (symbol+" "*spaces+symbol+"\n")*spaces + edge

g1 = draw_gift(3, '#')
print(g1)