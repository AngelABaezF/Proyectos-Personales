class Solution(object):
    """
        Solución 1: uso dos variables para mantener el máximo dinero robado hasta la casa anterior y la casa actual, complejidad temporal O(n) y espacial O(1).
        Solución 2: uso una lista para almacenar los resultados parciales de la máxima cantidad robada hasta cada casa, complejidad temporal O(n) y espacial O(n).
    """
    
    def robar_con_dos_variables(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        max_anterior = 0
        max_actual = 0
        
        for num in nums:
            temp = max_actual
            max_actual = max(max_anterior + num, max_actual)
            max_anterior = temp
        
        return max_actual

    def robar_con_lista(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
