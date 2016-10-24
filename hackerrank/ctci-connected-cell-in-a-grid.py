def get_biggest_region(grid, n, m):
    def check_me(ii, jj):
        area = 0
        for j in range(max(0, jj-1), min(m, jj+2)):
            for i in range(max(0, ii-1), min(n, ii+2)):
                if grid[j][i] == 1:
                    area += 1
                    grid[j][i] = 2
                    area += check_me(i, j)
        return area
    marea = 0
    for j in range(m):
        for i in range(n):
            if grid[j][i] == 1:
                area = check_me(i, j)
                if area > marea:
                    marea = area
    return marea

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid, m, n)
