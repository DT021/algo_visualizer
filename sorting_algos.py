import random
import numpy as np

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
  for i in range(0, len(arr)):
    for j in range(0, len(arr) - i - 1):
      if (ascending == True):
        if (arr[j] > arr[j + 1]):
          arr = swap(arr, j, j + 1)
      else:
        if (arr[j] < arr[j + 1]):
          print(arr)
          arr = swap(arr, j, j+1)
  return arr

# Selection sort: Worst Case = Best Case = O(n^2)
def selection(arr, ascending=True):
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
      print(arr)
      arr = swap(arr, min, i)
  print(arr)
  return arr

# Insertion sort: Worst Case = O(n^2), Best Case = O(n)
def insertion(arr, ascending=True):
  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    if ascending == True:
      while (i >= 0 and arr[i] > key):
        swap(arr, i, i + 1)
        i -= 1
    else:
      while (i >= 0 and arr[i] < key):
        swap(arr, i, i + 1)
        i -= 1
  return arr

# Merge sort - Best Case = Worst Case = O(nlogn)
def mergeSort(arr, ascending=True):
  mergeHelp(arr, 0, len(arr))

def mergeHelp(arr, start, end, ascending=True):
  if(start < 1):
    mid = (start+end)/2
    mergeHelp(arr, start, mid)
    mergeHelp(arr, mid + 1, end)
    return merge(arr, start, mid, end, ascending)

def merge(left, right, ascending):
  res = []
  i = j = 0
  while (i < len(left) and j < len(right)):
    if ascending == True:
      if (left[i] <= right[j]):
        res.append(left[i])
        i += 1
      else:
        res.append(right[j])
        j += 1
    else:
      if (left[i] >= right[j]):
        res.append(left[i])
        i += 1
      else:
        res.append(right[j])
        j += 1
  res += left[i:]
  res += right[j:]
  return res

def main():
  # arr = [4,2,3,1,5]
  arr = arrgen(lo=0, hi=10, s=10)
  print(arr)
  mergeSort(arr, False)
  print(arr)

if __name__ == "__main__":
  main()