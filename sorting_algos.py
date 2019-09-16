import random
import numpy as np
import copy

def arrgen(lo=0, hi=100, s=100, tosort=False, rand=False):
  random.seed(42)
  if rand == True or (s != hi):
    arr = np.random.randint(low=lo, high=hi, size=s)
    return arr
  else:
    arr = np.arange(hi)
    if tosort == False:
      np.random.shuffle(arr)
      return arr
    else:
      return arr
    
def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  return arr

# Bubble sort: Worst Case = Best Case = O(n^2)
def bubble(arr, ascending=True):
  frames = []
  for i in range(0, len(arr)):
    for j in range(0, len(arr) - i - 1):
      if (ascending == True):
        if (arr[j] > arr[j + 1]):
          arr = swap(arr, j, j + 1)
          frames.append(copy.deepcopy(arr))
      else:
        if (arr[j] < arr[j + 1]):
          arr = swap(arr, j, j + 1)
          frames.append(copy.deepcopy(arr))
  return (arr,frames)

# Selection sort: Worst Case = Best Case = O(n^2)
def selection(arr, ascending=True):
  frames = []
  for i in range(0, len(arr)):
    min = i
    for j in range(i + 1, len(arr)):
      if(ascending == True):
        if (arr[j] < arr[min]):
          min = j
      else:
        if (arr[min] < arr[j]):
          min = j
    if (min != i):
      arr = swap(arr, min, i)
      frames.append(copy.deepcopy(arr))
  return arr,frames

# Insertion sort: Worst Case = O(n^2), Best Case = O(n)
def insertion(arr, ascending=True):
  frames = []
  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    if ascending == True:
      while (i >= 0 and arr[i] > key):
        swap(arr, i, i + 1)
        frames.append(copy.deepcopy(arr))
        i -= 1
    else:
      while (i >= 0 and arr[i] < key):
        swap(arr, i, i + 1)
        frames.append(copy.deepcopy(arr))
        i -= 1
  return arr,frames

# Merge sort - Best Case = Worst Case = O(nlogn)

def merge(left, right, frames): 
    if not len(left) or not len(right): 
        return left or right 
  
    result = [] 
    i, j = 0, 0
    while (len(result) < len(left) + len(right)): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i+= 1
        else: 
            result.append(right[j]) 
            j+= 1
        if i == len(left) or j == len(right): 
            result.extend(left[i:] or right[j:]) 
            break 
    frames.append(copy.deepcopy(result))
    return result 
  
def mergesort(list, frames): 
    if len(list) < 2: 
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle], frames) 
    right = mergesort(list[middle:], frames) 
  
    return merge(left, right, frames)
    
def main():
  # arr = [4,2,3,1,5]
  arr = arrgen(lo=0, hi=10, s=10)
  print(arr)
  frames = []
  f = mergesort(arr, frames)
  print(frames)

if __name__ == "__main__":
  main()