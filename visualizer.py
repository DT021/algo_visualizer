import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sorting_algos as srt

plt.style.use('seaborn-pastel')

def main():
  # Initialization
  arr = srt.arrgen(lo=0, hi=10, s=10)
  temp = srt.copy.deepcopy(arr)
  a, frames = srt.bubble(temp, ascending=True)

  # Plotting image
  fig, ax = plt.subplots(figsize=(6, 6))
  ax.set_title('Sorting Visualizer')
  ax.set_xlabel('Values')
  rects = ax.bar(range(len(arr)),arr)

  # Animate
  def animate(i):
    for f in frames:
      for rect, y in zip(rects, f):
        rect.set_height(y)

  # # Show animation
  anim = FuncAnimation(fig,animate,frames=len(frames),interval=1, blit=False)
  plt.show()
  pass

if __name__ == "__main__":
  main()