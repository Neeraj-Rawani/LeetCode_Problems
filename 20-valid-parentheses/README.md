# 20. Valid Parentheses

**Difficulty:** Easy

**LeetCode:** [Open Problem](https://leetcode.com/problems/valid-parentheses/)

---

## Problem Description

<p>Given a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>


<h3>Example 1</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "()"</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<h3>Example 2</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "()[]{}"</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<h3>Example 3</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "(]"</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<h3>Example 4</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "([])"</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<h3>Example 5</h3>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "([)]"</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= s.length <= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>'()[]{}'</code>.</li>
</ul>

---

## Topics

- String
- Stack
- Bracket Sequences

---

## My Solution

**Language:** C++

[View Solution](./solution.cpp)

---
