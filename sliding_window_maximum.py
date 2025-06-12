import collections # You'd need this for deque, assuming it's imported elsewhere or provided.
# from typing import List # For type hinting, good practice.

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 1. Initialization
        output = []          # This list will store the maximums of each sliding window.
        q = collections.deque() # This is our double-ended queue. It will store INDICES of numbers from `nums`.
                             # It's kept "monotonic decreasing" meaning nums[q[0]] > nums[q[1]] > ...
        l = r = 0            # l: left pointer of the window, r: right pointer of the window. Both start at the beginning.

        # 2. Main Loop: Iterate through the array with the right pointer `r`
        while r < len(nums):
            # `r` is the index of the current element we are considering to add to our window.
            # `nums[r]` is the value of that element.

            # 2a. Maintain Monotonic Decreasing Deque (from the right)
            # Before adding the current element's index `r` to the deque,
            # remove any elements from the *right* end of the deque whose values
            # are smaller than the current element `nums[r]`.
            # Why? If nums[q[-1]] < nums[r], then nums[q[-1]] can never be the maximum
            # in any window that also includes nums[r] (because nums[r] is to its right AND larger).
            # So, nums[q[-1]] is no longer a useful candidate.
            while q and nums[q[-1]] < nums[r]:
                q.pop() # Removes the last element (index) from the deque.

            # 2b. Add Current Element's Index to Deque
            # After the above loop, q is either empty, or nums[q[-1]] >= nums[r].
            # Now, add the index `r` of the current element to the right end of the deque.
            q.append(r)

            # 2c. Remove Out-of-Window Elements (from the left)
            # The element at the *left* end of the deque (q[0]) is the oldest element
            # (in terms of its position in `nums`) among the candidates in the deque.
            # If this oldest element's index `q[0]` is no longer within the current
            # window [l, r] (i.e., q[0] < l), it means it has slid out of view.
            if l > q[0]: # This means the element at index q[0] is to the left of our current window's start.
                q.popleft() # Remove it from the left end of the deque.

            # 2d. Check if Window is Formed and Record Maximum
            # A window of size `k` is formed when `r` has moved `k-1` steps from the start (0-indexed).
            # So, `r + 1` gives the number of elements considered so far for the window.
            # When `r + 1 >= k`, the window [l, r] has at least `k` elements.
            # (e.g., if k=3:
            #  r=0: window size 1
            #  r=1: window size 2
            #  r=2: window size 3. Here r+1 = 3, which is >= k. First full window is nums[0..2])
            if (r + 1) >= k:
                # The element at `nums[q[0]]` is the maximum for the current window [l, r].
                # Why?
                # 1. All elements to the left of q[0] that were smaller have been popped.
                # 2. All elements whose indices are in q are within the current window [l,r] (due to 2c).
                # 3. The values nums[q[i]] are in decreasing order, so nums[q[0]] is the largest.
                output.append(nums[q[0]])
                l += 1 # Slide the window: move the left pointer one step to the right.
                       # This prepares for the next iteration where `r` will also move right.

            # 2e. Advance Right Pointer
            r += 1 # Move the right pointer to consider the next element in `nums`.

        # 3. Return Result
        return output