def heapify(arr, n, i):
    largest = i  # Initialize largest as the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Compare root with left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare root with right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the reduced heap
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [44, 11, 50, 5, 1, 7]
    print("Original Array:", arr)
    heap_sort(arr)
    print("Sorted Array:", arr)
