class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0

        while start < len(s) - 2:
            if s[start] == s[start + 1] and s[start] == s[start + 2]:
                end = start + 2
                while end < len(s) and s[start] == s[end]:
                    end += 1
                interval = [start, end - 1]
                result.append(interval)
                start = end
            else:
                start += 1

        return result
        