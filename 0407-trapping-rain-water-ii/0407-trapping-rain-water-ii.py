class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Step 1. 테두리 셀을 전부 힙에 넣기
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2. BFS + 최소 힙
        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # 물이 고일 수 있는지 확인
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # 벽 높이는 현재 높이와 이웃 높이 중 더 높은 값으로 갱신
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

        return trapped_water