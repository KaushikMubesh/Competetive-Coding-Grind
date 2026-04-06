price = [3,4,2,5,6,1]
maxi = -93128329
mini = 942012
for i in range(len(price)):
    mini=min(mini,price[i])
    maxi = max(maxi,price[i]-mini)
    print(mini,maxi)
print(maxi)