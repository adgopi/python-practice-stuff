from typing import List

def find_indices_of_sum_target_new(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    val_map = {}
    for i in range(n):
        if nums[i] in val_map:
            return [i, val_map[nums[i]]]
        val_map[target - nums[i]] = i


print(find_indices_of_sum_target_new([2,7,11,15], 9))
print(find_indices_of_sum_target_new([3,4], 6))
  
