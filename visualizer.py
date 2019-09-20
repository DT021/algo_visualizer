# Matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sorting_algos as srt
from matplotlib.collections import PatchCollection

# Plotly
import plotly.express as px
import plotly.graph_objects as go

plt.style.use('seaborn-pastel')

def showBasicSorts(method):
  # Initialization
  arr = srt.arrgen(lo=0, hi=55, s=55)
  temp = srt.copy.deepcopy(arr)
  frames = []
  if method == "insertion":
    _, frames = srt.insertion(temp, ascending=True)
  elif (method == "selection"):
    _, frames = srt.selection(temp, ascending=True)
  elif (method == "bubble"):
    _, frames = srt.bubble(temp, ascending=True)

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
  anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=len(frames), repeat=False, blit=False)
  Writer = animation.writers['imagemagick']
  writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
  loc = method + ".gif"
  anim.save(loc, writer=writer)
  plt.show()

def plotlyBasicSorts(method):
  # Initialization
  arr = []
  temp = []
  frames = []
  if method == "Insertion sort":
    arr = srt.arrgen(lo=0, hi=25, s=25)
    temp = srt.copy.deepcopy(arr).tolist()
    _, frames = srt.insertion(temp, ascending=True)
  elif (method == "Selection sort"):
    arr = srt.arrgen(lo=0, hi=25, s=25)
    temp = srt.copy.deepcopy(arr).tolist()
    _, frames = srt.selection(temp, ascending=True)
  elif (method == "Bubble sort"):
    arr = srt.arrgen(lo=0, hi=25, s=25)
    temp = srt.copy.deepcopy(arr).tolist()
    _, frames = srt.bubble(temp, ascending=True)

  # Create figure
  figure = {
    'data': [{
      'type': 'bar',
      'x': list(srt.np.linspace(0, len(arr), num=len(arr))),
      'y': arr
    }],
    'layout': {
      'xaxis': {
        'title': 'X',
        'gridcolor': '#FFFFFF',
        'linecolor': '#000',
        'linewidth': 0,
        'zeroline': False,
        'autorange': True
      },
      'yaxis': {
        'title': 'Y',
        'gridcolor': '#FFFFFF',
        'linecolor': '#000',
        'linewidth': 0,
        'autorange': True
      },
      'title': method + ' - Iterations: ' + str(len(frames)),
      'updatemenus': [{
        'type': 'buttons',
        'buttons': [{
          'label': 'Play',
          'method': 'animate',
          'args': [None, {
            'frame': {
              'duration': 30,
              'redraw': True
            },
            'fromcurrent': True,
            'transition': {
              'duration': 30,
              'easing': 'quad-in-out'
            }
          }]
        }]
      }]
    },
    'frames': []   
  }

  # Update frame
  for k in range(len(frames)):
    frame = {"data": {
      'type': 'bar',
      "x": list(srt.np.linspace(0, len(arr), num=len(arr))),
      "y": frames[k],
      "name": 'f-' + str(k)
    }}
    figure["frames"].append(frame)

  fig = go.Figure(figure)
  return fig

def showMergeSort():
  # Initialization
  arr = srt.arrgen(lo=0, hi=105, s=105)
  temp = srt.copy.deepcopy(arr).tolist()
  frames = []
  srt.mergesort(temp, frames)

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
  anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=len(frames), repeat=False, blit=False)
  
  # Set up formatting for the movie files
  Writer = animation.writers['imagemagick']
  writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
  anim.save('ms.gif', writer=writer)
  plt.show()

def plotlyMS():
  # Initialization
  arr = srt.arrgen(lo=0, hi=25, s= 25)
  temp = srt.copy.deepcopy(arr).tolist()
  frames = []
  srt.mergesort(temp, frames)
 
  # Create figure
  figure = {
    'data': [{
      'type': 'bar',
      'x': list(srt.np.linspace(0, len(arr), num=len(arr))),
      'y': arr
    },{
      'type': 'bar',
      'x': list(srt.np.linspace(0, len(arr), num=len(arr))),
      'y': arr
    }],
    'layout': {
        'xaxis': {
        'title': 'X',
        'gridcolor': '#FFFFFF',
        'linecolor': '#000',
        'linewidth': 1,
        'zeroline': False,
        'autorange': True
      },
      'yaxis': {
        'title': 'Y',
        'gridcolor': '#FFFFFF',
        'linecolor': '#000',
        'linewidth': 1,
        'autorange': True
      },
      'title': "Merge Sort" + ' - Iterations: ' + str(len(frames)),
      'updatemenus': [{
        'type': 'buttons',
        'buttons': [{
          'label': 'Play',
          'method': 'animate',
          'args': [None, {
            'frame': {
              'duration': 100,
              'redraw': True
            },
            'fromcurrent': True,
            'transition': {
              'duration': 300,
              'easing': 'quadratic-in-out'
            }
          }]
        }]
      }]
    },
    'frames': []   
  }

  for k in range(len(frames)):
    frame = {"data": {
      'type': 'bar',
      "x": list(srt.np.linspace(0, len(arr), num=len(arr))),
      "y": frames[k]
    }}
    figure["frames"].append(frame)

  fig = go.Figure(figure)
  return fig

def main():
  plotlyBasicSorts("Selection sort")
  pass

if __name__ == "__main__":
  main()