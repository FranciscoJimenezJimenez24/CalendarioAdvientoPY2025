def decode_santa_pin(code: str) -> str:
  lastNumber = ""
  pin = ""
  codeArray = code.split("]")
  codeArray.pop()
  if len(codeArray) != 4: return None
  for i in range(len(codeArray)):
    block = codeArray[i].replace("[","")
    if (len(block) > 1):
      digit = 0
      if (block[1] == "+"):
        digit = int(block[0]) + 1*(len(block)-1)
      else:
        digit = int(block[0]) - 1*(len(block)-1)
      digit = digit % 10
      lastNumber = f"{digit}"
      pin += lastNumber
    else:
      if (block[0] == "<"): 
        pin += lastNumber
      else:
        pin += f"{block[0]}"
        lastNumber = block[0]
  return pin

text = decode_santa_pin('[9+][<][<][<]')
print(text)