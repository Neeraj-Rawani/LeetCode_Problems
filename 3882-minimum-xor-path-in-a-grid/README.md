# 3882. Minimum XOR Path in a Grid

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)

---

## Problem Description

<p>You are given a 2D integer array <code>grid</code> of size <code>m * n</code>.</p>

<p>You start at the <strong>top-left</strong> cell <code>(0, 0)</code> and want to reach the <strong>bottom-right</strong> cell <code>(m - 1, n - 1)</code>.</p>

<p>At each step, you <strong>may</strong> move either <strong>right or down</strong>.</p>

<p>The <strong>cost</strong> of a path is defined as the <strong>bitwise XOR</strong> of all the values in the cells along that path, <strong>including</strong> the start and end cells.</p>

<p>Return the <strong>minimum</strong> possible XOR value among all valid paths from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two valid paths:</p>

<ul>
	<li><code>(0, 0) → (0, 1) → (1, 1)</code> with XOR: <code>1 XOR 2 XOR 4 = 7</code></li>
	<li><code>(0, 0) → (1, 0) → (1, 1)</code> with XOR: <code>1 XOR 3 XOR 4 = 6</code></li>
</ul>

<p>The minimum XOR value among all valid paths is 6.</p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[6,7],[5,8]]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two valid paths:</p>

<ul>
	<li><code>(0, 0) → (0, 1) → (1, 1)</code> with XOR: <code>6 XOR 7 XOR 8 = 9</code></li>
	<li><code>(0, 0) → (1, 0) → (1, 1)</code> with XOR: <code>6 XOR 5 XOR 8 = 11</code></li>
</ul>

<p>The minimum XOR value among all valid paths is 9.</p>
</div>

<h3>Example 3</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[2,7,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one valid path:</p>

<ul>
	<li><code>(0, 0) → (0, 1) → (0, 2)</code> with XOR: <code>2 XOR 7 XOR 5 = 0</code></li>
</ul>

<p>The XOR value of this path is 0, which is the minimum possible.</p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= m == grid.length <= 1000</code></li>
	<li><code>1 <= n == grid[i].length <= 1000</code></li>
	<li><code>m * n <= 1000</code></li>
	<li><code>0 <= grid[i][j] <= 1023​</code></li>
</ul>

---

## Topics

- Array
- Dynamic Programming
- Bit Manipulation
- Matrix

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
