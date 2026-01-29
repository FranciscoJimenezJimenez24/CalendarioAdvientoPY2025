def find_unique_toy(toy: str) -> str:
  toyLower = toy.lower()
  letter = ''
  frequencies = {}
  for i in range(len(toyLower)):
    if toyLower[i] in frequencies:
      frequencies[toyLower[i]] += 1
    else:
      frequencies[toyLower[i]] = 1
  
  for i in range (len(toyLower)):
    if (frequencies[toyLower[i]] == 1):
      letter = toy[i]
      break
  return letter