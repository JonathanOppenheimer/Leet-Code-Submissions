# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        answer = [n * [-1] for i in range(m)]    
        dx_dy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        i = 0
        x, y = 0, 0
        cur = head
        while cur != None:
            answer[y][x] = cur.val
            cur = cur.next 
            
            if (x + dx_dy[i][0] > n - 1) or (y + dx_dy[i][1] > m - 1) or (answer[y+dx_dy[i][1]][x+dx_dy[i][0]] != -1):
                 i = (i + 1) % 4
            
            x += dx_dy[i][0]
            y += dx_dy[i][1]
        
        return answer
            
            
                 
            


        