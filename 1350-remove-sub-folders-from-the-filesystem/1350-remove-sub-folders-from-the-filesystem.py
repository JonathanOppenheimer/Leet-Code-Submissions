class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n_folder = len(folder)
        folder = sorted(folder)
        seen = set()
        seen.add(folder[0])
        answer = []
        answer.append(folder[0])
        for i in range(1, n_folder):
            folder_so_far = ""
            folds = folder[i].split("/")
            print(folds)
            unique = True 
            for j in range(1, len(folds)): 
                print(folder_so_far)
                folder_so_far += "/" + folds[j]
                if folder_so_far in seen: 
                    unique = False
                    continue 
            if unique:
                seen.add(folder[i])
                answer.append(folder[i])

        return answer
