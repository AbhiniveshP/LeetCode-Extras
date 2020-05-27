class Solution:

    def __init__(self):
        self.digitCharsMap = {'0': '', '1': '', '2': 'abc', '3': 'def',
                              '4': 'ghi', '5': 'jkl', '6': 'mno',
                              '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def __backtrack(self, currIdx: int, digits: str, currStrList: List[str], finalList: List[str]) -> None:

        if (len(currStrList) == len(digits)):
            finalList.append(''.join(currStrList))
            return

        currDigit = digits[currIdx]

        for char in self.digitCharsMap[currDigit]:
            currStrList.append(char)

            self.__backtrack(currIdx + 1, digits, currStrList, finalList)

            currStrList.pop()

        return

    def letterCombinations(self, digits: str) -> List[str]:

        if (digits == None or len(digits) == 0):
            return []

        finalList = []
        currStrList = []

        self.__backtrack(0, digits, currStrList, finalList)

        return finalList