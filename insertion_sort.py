

def insertion_sort(nums: list):

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j = j - 1

        nums[j+1] = key

    print(nums)

insertion_sort([1,5,4,8,3,9])