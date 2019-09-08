import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sorting_algos as srt

plt.style.use('seaborn-pastel')

def animate(arr, rects):
  for rect, val in zip(rects, arr):
    rect.set_height(val)

def main():
  arr = srt.arrgen(lo=0, hi=10, s=10)
  print(arr)
  gen = srt.bubble(arr, ascending=True)
  print(arr)
  fig, ax = plt.subplots(figsize=(6, 6))
  ax.set_title('Sorting Visualizer')
  ax.set_xlabel('Values')
  rects = ax.bar(arr, range(len(arr)))
  plt.show()
  pass

if __name__ == "__main__":
  main()