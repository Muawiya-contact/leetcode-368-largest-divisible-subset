# LeetCode 368: Largest Divisible Subset

This repository contains a Python solution to LeetCode Problem **368 - Largest Divisible Subset**.

---

## 🔢 Problem Statement

Given a set of **distinct positive integers** `nums`, return the **largest subset** `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

- `answer[i] % answer[j] == 0`, or  
- `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them.

---

## 📥 Example Inputs and Outputs

### ✅ Example 1:
#### Input: nums = [1, 2, 3] 
#### Output: [1, 2] 
#### Explanation: [1, 3] is also accepted.

### ✅ Example 2:
#### Input: nums = [1, 2, 4, 8] 
#### Output: [1, 2, 4, 8]

---

## ⚙️ Constraints

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 10^9`
- All the integers in `nums` are **unique**

---

## 🧠 Approach

This problem is solved using **Dynamic Programming**:

1. **Sort the array** to ensure proper divisibility order.
2. Use a `dp[]` array to keep track of the size of the largest divisible subset ending at each index.
3. Use a `prev[]` array to remember the **previous index** of the number in the subset chain.
4. Reconstruct the subset by backtracking from the largest value found.

Time Complexity: `O(n^2)`  
Space Complexity: `O(n)`

---

## 🧾 File Structure

leetcode-368-largest-divisible-subset
# README.md 
# main.py
# Python code with comments

---

## 📌 Tags

- #DynamicProgramming
- #Subsets
- #Greedy
- #Math
- #Medium

---

## 🔗 LeetCode Link

👉 [LeetCode Problem 368 - Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)



### 💡 Feel free to star ⭐ the repo if you find it helpful!

---

