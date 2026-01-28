def filter_gifts(gifts):
  goodgifts = []
  for i in range(len(gifts)):
    if "#" not in gifts[i]: 
      goodgifts.append(gifts[i])
  return goodgifts

gifts1 = ['car', 'doll#arm', 'ball', '#train']
good1 = filter_gifts(gifts1)
print(good1)

gifts2 = ['#broken', '#rusty']
good2 = filter_gifts(gifts2)
print(good2)

gifts3 = []
good3 = filter_gifts(gifts3)
print(good3)