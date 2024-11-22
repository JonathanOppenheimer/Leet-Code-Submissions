class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n_nums = len(nums)
        answer = []
        xor_result = 0  # Initialize xor_result
        mask = (1 << maximumBit) - 1  # Create a mask with maximumBit ones

        for num in nums:
            xor_result ^= num  # Compute cumulative XOR

        for i in range(n_nums):
            complement = xor_result ^ mask
            answer.append(complement)
            xor_result ^= nums[n_nums - 1 - i]  # Remove the last element

        return answer
