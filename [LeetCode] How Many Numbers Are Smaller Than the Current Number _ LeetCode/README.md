# How Many Numbers Are Smaller Than the Current Number - LeetCode

### Difficulty: Medium

## Description

Problem List
Debugging...
Submit
0
00:00:00
AbhayVarshith_Aripirala
Access all features with our Premium subscription!
My Lists
Favorites
Notebook
Progress
Points
Try New Features
Orders
My Playgrounds
Settings
Appearance
Sign Out
Premium
Description
Description
Editorial
Editorial
Solutions
Solutions
Submissions
Code
Testcase
Testcase
Test Result
Status
Language
Runtime
Memory
Notes
7
Accepted
2 minutes ago
Python3
185 ms
19 MB
6
Accepted
Apr 24, 2026
Python
124 ms
12.3 MB
5
Compile Error
Dec 20, 2025
C++
N/A
N/A
4
Accepted
Dec 08, 2025
C++
15 ms
14 MB
3
Accepted
Dec 08, 2025
C++
14 ms
14 MB
2
Accepted
Dec 08, 2025
C++
15 ms
14.1 MB
1
Accepted
Dec 08, 2025
C++
16 ms
14 MB
Python3
Auto
1
2
3
4
5
6
7
8
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1
Restored from local
Upgrade to Cloud Saving
Ln 1, Col 1
You must run your code first

Pushing...

---
**Company Tags**: None
**Topic Tags**: None

## Test Cases

```
Test cases not found.
```