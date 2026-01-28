def decode_santa_pin(code: str) -> str:
  lastNumber = ""
  pin = ""
  codeArray = code.replace("[", "").split("]")
  codeArray.pop()
  if len(codeArray) != 4: return None
  for i in range(len(codeArray)):
    if (len(codeArray[i]) > 1):
      digit = 0
      if (codeArray[i][1] == "+"):
        digit = int(codeArray[i][0]) + 1*(len(codeArray[i])-1)
      else:
        digit = int(codeArray[i][0]) - 1*(len(codeArray[i])-1)
      digit = digit % 10
      lastNumber = f"{digit}"
      pin += lastNumber
    else:
      if (codeArray[i][0] == "<"): 
        pin += lastNumber
      else:
        pin += f"{codeArray[i][0]}"
        lastNumber = codeArray[i][0]
  return pin

text = decode_santa_pin('[9+][<][<][<]')
print(text)