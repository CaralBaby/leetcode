def BinarySearch(nums, middle):
    i = len(nums) - 1
    while True:
        if nums[i] == middle:
            return i + 1
        elif i < len(nums) - 1 and nums[i] < middle and nums[i + 1] > middle:
            return i + 1
        elif i == len(nums) - 1 and nums[i] < middle:
            return i + 1
        elif i == 0:
            return i
        else:
            i = i // 2


class Solution(object):
    def findMedianSortedArrays0(self, nums1, nums2, k):
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        print(nums1)
        print(nums2)
        print(l1)
        print(l2)
        print(k)
        if l1 == 0:
            return 0.5 * (nums2[k - 1] + nums2[k]) if not self.is_odd else nums2[k]
        elif l2 == 0:
            return 0.5 * (nums1[k - 1] + nums1[k]) if not self.is_odd else nums1[k]
        elif l1 + l2 == k:
            if k == 2 and not self.is_odd:
                return (nums1[0] + nums2[0]) / 2
            return max(nums1[-1], nums2[-1])
        elif l1 == 1 and l2 == 1:
            if self.is_odd:
                return min(nums1[0], nums2[0]) if k == 0 else max(nums1[0], nums2[0])
            else:
                return (nums1[0] + nums2[0]) / 2.0
        elif l1 == 2 and l2 == 2:
            sorted_list = sorted([nums1[0], nums1[1], nums2[0], nums2[1]])
            return (sorted_list[k] + sorted_list[k - 1]) * 0.5 if not self.is_odd else sorted_list[k]
        elif l1 + l2 <= 4:
            nums1.extend(nums2)
            sorted_list = sorted(nums1)
            return (sorted_list[k] + sorted_list[k - 1]) * 0.5 if not self.is_odd else sorted_list[k]
        else:
            middle1 = 0.5 * (nums1[l1 // 2] + nums1[(l1 - 1) // 2])
            middle2 = 0.5 * (nums2[l2 // 2] + nums2[(l2 - 1) // 2])
            print(middle1, middle2)
            if l1 > l2:
                n2 = BinarySearch(nums2, middle1)
                print("n2:", n2)
                if n2 > l2 - n2:
                    if l1 / 2 + n2 < k or (n2 + (l1 + 1) // 2 < k - 1 and not self.is_odd):
                        return self.findMedianSortedArrays0(nums1[l1 // 2:], nums2[n2:], k - l1 // 2 - n2)
                    else:
                        print("here1")
                        return self.findMedianSortedArrays0(nums1[0:(l1 + 1) // 2], nums2[0:n2], k)
                elif n2 <= l2 - n2:
                    if l1 // 2 + n2 > k or (n2 + l1 // 2 > k - 1 and not self.is_odd):
                        return self.findMedianSortedArrays0(nums1[0:(l1 + 1) // 2], nums2[0:n2 + 1], k)
                    else:
                        return self.findMedianSortedArrays0(nums1[l1 // 2:], nums2[n2:],
                                                     k - l1 // 2 - n2)
                elif n2 == l2 - n2:
                    sorted_list = sorted([nums2[n2], nums2[n2 - 1], nums1[l1 // 2], nums1[(l1 - 1) // 2]])
                    middle1 = 0.5 * (sorted_list[1] + sorted_list[2])
                    if l1 // 2 is not (l1 - 1) // 2:
                        return middle1
                    else:
                        if n2 + l1 // 2 >= k:
                            middle2 = nums2[n2 - 1] if nums2[n2 - 1] > nums1[l1 // 2 - 1] else nums1[l1 // 2 - 1]
                        else:
                            middle2 = nums2[n2] if nums2[n2] < nums1[l1 // 2 + 1] else nums1[l1 // 2 + 1]
                        return 0.5 * (middle1 + middle2)
            elif l1 <= l2:
                n1 = BinarySearch(nums1, middle2)
                print("n1:", n1)
                if n1 > l1 - n1:
                    print("wo")
                    if n1 + (l2 + 1) // 2 < k or (n1 + (l2 + 1) // 2 < k + 1 and not self.is_odd):
                        print("wo")
                        return self.findMedianSortedArrays0(nums1[n1 - 1:], nums2[(l2 - 1) // 2:], k - n1 + 1 - (l2 - 1) // 2)
                    else:
                        return self.findMedianSortedArrays0(nums1[0:n1], nums2[0:(l2 + 1) // 2], k)
                elif n1 <= l1 - n1:
                    if (n1 + l2 // 2 > k and self.is_odd) or (n1 + l2 // 2 > k - 1 and not self.is_odd):
                        return self.findMedianSortedArrays0(nums1[0:n1 + 1], nums2[0:l2 // 2 + 1], k)
                    else:
                        return self.findMedianSortedArrays0(nums1[n1:], nums2[l2 // 2:],
                                                            k - l2 // 2 - n1)
                elif n1 == l1 - n1:
                    sorted_list = sorted([nums1[n1], nums1[n1 - 1], nums2[l2 // 2], nums2[(l2 - 1) // 2]])
                    middle1 = 0.5 * (sorted_list[1] + sorted_list[2])
                    if l2 // 2 is not (l2 - 1) // 2:
                        return middle1
                    else:
                        if n1 + l2 // 2 >= k:
                            middle2 = nums1[n1 - 1] if nums1[n1 - 1] > nums2[l2 // 2 - 1] else nums2[l2 // 2 - 1]
                        else:
                            middle2 = nums1[n1] if nums1[n1] < nums2[l2 // 2 + 1] else nums2[l2 // 2 + 1]
                        return 0.5 * (middle1 + middle2)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        if l % 2 == 1:
            self.is_odd = True
        else:
            self.is_odd = False
        lala = self.findMedianSortedArrays0(nums1, nums2, l // 2)
        print("lalala", lala)
        return lala


if __name__ == '__main__':
    solution1 = Solution()
    lala = solution1.findMedianSortedArrays([4, 6], [1,2, 3,5,7])
