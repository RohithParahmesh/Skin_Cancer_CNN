def xor_total_sum(nums):
    def helper(nums, index, xor_sum):
        if index == len(nums):
            return xor_sum
        return helper(nums, index + 1, xor_sum) + helper(nums, index + 1, xor_sum ^ nums[index])
    
    return helper(nums, 0, 0)

if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements of the array, separated by spaces: ").strip().split()))
    result = xor_total_sum(nums)
    print("The sum of all XOR totals for every subset of the array is:", result)
