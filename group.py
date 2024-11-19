#task 1
#function:
#input:
#output:
def groups_of_3(nums:list[int]) -> list[list[int]]:
    return [nums[i:i+3] for i in range(0, len(nums), 3)]

#task 2
