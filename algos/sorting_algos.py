def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  return arr

def bubble(arr, ascending=True):
  for i in range(0, len(arr)-1):
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

def main():
  arr = [4,2,3,1,5]
  bubble(arr, False)

if __name__ == "__main__":
  main()