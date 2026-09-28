nums = [10, 50, 20, 40, 30]

largest = nums[0]
second = None

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif second is None or (n > second and n != largest):
        second = n

print("Second largest:", second)
