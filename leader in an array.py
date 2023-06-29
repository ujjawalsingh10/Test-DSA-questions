class findLeader:
    def leader(self, arr):
        sortLeader = []
        for i in range(len(arr)):
            j = i + 1
            while j < len(arr):
                if arr[i] < arr[j]:
                    break
                j = j + 1
            
            if j == len(arr):
                sortLeader.append(arr[i])
        return sortLeader

myObj = findLeader()
print(myObj.leader([7, 10, 4, 10, 6, 5, 2]))