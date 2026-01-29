from typing import List, Literal

def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
  lines = board.split("\n")
  lines.pop()
  lines.pop(0)
  positionRobot = 0
  positionLineRobot = 0
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if (lines[i][j] == "@"):
        positionRobot = j
        positionLineRobot = i
        break;
  for i in range(len(moves)):
    match moves[i]:
      case 'U': positionLineRobot -= 1
      case 'D': positionLineRobot += 1
      case 'L': positionRobot -= 1
      case 'R': positionRobot += 1
    if (positionLineRobot < 0 or positionLineRobot > 3 or
        positionRobot < 0 or positionRobot > 4):
      return 'crash'
    match lines[positionLineRobot][positionRobot]:
      case '*': return 'success'
      case '#': return 'crash'
  return 'fail'

board = """
.....
.*#.*
.@...
.....
"""

print(move_reno(board, 'D'))
print(move_reno(board, 'U'))
print(move_reno(board, 'RU'))
print(move_reno(board, 'RRRUU'))
print(move_reno(board, 'DD'))
print(move_reno(board, 'UUU'))
print(move_reno(board, 'RR'))