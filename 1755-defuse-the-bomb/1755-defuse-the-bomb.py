class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_n = len(code)

        def get_k(i, k): 
            run_sum = 0
            
            if k < 0:
                i-=1 
                count = abs(k)
                while count > 0:
                    if i == -1: 
                        i = code_n - 1
                    run_sum += code[i]
                    count -= 1
                    i -= 1
            
            if k > 0:
                i+=1 
                while k > 0: 
                    if i == code_n:
                        i = 0 
                    run_sum += code[i]
                    k -= 1
                    i += 1

            return run_sum


        new_arr = []
        if k == 0:
            new_arr = [0] * code_n
            return new_arr

        for i in range(code_n):
            new_arr.append(get_k(i,k))

        return new_arr