class Solution(object):
    """
        Solución 1: uso un diccionario para almacenar los números y sus índices, complejidad temporal O(n) y espacial O(n).
        Solución 2: uso dos bucles anidados, comprobando todas las combinaciones posibles, complejidad temporal O(n^2) y espacial O(1).
    """
    
    def dos_sumas_con_diccionario(self, nums, objetivo):
        """   
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diccionario = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in diccionario:
                return [diccionario[complemento], i]
            diccionario[num] = i
        
        return []

    def dos_sumas_fuerza_bruta(self, nums, objetivo):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []