# 1254. Number of Closed Islands

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/number-of-closed-islands/)

---

## Problem Description

<p>Given a 2D <code>grid</code> consists of <code>0s</code> (land) and <code>1s</code> (water).  An <em>island</em> is a maximal 4-directionally connected group of <code><font face="monospace">0</font>s</code> and a <em>closed island</em> is an island <strong>totally</strong> (all left, top, right, bottom) surrounded by <code>1s.</code></p>

<p>Return the number of <em>closed islands</em>.</p>


<h3>Example 1</h3>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="width: 240px; height: 120px;" /></p>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
Islands in gray are closed because they are completely surrounded by water (group of 1s).</pre>

<h3>Example 2</h3>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png" style="width: 160px; height: 80px;" /></p>

<pre>
<strong>Input:</strong> grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
<strong>Output:</strong> 1
</pre>

<h3>Example 3</h3>

<pre>
<strong>Input:</strong> grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
<strong>Output:</strong> 2
</pre>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= grid.length, grid[0].length <= 100</code></li>
	<li><code>0 <= grid[i][j] <=1</code></li>
</ul>

---

## Topics

- Array
- Depth-First Search
- Breadth-First Search
- Union-Find
- Matrix

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
