from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for num in nums:
            dd[num] += 1
        vals = sorted(dd, key=lambda x: dd[x])
        vals.reverse()

        answer = []
        for i in range(k):
            answer.append(vals[i])

        return answer 