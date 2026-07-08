class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        if not s or not queries:
            return None
        m=len(queries)
        ans=[]
        MOD = 10**9 + 7
        ns=""
        for char in s:
            if char!='0':
                ns+=char
        if len(ns)==0:return [0]*len(queries)

        n=len(ns)

        p_s=[0]*(n+1)
        for i in range(n):
            p_s[i+1]+=p_s[i]+int(ns[i])
        

        p_c=[0]*(len(s)+1)

        for i in range(len(s)):
            if int(s[i])>=1:
                p_c[i+1]=p_c[i]+1
            else:
                p_c[i+1]=p_c[i]
        p_n=[0]*(n+1)
        
        for i in range(n):
            num=int(ns[i])
            p_n[i+1]=(p_n[i]*(10)+num)%MOD

        
        p_t=[1]*(n+1)
        for i in range(1,n+1):
            p_t[i]=(p_t[i-1]*10)%MOD

        
        for l,r in queries:
            cnt_l=p_c[l] 
            cnt_r=p_c[r+1]-1
            if cnt_l > cnt_r:
                ans.append(0)
                continue
            m=cnt_r-cnt_l+1
            t=p_s[cnt_r+1]-p_s[cnt_l]
            x=(p_n[cnt_r+1]-p_n[cnt_l]*p_t[m])
            if x<0:
                x=(x+MOD)%MOD
            else:
                x=x%MOD
            ans.append((x*t)%MOD)
        return ans



        




            
            


























