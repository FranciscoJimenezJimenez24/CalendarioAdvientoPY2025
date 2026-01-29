def max_depth(s: str) -> int:
  openBracket = s.count("[")
  closeBracket = s.count("]")

  if (closeBracket != openBracket or s[0] == "]" or s[-1] == "["): return -1

  wishIntensity = 0
  intensity = 0
  for i in range(len(s)):
    if(s[i] == "["):
      intensity += 1
      if (wishIntensity < intensity): wishIntensity = intensity
    elif s[i] == "]":
      intensity -= 1
  return wishIntensity

print(max_depth('[]'))
print(max_depth('[[]]'))
print(max_depth('[][]'))
print(max_depth('[[][]]'))
print(max_depth('[[[]]]'))
print(max_depth('[][[]][]'))
print(max_depth(']['))
print(max_depth('[[['))
print(max_depth('[]]]'))
print(max_depth('[][]['))