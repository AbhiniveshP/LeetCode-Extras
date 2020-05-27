class Solution:

    def __backtrack(self, currentList: List[int], currentSet: set,
                    finalList: List[List[int]], nums: List[int]) -> None:

        if (len(currentList) == len(nums)):
            finalList.append(list(currentList))
            return

        for i in range(len(nums)):

            if (nums[i] in currentSet):
                continue

            currentList.append(nums[i])
            currentSet.add(nums[i])

            self.__backtrack(currentList, currentSet, finalList, nums)

            currentList.pop()
            currentSet.remove(nums[i])

        return

    def permute(self, nums: List[int]) -> List[List[int]]:

        if (nums == None or len(nums) == 0):
            return []

        finalList = []
        currentList = []
        currentSet = set()

        self.__backtrack(currentList, currentSet, finalList, nums)

        return finalList