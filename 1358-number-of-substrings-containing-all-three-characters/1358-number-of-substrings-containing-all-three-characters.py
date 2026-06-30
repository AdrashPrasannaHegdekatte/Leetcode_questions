class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        seen={"a":-1, "b":-1, "c":-1}
        for i in range(len(s)):
            seen[s[i]]=i
            if seen["a"]==-1 or seen["b"]==-1 or  seen["c"]==-1:
                continue
            else:
                min_index=min(seen["a"] ,  seen["b"], seen["c"])
                ans += min_index + 1
        return ans

                

        