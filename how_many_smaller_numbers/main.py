def how_many_smaller_numbers(nums):
    result = []
    for i in range(len(nums)):
        others = nums[:i] + nums[i+1:]
        less_than = list(filter(lambda x: x < nums[i], others))
        result.append(len(less_than))
    return result
