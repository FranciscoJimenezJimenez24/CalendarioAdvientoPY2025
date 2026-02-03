def pack_gifts(gifts: list[int], maxWeight: int) -> int | None:
  for gift in gifts:
    if gift > maxWeight: return None

  sleds = 0
  sumWeights = 0
 
  for gift in gifts:
    if sumWeights + gift > maxWeight:
      sleds += 1              
      sumWeights = gift 
    else:
      sumWeights += gift

  if sumWeights > 0:
    sleds += 1

  return sleds

print(pack_gifts([2, 3, 4, 1], 5))
print(pack_gifts([3, 3, 2, 1], 3))
print(pack_gifts([1, 1, 1, 1], 2))
print(pack_gifts([5, 6, 1], 5))
print(pack_gifts([], 10))
print(pack_gifts([1, 2, 3, 4, 5], 10))
print(pack_gifts([5, 5, 5, 5], 5))