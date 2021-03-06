# 动态规划
动态规划常常适用于有重叠子问题和最优子结构性质的问题，动态规划方法所耗时间往往远少于朴素解法。

广泛应用于许多组合优化的算法设计中，比如背包问题、最长公共子序列问题、Viterbi算法、矩阵链的乘法问题、最大子段和问题、多起点与多终点的最短路径问题、最大效益投资问题

动态规划只能应用于有最优子结构的问题。最优子结构的意思是局部最优解能决定全局最优解 (对有些问题这个要求并不能完全满足，故有时需要引入一定的近似)。简单地说，问题能够分解成子问题来解决。

## 适用条件
1. 最优子结构性质。如果问题的最优解所包含的子问题的解也是最优的，我们就称该问题具有最优子结构性质（即满足最优化原理）。最优子结构性质为动态规划算法解决问题提供了重要线索。

2. 无后效性。即子问题的解一旦确定，就不再改变，不受在这之后、包含它的更大的问题的求解决策影响。

3. 子问题重叠性质。子问题重叠性质是指在用递归算法自顶向下对问题进行求解时，每次产生的子问题并不总是新问题，有些子问题会被重复计算多次。动态规划算法正是利用了这种子问题的重叠性质，对每一个子问题只计算一次，然后将其计算结果保存在一个表格中，当再次需要计算已经计算过的子问题时，只是在表格中简单地查看一下结果，从而获得较高的效率。

## 算法设计
1. 子问题划分
2. 递推方程

包含3个实例：
1. 矩阵链乘法
2. 最长公共子序列
3. Viterbi算法

## 矩阵链乘法

所谓矩阵链乘法是指当一些矩阵相乘时，如何加括号来改变乘法顺序从而来降低乘法次数。

例如有三个矩阵连乘：A1\*A2\*A3，其维数分别为：10\*100，100\*5，5\*50.如果按照（（A1\*A2）\*A3）来计算的话，求（A1\*A2）要10\*100\*5=5000次乘法，再乘以A3需要10\*5\*50=2500次乘法，因此总共需要7500次乘法。

如果按照（A1\*（A2\*A3））来计算的话，求（A2\*A3）要100\*5\*50=25000次乘法，再乘以A1需要10\*100\*50=50000次乘法，因此总共需要75000次乘法。可见，按不同的顺序计算，代价相差很大。

## 最长公共子序列

最长公共子序列（LCS）是一个在一个序列集合中（通常为两个序列）用来查找所有序列中最长子序列的问题。这与查找最长公共子串的问题不同的地方是：子序列不需要在原序列中占用连续的位置。

最长公共子序列问题是一个经典的计算机科学问题，也是数据比较程序，比如Diff工具，和生物信息学应用的基础。它也被广泛地应用在版本控制，比如Git用来调和文件之间的改变。

对于一般性的LCS问题（即任意数量的序列）是属于NP-hard。但当序列的数量确定时，问题可以使用动态规划（Dynamic Programming）在多项式时间内解决。

### 问题分析
最长公共子序列问题存在最优子结构：这个问题可以分解成更小，更简单的“子问题”，这个子问题可以分成更多的子问题，因此整个问题就变得简单了。最长公共子序列问题的子问题的解是可以重复使用的，也就是说，更高级别的子问题通常会重用低级子问题的解。拥有这个两个属性的问题可以使用动态规划算法来解决，这样子问题的解就可以被储存起来，而不用重复计算。这个过程需要在一个表中储存同一级别的子问题的解，因此这个解可以被更高级的子问题使用。

## Viterbi算法
本例参考Wikipedia: https://zh.wikipedia.org/wiki/%E7%BB%B4%E7%89%B9%E6%AF%94%E7%AE%97%E6%B3%95