# The main idea is to create a merge and count code that computes the number of inversions
# A given file has 1 - 100000 integers in some order. The main goal is to compute the no. of inversions in the file
# given that the ith row of the files indicates the ith entry of an array

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # There are mid - i inversions, because all the remaining elements in the left subarray
            # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count



# Test the merge_and_count function, load array from file
def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_and_count(arr, temp_arr, 0, n - 1)

# Read integers from a file and store them in a list
def read_file_to_list(filename):
        with open(filename, 'r') as file:
                arr = [int(line.strip()) for line in file]
        return arr

# Main function to read the file and count inversions
def main():
    filename = 'string.txt'  # Replace with your file name
    arr = read_file_to_list(filename)
    num_inversions = count_inversions(arr)
    print(f"Number of inversions in the file: {num_inversions}")


if __name__ == "__main__":
        main()