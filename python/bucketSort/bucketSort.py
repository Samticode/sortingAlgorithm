import random

def bucket_sort(arr):
    # Determine the range of input values
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) * (num_buckets - 1) / (max_val - min_val))
        buckets[index].append(num)

    # Sort each bucket individually
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets
    array = [num for bucket in buckets for num in bucket]

    return array

array = [random.randint(1, 75) for _ in range(50)]
 
print("Unsorted list is,")
print(array)
bucket_sort(array)
print("Sorted Array is, ")
print(array)
