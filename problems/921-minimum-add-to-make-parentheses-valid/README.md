# 921. Minimum Add to Make Parentheses Valid

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

---

## Problem Description

<p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = "()))"</code>, you can insert an opening parenthesis to be <code>"(<strong>(</strong>)))"</code> or a closing parenthesis to be <code>"())<strong>)</strong>)"</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>


<h3>Example 1</h3>

<pre>
<strong>Input:</strong> s = "())"
<strong>Output:</strong> 1
</pre>

<h3>Example 2</h3>

<pre>
<strong>Input:</strong> s = "((("
<strong>Output:</strong> 3
</pre>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s[i]</code> is either <code>'('</code> or <code>')'</code>.</li>
</ul>

---

## Topics

- String
- Stack
- Greedy
- Bracket Sequences

---

## My Solution

**Language:** C++

[View Solution](./solution.cpp)

---
