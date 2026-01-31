def run_factory(factory: list[str]) -> str:
  visited = set()
  i = j = 0
  while (0 <= i < len(factory) and 0 <= j < len(factory[i])):
    if (i, j) in visited: return "loop"
    visited.add((i, j))

    if (factory[i][j] == "."): return "completed"
    elif (factory[i][j] == ">"): 
      j+=1
    elif (factory[i][j] == "<"):
      j-=1
    elif (factory[i][j] == "v"):
      i+=1
    else:
      i-=1
  return 'broken'


print(run_factory([
  '>>.'
]))

print(run_factory([
  '>>>'
]))

print(run_factory([
  '>><'
]))

print(run_factory([
  '>>v',
  '..<'
]))

print(run_factory([
  '>>v',
  '<<<'
]))

print(run_factory([
  '>v.',
  '^..'
]))

print(run_factory([
  'v.',
  '^.'
]))