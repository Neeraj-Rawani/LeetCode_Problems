# 3970. Shortest Path With At Most K Consecutive Identical Characters

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

---

## Problem Description

<p>You are given an integer <code>n</code> representing the number of nodes in a <strong>directed weighted</strong> graph, numbered from 0 to <code>n - 1</code>. This is represented by a 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with weight <code>w<sub>i</sub></code>.</p>

<p>You are also given a string <code>labels</code> of length <code>n</code>, where <code>labels[i]</code> is the character assigned to node <code>i</code>, and an integer <code>k</code>.</p>

<p>Return the <strong>minimum</strong> <strong>total</strong> edge weight of a path from node 0 to node <code>n - 1</code> such that the concatenation of the labels of the nodes along the path contains <strong>at most</strong> <code>k</code> <strong>consecutive</strong> <strong>identical</strong> characters. If no valid path exists, return -1.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[2] = [0, 2, 3]</code> to reach node 2 with a weight <code>w<sub>i</sub> = 3</code>.</li>
</ul>
The corresponding concatenation of labels is <code>"ab"</code>, which satisfies at most <code>k = 1</code> consecutive identical characters. Thus, the answer is 3.</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal valid path from node 0 to node 2 is as follows:</p>

<ul>
	<li>Use <code>edges[0] = [0, 1, 1]</code> to reach node 1 with weight <code>w<sub>i</sub> = 1</code>.</li>
	<li>Use <code>edges[1] = [1, 2, 1]</code> to reach node 2 with weight <code>w<sub>i</sub> = 1</code>.</li>
</ul>
The corresponding concatenation of labels is <code>"aab"</code>, which satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is 2.</div>

<h3>Example 3</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no valid path from node 0 to node 2 that satisfies at most <code>k = 2</code> consecutive identical characters. Thus, the answer is -1.</p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= n == labels.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>0 <= edges.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
	<li><code>0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 <= w<sub>i</sub> <= 10<sup>4</sup></code></li>
	<li><code>labels</code> consists of lowercase English letters</li>
	<li><code>1 <= k <= 50</code></li>
</ul>

---

## Topics

- String
- Graph Theory
- Heap (Priority Queue)
- Shortest Path

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
