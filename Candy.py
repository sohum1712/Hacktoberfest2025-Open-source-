class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candy = [1]*n
        #Left TO Right Traversal
        for i in range (1,n):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1

        #right to left traversal
        for i in range (n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)

        return sum(candy)
