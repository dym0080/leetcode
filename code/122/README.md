## 题目

[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) <br/> [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

## 我的Solution

[python](../122/122_best_time_to_buy_and_sell_stock_ii.py)

## 解题思路

使用双指针 `i`、`j`,只要找到 `prices[j] > prices[i]`马上进行在第 `i` 天买入，第 `j` 天卖出，直到 `j` 遍历完整个数组。