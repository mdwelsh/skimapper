#!/usr/bin/env python3

#from stravaio import strava_oauth2
import gpxpy.gpx
import gpxpy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

gpx_file = open('Crystal_Mountain_first_time.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

lats = []
longs = []
elevs = []
velocities = [0]

def difference(x1, x2, y1, y2):
  return ((x2-x1)**2 + (y2-y1)**2)

for track in gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      longs.append(point.longitude)
      lats.append(point.latitude)
      elevs.append(point.elevation)
      if len(longs) >= 2:
        velocities.append(difference(longs[-1], longs[-2], lats[-1], lats[-2]))
             

plt.style.use('fivethirtyeight')

xs = longs
ys = lats
zs = elevs
colors = velocities

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs, c=colors, cmap='plasma')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()




