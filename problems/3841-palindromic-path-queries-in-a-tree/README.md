# 3841. Palindromic Path Queries in a Tree

**Difficulty:** Hard

**LeetCode:** [Open Problem](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

---

## Problem Description

<p>You are given an undirected tree with <code>n</code> nodes labeled 0 to <code>n - 1</code>. This is represented by a 2D array <code>edges</code> of length <code>n - 1</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates an undirected edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>You are also given a string <code>s</code> of length <code>n</code> consisting of lowercase English letters, where <code>s[i]</code> represents the character assigned to node <code>i</code>.</p>

<p>You are also given a string array <code>queries</code>, where each <code>queries[i]</code> is either:</p>

<ul>
	<li><code>"update u<sub>i</sub> c"</code>: Change the character at node <code>u<sub>i</sub></code> to <code>c</code>. Formally, update <code>s[u<sub>i</sub>] = c</code>.</li>
	<li><code>"query u<sub>i</sub> v<sub>i</sub>"</code>: Determine whether the string formed by the characters on the <strong>unique</strong> path from <code>u<sub>i</sub></code> to <code>v<sub>i</sub></code> (inclusive) can be <strong>rearranged</strong> into a <strong><span data-keyword="palindrome-string">palindrome</span></strong>.</li>
</ul>

<p>Return a boolean array <code>answer</code>, where <code>answer[j]</code> is <code>true</code> if the <code>j<sup>th</sup></code> query of type <code>"query u<sub>i</sub> v<sub>i</sub>"​​​​​​​</code> can be rearranged into a <strong>palindrome</strong>, and <code>false</code> otherwise.</p>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]</span></p>

<p><strong>Output:</strong> <span class="example-io">[true,false]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>"query 0 2"</code>: Path <code>0 → 1 → 2</code> gives <code>"aac"</code>, which can be rearranged to form <code>"aca"</code>, a palindrome. Thus, <code>answer[0] = true</code>.</li>
	<li><code>"update 1 b"</code>: Update node 1 to <code>'b'</code>, now <code>s = "abc"</code>.</li>
	<li><code>"query 0 2"</code>: Path characters are <code>"abc"</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[1] = false</code>.</li>
</ul>

<p>Thus, <code>answer = [true, false]</code>.</p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false,false,true]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>"query 1 2"</code>: Path <code>1 → 0 → 2</code> gives <code>"bac"</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[0] = false</code>.</li>
	<li><code>"update 0 b"</code>: Update node 0 to <code>'b'</code>, now <code>s = "bbca"</code>.</li>
	<li><code>"query 2 3"</code>: Path <code>2 → 0 → 3</code> gives <code>"cba"</code>, which cannot be rearranged to form a palindrome. Thus, <code>answer[1] = false</code>.</li>
	<li><code>"update 3 a"</code>: Update node 3 to <code>'a'</code>, <code>s = "bbca"</code>.</li>
	<li><code>"query 1 3"</code>: Path <code>1 → 0 → 3</code> gives <code>"bba"</code>, which can be rearranged to form <code>"bab"</code>, a palindrome. Thus, <code>answer[2] = true</code>.</li>
</ul>

<p>Thus, <code>answer = [false, false, true]</code>.</p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= n == s.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li>The input is generated such that <code>edges</code> represents a valid tree.</li>
	<li><code>1 <= queries.length <= 5 * 10<sup>4</sup></code>​​​​​​​
	<ul>
		<li><code>queries[i] = "update u<sub>i</sub> c"</code> or</li>
		<li><code>queries[i] = "query u<sub>i</sub> v<sub>i</sub>"</code></li>
		<li><code>0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1</code></li>
		<li><code>c</code> is a lowercase English letter.</li>
	</ul>
	</li>
</ul>

---

## Topics

- Array
- String
- Divide and Conquer
- Bit Manipulation
- Tree
- Depth-First Search
- Binary Indexed Tree
- Segment Tree

---

## My Solution

- **C++:** [View Solution](./solution.cpp)

---
