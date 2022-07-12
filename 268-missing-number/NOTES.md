
1. #### Gaus Formula


We can find the sum of first `n` numbers using [Gaus formula](https://nrich.maths.org/2478).

```
(n * (n+1))/2 where `n` is the length of input `nums`.
```

Then just subtract this with the sum of input `nums` to find the missing number.

```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1))//2 - sum(nums)
```


2. #### Bit Manipulation

In this approach, we will concat the input `nums` with the sequence of numbers from `[0, n]`. Then we would perform the reduce operation using an `xor` operator. The `xor` operation cancels the same elements in the list. So after the reduce operation, we would be left only with the missing number.

```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, list(range(len(nums)+1)) + nums)
```

**Time - O(n)
Space - O(1)**
