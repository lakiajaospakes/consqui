def find_max_subarray(arr):
  """
  Finds the maximum subarray sum in a given array.

  Parameters:
    arr: The array to search.

  Returns:
    The maximum subarray sum.
  """

  max_so_far = -float('inf')
  max_ending_here = 0

  for i in range(len(arr)):
    max_ending_here = max_ending_here + arr[i]
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here

    if max_ending_here < 0:
      max_ending_here = 0

  return max_so_far
