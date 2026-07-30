class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        counter = 0
        result = []

        for i in range(len(temperatures)):
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    stack.append(temperatures[j])
                else:
                    result.append(j - i)
                    found = True
                    break
            if not found:
                result.append(0)
        return result