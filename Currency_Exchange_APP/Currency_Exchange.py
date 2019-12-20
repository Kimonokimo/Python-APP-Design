# Python and Applications to Business Analytics Fall 2018, Module 1
# Assignment2
# Author: Ran Dou, Qimo Li


# We chose a new method rather than Dijkstra’s Algorithm to realize the expexted computation.
currency = ['CAD', 'EUR', 'CNY', 'GBP','JPY']
# Current FX rates between the following five currencies and the US dollar.
# In the order of EUR, CAD, CNY, JPY, GBP
ERsell = [1.29808, 113.53, 6.87990, 0.76624, 0.86103]
ERbuy = [1.29773,113.52, 6.87543, 0.76609, 0.86089]
# three option for the fluctuation of the Foreign exchange rate
FXrate = [0.01, 0.02, 0.05]

# define arbitrage function
def arbitrage(bidrate, askrate):
    results = {}  #show the result of the function
    for i in range(len(currency)):
        start = currency[i]  #start with the first currency in the currency list above
        usd = ERsell[i]*(1-bidrate)  #convert it into the amount of US dollar
        max = 0.8
        max_foreign_c = ''  #set the initial value for max_foreign_c
        for j in range(len(currency)):   # exchange through currency j (another currency in the list)
            foreign_c = currency[j]  #assign the chosen currency to foreign_c
            final_amount = usd / ERbuy[j] * (1 + askrate) * ERsell[j] * (1 - bidrate) / ERbuy[i] * (1 + askrate)  #compute the overall price
            if final_amount > max:  #make comparison between the pre-set amount
                max = final_amount  #if the computed amount is larger than the pre-set amount, set it as the new max
                max_foreign_c = foreign_c  #change the the currency name in the further print list
        results[start] = {max_foreign_c: max}  #update results
    return results

for bidrate in FXrate:  #print the chosen ask and bid rate
    for askrate in FXrate:
        print("bid: " + str(bidrate) + " ask: " + str(askrate))
        print(arbitrage(bidrate,askrate))
        print("")