# 3963. Create Grid With Exactly One Path

**Difficulty:** Easy

**LeetCode:** [Open Problem](https://leetcode.com/problems/create-grid-with-exactly-one-path/)

---

## Problem Description

<p>You are given two integers <code>m</code> and <code>n</code>, representing the number of rows and columns of a grid.</p>

<p>Construct <strong>any</strong> <code>m x n</code> grid consisting only of the characters <code>'.'</code> and <code>'#'</code>, where:</p>

<ul>
	<li><code>'.'</code> represents a free cell.</li>
	<li><code>'#'</code> represents an obstacle cell.</li>
</ul>

<p>A <strong>valid path</strong> is a sequence of free cells that:</p>

<ul>
	<li>Starts at the top-left cell <code>(0, 0)</code>.</li>
	<li>Ends at the bottom-right cell <code>(m - 1, n - 1)</code>.</li>
	<li>Moves only:
	<ul>
		<li>Right, from <code>(i, j)</code> to <code>(i, j + 1)</code>, or</li>
		<li>Down, from <code>(i, j)</code> to <code>(i + 1, j)</code>.</li>
	</ul>
	</li>
</ul>

<p>Return any grid such that there is <strong>exactly one valid path</strong> from the top-left cell to the bottom-right cell.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 2, n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">["..#","#.."]</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61005pm.png" style="width: 200px; height: 95px;" /></p>

<p>The only valid path is: <code>(0,0) → (0,1) → (1,1) → (1,2)</code></p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 3, n = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">["..#","#..","##."]</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2026/05/26/screenshot-2026-05-26-at-61129pm.png" style="width: 220px; height: 150px;" /></p>

<p>The only valid path is: <code>(0,0) → (0,1) → (1,1) → (1,2) → (2,2)</code></p>
</div>

<h3>Example 3</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">m = 1, n = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">["...."]</span></p>

<p><strong>Explanation:</strong></p>

<p>The only valid path is: <code>(0,0) → (0,1) → (0,2) → (0,3)</code></p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= m, n <= 25</code></li>
</ul>

---

## Topics

- Not available

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
