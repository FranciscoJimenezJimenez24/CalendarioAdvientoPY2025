def find_gift_path(workshop: dict, gift: str | int | bool) -> list[str]:
  levels = []
  for clave, valor in workshop.items():
    if valor == gift:
      levels.append(clave)
      return levels
    if isinstance(valor, dict):
      subLevels = find_gift_path(valor, gift)
      if subLevels: 
        levels.append(clave)
        levels.extend(subLevels)
        return levels
  return levels

workshop = {
  "storage": {
    "shelf": {
      "box1": 'train',
      "box2": 'switch'
    },
    "box": 'car'
  },
  "gift": 'doll'
}

print(find_gift_path(workshop, 'train'))
print(find_gift_path(workshop, 'switch'))
print(find_gift_path(workshop, 'car'))
print(find_gift_path(workshop, 'doll'))
print(find_gift_path(workshop, 'plane'))