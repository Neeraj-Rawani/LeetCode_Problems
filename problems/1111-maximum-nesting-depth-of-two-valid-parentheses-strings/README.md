# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium

**LeetCode:** [Open Problem](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

---

## Problem Description

<p>A string is a <em>valid parentheses string</em> (denoted VPS) if and only if it consists of <code>"("</code> and <code>")"</code> characters only, and:</p>

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are VPS's, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a VPS.</li>
</ul>

<p>We can similarly define the <em>nesting depth</em> <code>depth(S)</code> of any VPS <code>S</code> as follows:</p>

<ul>
	<li><code>depth("") = 0</code></li>
	<li><code>depth(A + B) = max(depth(A), depth(B))</code>, where <code>A</code> and <code>B</code> are VPS's</li>
	<li><code>depth("(" + A + ")") = 1 + depth(A)</code>, where <code>A</code> is a VPS.</li>
</ul>

<p>For example, <code>""</code>, <code>"()()"</code>, and <code>"()(()())"</code> are VPS's (with nesting depths 0, 1, and 2), and <code>")("</code> and <code>"(()"</code> are not VPS's.</p>

<p>Given a VPS <font face="monospace">seq</font>, split it into two disjoint subsequences <code>A</code> and <code>B</code>, such that <code>A</code> and <code>B</code> are VPS's (and <code>A.length + B.length = seq.length</code>). The subsequences may not necessarily be contiguous.</p>

<p>For example, for the sequence <code>123456789</code>, one possible split is:</p>

<ul data-end="822" data-start="776">
	<li data-end="800" data-start="776">
	<p data-end="800" data-start="778"><code data-end="799" data-start="778">A = {1, 3, 5, 7, 9}</code>,</p>
	</li>
	<li data-end="822" data-start="801">
	<p data-end="822" data-start="803"><code data-end="821" data-start="803">B = {2, 4, 6, 8}</code>.</p>
	</li>
</ul>

<p data-end="855" data-start="824">This corresponds to the output <code>[0, 1, 0, 1, 0, 1, 0, 1, 0]</code>  where 0 indicates membership in <code data-end="929" data-start="926">A</code> and 1 indicates membership in <code data-end="965" data-start="962">B</code>.</p>

<p>Now choose <strong>any</strong> such <code>A</code> and <code>B</code> such that <code>max(depth(A), depth(B))</code> is the minimum possible value.</p>

<p>Return an <code>answer</code> array (of length <code>seq.length</code>) that encodes such a choice of <code>A</code> and <code>B</code>:  <code>answer[i] = 0</code> if <code>seq[i]</code> is part of <code>A</code>, else <code>answer[i] = 1</code>.  Note that even though multiple answers may exist, you may return any of them.</p>


<h3>Example 1</h3>

<pre>
<strong>Input:</strong> seq = "(()())"
<strong>Output:</strong> [0,1,1,1,1,0]
</pre>

<h3>Example 2</h3>

<pre>
<strong>Input:</strong> seq = "()(())()"
<strong>Output:</strong> [0,0,0,1,1,0,1,1]
</pre>


<h2>Constraints</h2>

<ul>
	<li><code>1 <= seq.size <= 10000</code></li>
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
