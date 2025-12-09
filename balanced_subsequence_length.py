def length(nums):
  if not nums:
    return 0;
  dp = [1]*len(nums)
  for i in range(len(nums)):
    for j in range(i):
      if nums[j] < nums[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return max(dp)
array = input("enter numbers: ")
arr = list(map(int,array.split()))
print("balanced increasing subsequences length:",length(arr))
