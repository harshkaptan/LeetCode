from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        @lru_cache(None)
        def dfs(players):
            l = len(players)
            res = [float('inf'), -float('inf')]
            for i in range(l // 2):
                a, b = players[i], players[-(i + 1)]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return [1, 1]
            matchups = []
            for i in range(l // 2):
                a, b = players[i], players[-(i + 1)]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return [1, 1]
                elif a in {firstPlayer, secondPlayer}:
                    matchups.append([a])
                elif b in {firstPlayer, secondPlayer}:
                    matchups.append([b])
                else:
                    matchups.append([a, b])
            if l % 2 == 1:
                matchups.append([players[l // 2]])

            def backtrack(i, curr):
                if i == len(matchups):
                    new_players = tuple(sorted(curr))
                    sub = dfs(new_players)
                    res[0] = min(res[0], sub[0] + 1)
                    res[1] = max(res[1], sub[1] + 1)
                    return
                for p in matchups[i]:
                    backtrack(i + 1, curr + [p])

            backtrack(0, [])
            return res

        return dfs(tuple(range(1, n + 1)))
