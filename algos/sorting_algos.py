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
  print(arr)
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

# Insertion sort
def insertion(arr, )

def main():
  arr = [4,2,3,1,5]
  bubble(arr, False)

if __name__ == "__main__":
  main()