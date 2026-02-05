from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
  pairs = []
  pendientes = []

  for glove in gloves:
    encontrado = False
    
    for posible_pareja in pendientes:
      if (posible_pareja["color"] == glove["color"] and 
        posible_pareja["hand"] != glove["hand"]):
        
        pairs.append(glove["color"])
        pendientes.remove(posible_pareja)
        encontrado = True
        break 
      
    if not encontrado:
      pendientes.append(glove)
          
  return pairs

gloves = [
  { "hand": 'R', "color": 'blue' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'R', "color": 'blue' },
  { "hand": 'L', "color": 'blue' },
  { "hand": 'L', "color": 'blue' }
]

print(match_gloves(gloves))
