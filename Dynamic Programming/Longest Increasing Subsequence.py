def bst(dp,val,low,high):
    mid=(low+high)//2
    if val==dp[mid] or val==dp[low] or val==dp[high-1]:
        return
    elif val<dp[mid] and val>dp[mid-1]:
        dp[mid]=val
        return
    elif val>dp[mid]:
        return bst(dp,val,mid+1,high)
    elif val<dp[mid]:
        return bst(dp,val,low,mid)


def lis(a):
    n=len(a)
    dp=[]
    dp.append(-1)
    dp.append(a[0])
    for i in range(1,n):
        if a[i]>dp[-1]:
            dp.append(a[i])
        else:
            bst(dp,a[i],0,len(dp))
    return len(dp)-1


a=[2,5,3,7,11,8,10,13,6]
out_=lis(a)

print(out_)
