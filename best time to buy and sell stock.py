class Stocks():
    def maximumProfit(self, prices):
        minimumValue = 200
        maximumDiff = 0
        for i in range(len(prices)):
            minimumValue = min(prices[i], minimumValue)
            maximumDiff = max(prices[i]-minimumValue, maximumDiff)
            
        return maximumDiff

myObj = Stocks()
print(myObj.maximumProfit([7,6,4,3,1]))
print(myObj.maximumProfit( [7,1,5,3,6,4]))