def bubble_sort(Lists):
    count = len(Lists)
    for i in range(count):
        for j in range(i+1, count):
            if Lists[i] >= Lists[j]:
                Lists[i], Lists[j] = Lists[j], Lists[i]
    return Lists

print bubble_sort([2, 1, 5, 7, 6, 9])


def insert_sort(Lists):

    count = len(Lists)
    for i in range(1, count):
        key = Lists[i]
        j = i-1
        while j >= 0:
            if Lists[j] >= key:
                Lists[j+1] = Lists[j]
                Lists[j] = key
            j -= 1
    return Lists

print insert_sort([2, 1, 5, 7, 6, 9])


def merge(left, right):

    result = list()
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(Lists):
    if len(Lists) <= 1:
        return Lists
    nums = len(Lists) // 2
    left = merge_sort(Lists[:nums])
    right = merge_sort(Lists[nums:])
    return merge(left, right)

print merge_sort([4, 2, 5, 1, 3, 7, 6])


def quick_sort(Lists, left, right):
    if left >= right:
        return Lists
    key = Lists[left]
    low = left
    high = right
    while left < right:
        while left < right and Lists[right] >= key:
            right -= 1
        Lists[left] = Lists[right]
        while left < right and Lists[left] <= key:
            left += 1
        Lists[right] = Lists[left]
    Lists[left] = key
    quick_sort(Lists, low, left-1)
    quick_sort(Lists, left+1, high)
    return Lists

print quick_sort([4, 2, 5, 1, 3, 7, 6], 0, 6)


def shell_sort(Lists):
    count = len(Lists)
    step = 2
    group = count / 2
    while group > 0:
        for i in range(group, count):
            key = Lists[i]
            j = i - group
            while j-group >= 0:
                if Lists[j] >= key:
                    Lists[j+group] = Lists[j]
                    Lists[j] = key
                j -= group
        group /= step
    return Lists

print shell_sort([1, 7, 5, 3, 2, 4, 8])


