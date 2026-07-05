from functools import lru_cache
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        def value(i, j):
            if board[i][j] in "SE":
                return 0
            return int(board[i][j])

        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0 or board[i][j] == 'X':
                return (-1, 0)

            if board[i][j] == 'E':
                return (0, 1)

            bestScore = -1
            ways = 0

            for ni, nj in [(i-1, j), (i, j-1), (i-1, j-1)]:
                score, cnt = dfs(ni, nj)

                if score == -1:
                    continue

                if score > bestScore:
                    bestScore = score
                    ways = cnt
                elif score == bestScore:
                    ways = (ways + cnt) % MOD

            if bestScore == -1:
                return (-1, 0)

            return (bestScore + value(i, j), ways)

        score, ways = dfs(n - 1, n - 1)

        if score == -1:
            return [0, 0]

        return [score % MOD, ways % MOD]