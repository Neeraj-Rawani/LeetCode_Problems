# 301. Remove Invalid Parentheses

**Difficulty:** Hard

**LeetCode:** [Open Problem](https://leetcode.com/problems/remove-invalid-parentheses/)

---

## Problem Description

<p>Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.</p>

<p>Return <em>a list of <strong>unique strings</strong> that are valid with the minimum number of removals</em>. You may return the answer in <strong>any order</strong>.</p>


<h3>Example 1</h3>

<pre>
<strong>Input:</strong> s = "()())()"
<strong>Output:</strong> ["(())()","()()()"]
</pre>

<h3>Example 2</h3>

<pre>
<strong>Input:</strong> s = "(a)())()"
<strong>Output:</strong> ["(a())()","(a)()()"]
</pre>

<h3>Example 3</h3>

<pre>
<strong>Input:</strong> s = ")("
<strong>Output:</strong> [""]
</pre>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= s.length <= 25</code></li>
	<li><code>s</code> consists of lowercase English letters and parentheses <code>'('</code> and <code>')'</code>.</li>
	<li>There will be at most <code>20</code> parentheses in <code>s</code>.</li>
</ul>

---

## Topics

- String
- Backtracking
- Breadth-First Search

---

## My Solution

**Language:** C++

[View Solution](./solution.cpp)

---
