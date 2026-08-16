class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]

        for num in asteroids:
            destroyed=False
            while stack and num<0 and stack[-1]>0:
                if abs(stack[-1]) < abs(num):
                    stack.pop()
                elif abs(stack[-1]) == abs(num):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            if not destroyed:
                stack.append(num)
        return stack

    


        