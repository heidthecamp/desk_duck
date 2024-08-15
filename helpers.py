#   Source:
#!  https://github.com/amitt1236/Gaze_estimation/blob/master/helpers.py
relative = lambda landmark, shape: (int(landmark.x * shape[1]), int(landmark.y * shape[0]))
relativeT = lambda landmark, shape: (int(landmark.x * shape[1]), int(landmark.y * shape[0]), 0)