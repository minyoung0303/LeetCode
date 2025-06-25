import bisect,math

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        def Check(mid):
            n = len(nums1)
            m = len(nums2)

            count = 0
            for n in nums1:
                
                # Binary search depending on the sign of number
                if n > 0:
                    count += bisect.bisect_right(nums2,mid//n)
                elif n == 0:
                    count += m if mid>=0 else 0
                else:       
                    v = mid//n
                    if mid%n!=0:v+=1
                    count += (m - bisect.bisect_left(nums2,v))
          
            return count>=k
        
    
        l = -10**10
        r = 10**10

        while l<r:
            mid = l + (r-l)//2

            if Check(mid):
                r = mid
            else:
                l = mid+1
        
        return r
