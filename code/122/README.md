## 我的Solution

[python](https://github.com/dym0080/leetcode/blob/master/code/122/122_best_time_to_buy_and_sell_stock_ii.py)

## 解题思路

使用双指针 `i`、`j`,只要找到 `prices[j] > prices[i]`马上进行在第 `i` 天买入，第 `j` 天卖出，直到 `j` 遍历完整个数组。