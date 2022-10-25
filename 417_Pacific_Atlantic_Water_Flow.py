from collections import deque

# BFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        num_rows, num_cols = len(heights), len(heights[0])

        pacific_q, atlantic_q = deque(), deque()

        for i in range(num_rows):
            pacific_q.append((i, 0))
            atlantic_q.append(((i, num_cols - 1)))
        
        for i in range(num_cols):
            pacific_q.append((0, i))
            atlantic_q.append((num_rows-1 , i))

        def bfs(queue):
            reachable = set()
            while queue:
                row, col = queue.popleft()
                reachable.add((row, col))
                for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    
                    if heights[new_row][new_col] < heights[row][col]:
                        continue

                    queue.append((new_row, new_col))
            return reachable

        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)

        return list(pacific_reachable & atlantic_reachable)


# Time Complexity: O(R*C) R: num of rows, C: num of cols
# Space ComplexityL O(R*C)
