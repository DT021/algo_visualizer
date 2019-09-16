import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sorting_algos as srt
from matplotlib.collections import PatchCollection

plt.style.use('seaborn-pastel')

def main():
  # Initialization
  arr = srt.arrgen(lo=0, hi=50, s=50)
  temp = srt.copy.deepcopy(arr)
  a, frames = srt.bubble(temp, ascending=True)

  # Plotting image
  fig, ax = plt.subplots(figsize=(6, 6))
  ax.set_title('Sorting Visualizer')
  ax.set_xlabel('Values')
  rects = ax.bar(range(len(arr)), arr)

  # Animate
  def animate(fi):
    for rect, y in zip(rects, frames[fi]):
      rect.set_height(y)
    return (rects)

  # Show animation
  anim = animation.FuncAnimation(fig,animate,frames=len(frames),interval=len(frames),repeat=False, blit=False)
  plt.show()

if __name__ == "__main__":
  main()