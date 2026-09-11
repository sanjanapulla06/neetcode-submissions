class Solution:
    def nextGreaterElement(self, nums1, nums2):
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = -1
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            found = nums2[k]
                            break
                    output.append(found)
                    break
        return output