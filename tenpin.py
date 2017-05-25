#!/usr/bin/env python

import sys

def get_bonus(start, step, frames):
  start += 1
  end = start + step
  bonus = 0
  for e, f in enumerate(frames[start:end]):
    try:
      bonus += get_score(f)[0]
    except:
      prev_score = frames[start:end][e-1]
      this_score = 10 - int(prev_score)
      bonus += this_score
  return bonus

def get_score(s):
  if s.lower() == "x":
    score = [10, 2]
  elif s == "/":
    raise Exception("must determine spare")
  elif s == "-":
    score = [0, 0]
  else:
    score = [int(s), 0]
  return score

scores = sys.argv[1]
scores_by_frame = [s for s in scores]
total_score = 0
prev_score = 0
actual_frame = 1
for s, sbf in enumerate(scores_by_frame):
  try:
    this_frame_score, bonus_step = get_score(sbf)
    if sbf.lower() == "x":
      actual_frame += 1
  except:
    this_frame_score = 10 - prev_frame_score
    bonus_step = 1
  actual_frame += 1
  prev_frame_score = this_frame_score
  bonus = 0
  if actual_frame < 20:
    bonus = get_bonus(s, bonus_step, scores_by_frame)
  total_score += this_frame_score + bonus
print("[frames] %s\n[score] %s" %(scores, total_score))
