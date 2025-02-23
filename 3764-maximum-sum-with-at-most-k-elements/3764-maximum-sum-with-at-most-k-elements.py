class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        # grid, limits, k

        n, m=len(grid), len(grid[0])
        lst=[]
        for i in range(n): 
            if not limits[i]==0:
                for num in sorted(grid[i])[-limits[i]:]:
                    lst.append(num)
            
        return sum(sorted(lst)[-k:]) if k!=0 else 0

        
        