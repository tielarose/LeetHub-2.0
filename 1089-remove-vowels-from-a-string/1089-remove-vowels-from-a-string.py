class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join([let for let in s if let not in set('aeiou')])
        