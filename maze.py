def print_path(maze, paths, end):
  row, col = end
  while maze[row][col] != '0':
    prev_row, prev_col = paths[row][col]
    if maze[prev_row][prev_col] == ' ':
      if prev_row == row:
        maze[prev_row][prev_col] = '-'
      else:
        maze[prev_row][prev_col] = '|'
    row, col = prev_row, prev_col
  for row in maze:
    print("".join(row))

def find_solution(maze, start, end):
  rows = len(maze)
  cols = len(maze[0])
  
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  
  reached = [start]
  next_reached = []
  tr, tc = end
  
  paths = []
  for i in range(rows):
    paths.append([None] * cols)
  paths[start[0]][start[1]] = -1
  
  while True:
    if len(reached) == 0:
      break

    for step in reached:
      row, col = step
      for d in directions:
        dr, dc = d
        next_row = row + dr
        next_col = col + dc
        if next_row in range(rows) and next_col in range(cols):
          if maze[next_row][next_col] != 'X' and not paths[next_row][next_col]:
            next_reached.append((next_row, next_col))
            paths[next_row][next_col] = (row, col)
            if next_row == tr and next_col == tc:
              print_path(maze, paths, end)
              return

    reached, next_reached = next_reached, []

  print("Can't reach to target")

maze = []
i = 0
for row in open('maze.txt', 'r'):
  row_list = []
  row = row.strip()
  for j, st in enumerate(row):
    row_list.append(st)
    if st == '0':
      start = (i, j)
    elif st == 'F':
      end   = (i, j)
  i += 1

  maze.append(row_list)

find_solution(maze, start, end)