def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:
  # order the data
  dataSorted = sorted(data, key=lambda listElement:listElement[sortBy])

  # the length of every column
  maxLengthColumn = []
  for i in range(len(dataSorted)):
    for j, (clave, valor) in enumerate(dataSorted[i].items()):
      if len(maxLengthColumn) < len(dataSorted[0]):
        maxLengthColumn.append(len(str(valor)))
      else:
        if (maxLengthColumn[j] < len(str(valor))):
          maxLengthColumn[j] = len(str(valor))
  
  # the border of the table
  borderTable = "+"
  for i in range(len(maxLengthColumn)):
    borderTable += "-"*(maxLengthColumn[i] + 2) + "+"

  # the header of the table
  header = borderTable + "\n|"
  for i in range(len(maxLengthColumn)):
    header += " " + chr((i+1) + 64) + " "*(maxLengthColumn[i]) + "|"
  header += "\n" + borderTable

  # the structure of the table
  table = header + "\n"
  for i in range(len(dataSorted)):
    table += "|"
    for j, (clave, valor) in enumerate(dataSorted[i].items()):
      table += " " + str(valor) + " "*(maxLengthColumn[j] - len(valor) + 1) + "|"
    table += "\n"
  return table + borderTable
  


print(draw_table(
  [
    { "gift": 'Book', "quantity": 5 },
    { "gift": 'Music CD', "quantity": 1 },
    { "gift": 'Doll', "quantity": 10 }
  ],
  'quantity'
))

print(draw_table(
  [
    { "name": 'Charlie', "city": 'New York' },
    { "name": 'Alice', "city": 'London' },
    { "name": 'Bob', "city": 'Paris' }
  ],
  'name'
))