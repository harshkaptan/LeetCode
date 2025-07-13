from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = j = match = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return match
