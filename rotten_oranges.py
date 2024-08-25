# time: O(n)
# space: O(1)

class Solution(object):
    def orangesRotting(self, grid):
        # if len(grid) == 1 and len(grid[0]) == 1 and (grid[0][0] == 0 or grid[0][0] == 2):
        #     return 0
        q = []
        time = 0
        dirs = [[0,-1], [0, 1], [-1,0], [1,0]]
        for i in  range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
        while q:
            size = len(q)
            for i in range(size):
                curr = q.pop(0)
                r, c = curr[0], curr[1]
                for d in dirs:
                    rn, cn = r + d[0], c + d[1]
                    if rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid[0]):
                        if grid[rn][cn] == 1:
                            grid[rn][cn] = 2
                            q.append([rn, cn])
            time += 1
        flag = 0
        for i in  range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = 1
                    break
                if flag == 1:
                    break
        if flag == 0 and time != 0:
            return time - 1
        elif flag == 0 and time == 0:
            return time
        else:
            return -1