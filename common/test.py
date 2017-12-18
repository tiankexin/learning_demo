# -*- coding: utf-8 -*-


def bubble_sort(Lists):
    count = len(Lists)
    for i in range(count):
        for j in range(i+1, count):
            if Lists[i] >= Lists[j]:
                Lists[j], Lists[i] = Lists[i], Lists[j]
        i += 1
    return Lists

print "============"
print bubble_sort([4, 2, 5, 1, 3, 7, 6])


def insert_sort(Lists):
    count = len(Lists)
    for i in range(1, count):
        key = Lists[i]
        j = i-1
        while j >= 0:
            if key < Lists[j]:
                Lists[j+1] = Lists[j]
                Lists[j] = key
            j -= 1
    return Lists
print "============"
print insert_sort([4, 2, 5, 1, 3, 7, 6])


def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[i:]
    return result


def merge_sort(Lists):
    if len(Lists) <= 1:
        return Lists
    nums = len(Lists) /2
    left = merge_sort(Lists[:nums])
    right = merge_sort(Lists[nums:])
    return merge(left, right)

print "============"
print insert_sort([4, 2, 5, 1, 3, 7, 6])


def quick_sort(Lists, left, right):
    if left >= right:
        return Lists
    low = left
    high = right
    key = Lists[left]
    while left < right:
        while left < right and key <= Lists[right]:
            right -= 1
        Lists[left] = Lists[right]
        while left < right and key >= Lists[left]:
            left += 1
        Lists[right] = Lists[left]
    Lists[left] = key
    quick_sort(Lists, low, left-1)
    quick_sort(Lists, left+1, high)
    return Lists

print "============"
print quick_sort([4, 2, 5, 1, 3, 7, 6], 0, 6)



