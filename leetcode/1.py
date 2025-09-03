class Solution:
    def twoSum(self,numbers:list[int],target:int)->list[int]:
        map_dict = {}
        for k,v in enumerate(numbers):
            if target-v in map_dict.keys():
                return [map_dict[target-v],k]
            map_dict[v] = k
        return []
            
             

s = Solution()
result = s.twoSum([2,7,3,6],9)
print(result)