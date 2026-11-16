class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        while(len(s)>k):
            cnt=1
            ns=""
            sg=0
            for char in s:
                if cnt%k==0:
                    ns+=str(sg+int(char))
                    sg=0
                else:
                    sg+=int(char)
                cnt+=1
            if len(s)%k:ns+=str(sg)
            s=ns
        return s

