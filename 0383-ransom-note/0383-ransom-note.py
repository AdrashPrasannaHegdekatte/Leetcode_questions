class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r=Counter(ransomNote)
        m=Counter(magazine)
        for char, freq in r.items():
            if m[char] < freq:
                return False
        return True