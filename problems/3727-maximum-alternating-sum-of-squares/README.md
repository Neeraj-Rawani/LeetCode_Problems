# 3727. Maximum Alternating Sum of Squares

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

---

## Problem Description

<p>You are given an integer array <code>nums</code>. You may <strong>rearrange the elements</strong> in any order.</p>

<p>The <strong>alternating score</strong> of an array <code>arr</code> is defined as:</p>

<ul>
	<li><code>score = arr[0]<sup>2</sup> - arr[1]<sup>2</sup> + arr[2]<sup>2</sup> - arr[3]<sup>2</sup> + ...</code></li>
</ul>

<p>Return an integer denoting the <strong>maximum possible alternating score</strong> of <code>nums</code> after rearranging its elements.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>A possible rearrangement for <code>nums</code> is <code>[2,1,3]</code>, which gives the maximum alternating score among all possible rearrangements.</p>

<p>The alternating score is calculated as:</p>

<p><code>score = 2<sup>2</sup> - 1<sup>2</sup> + 3<sup>2</sup> = 4 - 1 + 9 = 12</code></p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-1,2,-2,3,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>A possible rearrangement for <code>nums</code> is <code>[-3,-1,-2,1,3,2]</code>, which gives the maximum alternating score among all possible rearrangements.</p>

<p>The alternating score is calculated as:</p>

<p><code>score = (-3)<sup>2</sup> - (-1)<sup>2</sup> + (-2)<sup>2</sup> - (1)<sup>2</sup> + (3)<sup>2</sup> - (2)<sup>2</sup> = 9 - 1 + 4 - 1 + 9 - 4 = 16</code></p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-4 * 10<sup>4</sup> <= nums[i] <= 4 * 10<sup>4</sup></code></li>
</ul>

---

## Topics

- Array
- Greedy
- Sorting

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
