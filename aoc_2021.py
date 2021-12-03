# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Advent of Code 2021
#
# This solution (Jupyter notebook; python 3.10) by kannix68, @ 2021-12.  \
# Using anaconda distro, conda v4.10.3. installation on MacOS v10.14.6 "Mojave".

# %%
import sys
import logging
import itertools
import re

import numpy as np
import pandas as pd

import pylib.aochelper as aoc
from pylib.aochelper import map_list as mapl
from pylib.aochelper import filter_list as filterl

print("Python version:", sys.version)
print("Version info:", sys.version_info)

log = aoc.getLogger(__name__)
print(f"Initial log-level={aoc.getLogLevelName(log.getEffectiveLevel())}.")

# %% [markdown]
# ## Problem domain code

# %% [markdown]
# ### Day 1: Sonar Sweep

# %%
print("Day 1")

tests = """
199
200
208
210
200
207
240
269
260
263""".strip()


# %%
def solve_d01pt1(inp):
  """Solve Day 1 part 1."""
  inp = map(int, inp.split())
  # diff-window ("right"): first row will have NaN, so omit:
  outp = pd.Series(inp).diff()[1:].astype(int).tolist()
  outp = filterl(lambda it: it > 0, outp)
  return len(outp)


# %%
#log.setLevel(logging.DEBUG)
expected = 7
result = solve_d01pt1(tests)
aoc.assert_msg("test solve day 1 part 1", result == expected) 

# %%
ins = aoc.read_file_to_str("./in/day01.in")
out = solve_d01pt1(ins)
print("day 1 part 1 output:", out)

# %%
print("Day 1 part 2")


# %%
def solve_d01pt2(inp):
  """Solve Day 1 part 2."""
  inp = map(int, inp.split())
  # rolling(3)-window ("right"): first 3 rows will have NaN, so omit:
  outp = pd.Series(inp).rolling(3).sum().diff()[3:].astype(int).tolist()
  outp = filterl(lambda it: it > 0, outp)
  return len(outp)


# %%
expected = 5
result = solve_d01pt2(tests)
aoc.assert_msg("test solve day 1 part 2", result == expected) 

# %%
out = solve_d01pt2(ins)
print("day 1 part 2 output:", out)

# %% [markdown]
# ## Day 2: Dive!

# %%
print("Day 2")

# %%
tests = """
forward 5
down 5
forward 8
up 3
down 8
forward 2""".strip()

def solve_d02pt1(inp):
  log.trace(inp)
  cmds = inp.splitlines()
  pos = [0, 0]
  for cmd in cmds:
    log.trace(cmd)
    direct, val = cmd.split(" ")
    val = int(val)
    if direct == "forward":
      pos[0] += val
    elif direct == "down":
      pos[1] += val
    elif direct == "up":
      pos[1] -= val
    log.trace(f"direct={direct}, val={val}; pos={pos}")
  rc = pos[0] * pos[1]
  log.debug(f"rc={rc}")
  return rc

expected = 150
result = solve_d02pt1(tests)
aoc.assert_msg("test solve day 1 part 1", result == expected)

# %%
ins = aoc.read_file_to_str("./in/day02.in")
out = solve_d02pt1(ins)
print("day 2 part 1 output:", out)

# %%
print("Day 2 part 2")


# %%
def solve_d02pt2(inp):
  HPOS, DEPTH, AIM = 0, 1, 2
  cmds = inp.splitlines()
  pos = [0, 0, 0]
  for cmd in cmds:
    direct, val = cmd.split(" ")
    val = int(val)
    if direct == "forward":
      pos[HPOS] += val
      pos[DEPTH] += pos[AIM] * val
    elif direct == "down":
      pos[AIM] += val
    elif direct == "up":
      pos[AIM] -= val
  rc = pos[0] * pos[1]
  log.debug(f"rc={rc}")
  return rc

# `tests` remains the same
expected = 900
result = solve_d02pt2(tests)
aoc.assert_msg("test solve day 2 part 2", result == expected)

# %%
# `ins` remains the same
out = solve_d02pt2(ins)
print("day 2 part 2 output:", out)

# %% [markdown]
# ## Day 3: Binary Diagnostic

# %%
print("Day 3")

# %%
tests = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()

def solve_d03pt1(ins):
  lst = ins.splitlines()
  for idx in range(len(lst)):
    lst[idx] = mapl(int, list(lst[idx]))
  l = len(lst)
  log.debug(lst)
  in_t = [list(i) for i in zip(*lst)]  # transpose
  log.debug(in_t)
  blst = []
  cblst = []
  for col in in_t:
    c0, c1 = col.count(0), l - col.count(0)
    if c0 > c1:
      i = 0
      c = 1
    else:
      i = 1
      c = 0
    blst.append(i)
    cblst.append(c)
  log.debug(blst)
  bnum = int(str.join('', map(str, blst)), 2)
  cnum = int(str.join('', map(str, cblst)), 2)
  log.debug([bnum, cnum])
  return bnum * cnum

expected = 198
result = solve_d03pt1(tests)
aoc.assert_msg("test solve day 1 part 1", result == expected)

# %%
ins = aoc.read_file_to_str("./in/day03.in")
out = solve_d03pt1(ins)
print("day 2 part 1 output:", out)

# %%
print("Day 3 part 2")

# %%
print("tbd")

# %%
