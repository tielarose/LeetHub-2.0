from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        return Counter(count1.values()) == Counter(count2.values())
