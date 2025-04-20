# Count inversions in an array where the ith row of the file indicates the ith entry of an array 
# The file contains 100000 integers

def count_inversions(arr):
        """
        Count the number of inversions in the array using a modified merge sort algorithm.
        An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
        """
        if len(arr) < 2:
                return arr, 0
        
        mid = len(arr) // 2
        left, left_inversions = count_inversions(arr[:mid])
        right, right_inversions = count_inversions(arr[mid:])
        merged, split_inversions = merge_and_count(left, right)
        
        return merged, left_inversions + right_inversions + split_inversions

def merge_and_count(left, right):
        """
        Merge two sorted arrays and count the number of split inversions.
        A split inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j],
        where arr[i] is from the left array and arr[j] is from the right array.
        """
        merged = []
        i = j = 0
        inversions = 0
        
        while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                        merged.append(left[i])
                        i += 1
                else:
                        merged.append(right[j])
                        inversions += len(left) - i  # Count inversions
                        j += 1
        
        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inversions
if __name__ == "__main__":
        # Read the file and convert it into a list of integers
        with open('string.txt', 'r') as f:
                arr = [int(line.strip()) for line in f]
        
        # Count inversions
        _, num_inversions = count_inversions(arr)
        
        # Print the number of inversions
        print("Number of inversions:", num_inversions)

