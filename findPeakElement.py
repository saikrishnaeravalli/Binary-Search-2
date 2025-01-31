# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            
            if ((mid == 0) or (nums[mid-1] < nums[mid])) and ((mid == len(nums)-1) or (nums[mid] > nums[mid+1])):
                return mid
            elif mid == len(nums)-1 or nums[mid] < nums[mid+1]:
                low = mid + 1
            elif mid == 0 or nums[mid-1] > nums[mid]:
                high = mid - 1