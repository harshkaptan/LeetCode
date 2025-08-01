from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]  # Start with the first row
        
        for i in range(1, numRows):
            row = [1]  # Each row starts with 1
            # Compute middle elements based on the previous row
            for j in range(1, i):
                val = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(val)
            row.append(1)  # Each row ends with 1
            triangle.append(row)
        
        return triangle
