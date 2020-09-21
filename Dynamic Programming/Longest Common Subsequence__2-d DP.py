def lcs(i,j,s1,s2,dp):
    if i>=len(s1) or j>=len(s2):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i]==s2[j]:
        return 1+lcs(i+1,j+1,s1,s2,dp)
    else:
        left=lcs(i+1,j,s1,s2,dp)
        right=lcs(i,j+1,s1,s2,dp)
        dp[i][j]=max(left,right)
        return max(left,right)


s1='abcwsd'
s2='cdge'
dp=[[-1]*len(s2)]*len(s1)
print(lcs(0,0,s1,s2,dp))
