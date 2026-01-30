def find_unsafe_gifts(warehouse: list[str]) -> int:
  unsafeGiftsCount = 0
  copyWarehouse = warehouse[:]

  width = len(copyWarehouse[0])
  copyWarehouse.insert(0, "." * width)
  copyWarehouse.insert(len(copyWarehouse), "." * width)

  for i in range(len(copyWarehouse)):
    copyWarehouse[i] = "." + copyWarehouse[i] + "."

  for i in range(len(copyWarehouse)):
    for j in range(len(copyWarehouse[i])):
      if (copyWarehouse[i][j] == "*"):
        neighbours = [
          copyWarehouse[i][j+1],
          copyWarehouse[i+1][j], 
          copyWarehouse[i][j-1],
          copyWarehouse[i-1][j]
        ]
        if "#" not in neighbours: unsafeGiftsCount+=1
  return unsafeGiftsCount

print(find_unsafe_gifts([
  '.*.',
  '*#*',
  '.*.'
]))

print(find_unsafe_gifts([
  '...',
  '.*.',
  '...'
])) 

print(find_unsafe_gifts([
  '*.*',
  '...',
  '*#*'
]))
print(find_unsafe_gifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]))
print(find_unsafe_gifts([
  '#*.',
  '...',
  '..#'
]))
print(find_unsafe_gifts([
  '...#....',
  '..*#*...',
  '...#....'
]))
print(find_unsafe_gifts([
  '*.*',
  '...',
  '*.*'
]))