# 3942. Minimum Operations to Sort a Permutation

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)

---

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a <span data-keyword="permutation-array">permutation</span> of the integers from 0 to <code>n - 1</code>.</p>

<p>You may perform <strong>only</strong> the following operations:</p>

<ul>
	<li><strong>Reverse</strong> the entire array.</li>
	<li><strong>Rotate Left by One</strong>: Move the first element to the end of the array, and rest elements to left by one position.</li>
</ul>

<p>Return an integer denoting the <strong>minimum</strong> number of operations required to sort the array in <strong>increasing</strong> order. If it is <strong>not possible</strong> to sort the array using only the given operations, return -1.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Rotate Left by one: <code>[2, 1, 0]</code></li>
	<li>Reverse the array: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal</p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Reverse the array: <code>[2, 0, 1]</code></li>
	<li>Rotate Left by one: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal.</p>
</div>

<h3>Example 3</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>It is impossible to reach <code>[2, 0, 1, 3]</code>. Thus, the answer is -1.</p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= n == nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= n - 1</code></li>
	<li><code>nums</code> is a permutation of integers from 0 to <code>n - 1</code>.</li>
</ul>

---

## Topics

- Array

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
