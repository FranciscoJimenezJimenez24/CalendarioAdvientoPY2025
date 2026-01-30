def elf_battle(elf1: str, elf2: str) -> int:
  elf1Points = elf2Points = 3
  turns = len(elf1)

  for i in range(turns):
    if (elf1[i] == "A" and elf2[i] != "B"): 
      elf2Points -= 1
    elif (elf1[i] == "F"): elf2Points -= 2
    if (elf2[i] == "A" and elf1[i] != "B"): 
      elf1Points -= 1
    elif (elf2[i] == "F"): elf1Points -= 2

    if (elf1Points <= 0 and elf2Points <= 0): return 0
    if (elf1Points <= 0): return 2
    if (elf2Points <= 0): return 1

  if (elf1Points > elf2Points): return 1
  if (elf2Points > elf1Points): return 2
  return 0

print(elf_battle('A', 'B'))

print(elf_battle('F', 'B'))

print(elf_battle('AAB', 'BBA'))

print(elf_battle('AFA', 'BBA'))

print(elf_battle('AFAB', 'BBAF'))

print(elf_battle('AA', 'FF'))