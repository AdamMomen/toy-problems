/*
Input: [7,1,5,3,6,4]
Output: 7
Explanation:
	 Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.

	Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


- window traversal

	min = 7, 1, 1, 1, 1 | 1 1 3 4 4 | 
	max = 7 7 7 7 7 7 7 | 7 6 6 6 4
	diff= k 
*/
class Solution {
	static maxProfit(prices = []){
		let maxprofit = 0
		for(let i =1; i < prices.length; i++){
			if(prices[i] > prices[i - 1]){
				maxprofit += prices[i] prices[i -1]
			}
		}
	}
	return maxprofit
}
let input = [7,1,5,3,6,4]

console.log(
Solution.maxProfit(input)
)
