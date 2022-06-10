def displayPathtoPrincess(n,grid):
    #print all the moves here
#To find p
  for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
            drows = princess[0] - mario[0]
            dcols = princess[1] - mario[1]

            return ''.join([
                'UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows,
                'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols])
if '_input' in globals():
    _input = _input.strip().split()
    m = int(_input[0], 10)
    grid = _input[1:]
else:
    m = input()
    grid = []

    for i in xrange(0, m):
        grid.append(raw_input().strip())

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)