import time


def heapify(arr, n, i):
    
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code
arr = [5, 15, 39, 83, 153, 255, 395, 579, 813, 1103, 1455, 1875, 2369, 2943, 3603, 4355, 5205, 6159, 7223, 8403, 9705, 11135, 12699, 14403, 16253, 18255, 20415, 22739, 25233, 27903, 30755, 33795, 37029, 40463, 44103, 47955, 52025, 56319, 60843, 65603, 70605, 75855, 81359, 87123, 93153, 99455, 106035, 112899, 120053, 127503, 135255, 143315, 151689, 160383, 169403, 178755, 188445, 198479, 208863, 219603, 230705, 242175, 254019, 266243, 278853, 291855, 305255, 319059, 333273, 347903, 362955, 378435, 394349, 410703, 427503, 444755, 462465, 480639, 499283, 518403, 538005, 558095, 578679, 599763, 621353, 643455, 666075, 689219, 712893, 737103, 761855, 787155, 813009, 839423, 866403, 893955, 922085, 950799, 980103]
heapSort(arr)
n = len(arr)

print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")



end = time.process_time()
print('tempo: ',end - start)