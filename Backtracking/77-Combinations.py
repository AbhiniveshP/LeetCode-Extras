class Solution:

    def __backtrack(self, prevIndex: int, currentList: List[int],
                    finalList: List[List[int]], k: int, firstNInts: List[int]) -> None:

        if (len(currentList) == k):
            finalList.append(list(currentList))
            return

        for indexToAdd in range(prevIndex + 1, len(firstNInts)):
            currentList.append(firstNInts[indexToAdd])

            self.__backtrack(indexToAdd, currentList, finalList, k, firstNInts)

            currentList.pop()

        return

    def combine(self, n: int, k: int) -> List[List[int]]:

        if (n == 0 or k == 0):
            return []

        firstNInts = [i + 1 for i in range(n)]
        currentList = []
        finalList = []

        self.__backtrack(-1, currentList, finalList, k, firstNInts)

        return finalList