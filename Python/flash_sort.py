def flashsort(arr):
    n = len(arr)
    if n == 0:
        return arr

    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Create the number of buckets
    num_buckets = int(n / 2)  # You can adjust the number of buckets
    if num_buckets < 1:
        num_buckets = 1

    # Create the buckets
    buckets = [0] * num_buckets
    for value in arr:
        index = int(num_buckets * (value - min_val) / (max_val - min_val + 1))
        buckets[index] += 1

    # Create a list of positions
    for i in range(1, num_buckets):
        buckets[i] += buckets[i - 1]

    # Create the output array
    output = [0] * n

    # Move elements to their respective positions
    for i in range(n - 1, -1, -1):
        index = int(num_buckets * (arr[i] - min_val) / (max_val - min_val + 1))
        output[buckets[index] - 1] = arr[i]
        buckets[index] -= 1

    return output

# Example usage
if __name__ == "__main__":
    data = [5, 3, 8, 6, 2, 7, 4, 1]
    sorted_data = flashsort(data)
    print("Sorted array:", sorted_data)
