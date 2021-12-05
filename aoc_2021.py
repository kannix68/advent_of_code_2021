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
import copy
import itertools
import logging
import re
import sys

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

def T(lst):
  """Transpose a 2d list."""
  return [list(i) for i in zip(*lst)]  # transpose

def solve_d03pt1(ins):
  lst = ins.splitlines()
  for idx in range(len(lst)):
    lst[idx] = mapl(int, list(lst[idx]))
  l = len(lst)
  log.debug(lst)
  in_t = T(lst)
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
log.setLevel(logging.INFO)
result = solve_d03pt1(tests)
aoc.assert_msg("test solve day 3 part 1", result == expected)

# %%
ins = aoc.read_file_to_str("./in/day03.in")
out = solve_d03pt1(ins)
print("day 3 part 1 output:", out)

# %%
print("Day 3 part 2")

# %% [markdown]
# See coconut language solution.

# %% [markdown]
# ## Day 4: Giant Squid

# %%
print("Day 4, bingo!")

# %%
tests = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".strip()


# %%
def solve_d04pt1(ins):
  """Bingo subsystem."""
  lst = ins.split("\n\n")
  draws, boards = lst[0], lst[1:]
  boardlen = 5
  draws = mapl(int, draws.split(","))
  boards = mapl(lambda it: mapl(lambda inr: mapl(int, re.split(r"\s+", inr.strip())), it.splitlines()), boards)
  tboards = mapl(lambda it: T(it), boards)
  log.debug(f"draws={draws}")
  log.debug(f"boards={boards}")
  log.debug(f"boards0={boards[0]} boards0T={T(boards[0])}")
  found = False
  crossed = []
  for nums in range(boardlen, len(draws)):
    drawn = set(draws[0:nums])
    log.debug(f"draw={drawn}")
    for bdidx in range(len(boards)):
      for rowidx in range(boardlen):
        row, col = set(boards[bdidx][rowidx]), set(tboards[bdidx][rowidx])
        log.trace(f"r={row}; c={col}; drawn={drawn}")
        if set(row).issubset(drawn):
          log.info(f"found bingo! board#{bdidx} row={row}; num={draws[nums-1]}")
          found = True
          crossed = row
          break
        elif set(col).issubset(drawn):
          log.info(f"found bingo! board#{bdidx} col={col}; num={draws[nums]-1}")
          found = True
          crossed = col
          break
      if found:
        break
    if found:
      break
  log.debug(f"idx={bdidx}, nums-drawn-idx={nums} crossed={crossed}, drawn={drawn}")
  remd = set(aoc.flatten(boards[bdidx])) - set(drawn)
  sm = sum(remd)
  last_drawn = draws[nums-1]
  log.debug(f"  last_drawn={last_drawn}; sum={sm} of remainders={remd}")
  return sm * last_drawn

expected = 4512
log.setLevel(logging.INFO)
result = solve_d04pt1(tests)
aoc.assert_msg("test solve day 4 part 1", result == expected)

# %%
ins = aoc.read_file_to_str("./in/day04.in")
out = solve_d04pt1(ins)
print("day 4 part 1 output:", out)

# %%
print("Day 4 part 2: last bingo board to win")


# %%
def find_winboard(draws, boards, fromidx):
  """Find the first winning boards, return info-dictionary."""
  tboards = mapl(lambda it: T(it), boards)
  boardlen = len(boards[0][0])
  found = False
  crossed = []
  for nums in range(boardlen, len(draws)):
    drawn = set(draws[0:nums])
    log.trace(f"draw={drawn}")
    for bdidx in range(len(boards)):
      for rowidx in range(boardlen):
        row, col = set(boards[bdidx][rowidx]), set(tboards[bdidx][rowidx])
        if set(row).issubset(drawn):
          log.debug(f"found bingo! board#{bdidx} row={row}; num={draws[nums-1]}")
          found = True
          crossed = row
          break
        elif set(col).issubset(drawn):
          log.debug(f"found bingo! board#{bdidx} col={col}; num={draws[nums-1]}")
          found = True
          crossed = col
          break
      if found:
        break
    if found:
      break
  remd = set(aoc.flatten(boards[bdidx])) - set(drawn)
  sm = sum(remd)
  last_drawn = draws[nums-1]
  d = {"board_idx": bdidx, "result": sm * last_drawn, "nums_drawn":nums-1}
  return d

def solve_d04pt2(ins):
  """Bingo subsystem, loop through all winners."""
  lst = ins.split("\n\n")
  draws, boards = lst[0], lst[1:]
  boardlen = len(boards[0][0])
  draws = mapl(int, draws.split(","))
  boards = mapl(lambda it: mapl(lambda inr: mapl(int, re.split(r"\s+", inr.strip())), it.splitlines()), boards)
  boards_num = len(boards)
  for i in range(boards_num): # play until last board wins, removing winners
    log.debug(f"start bingo #boards={len(boards)}")
    resd = find_winboard(draws, boards, 0)
    log.debug(f"winboard {resd}")
    boards.remove(boards[resd["board_idx"]])
  return resd["result"]

expected = 1924
log.setLevel(logging.INFO)
result = solve_d04pt2(tests)
aoc.assert_msg("test solve day 4 part 2", result == expected)

# %%
out = solve_d04pt2(ins)
print("day 4 part 2 output:", out)

# %% [markdown]
# ## Day 5: Hydrothermal Venture
# See coconut language solution.

# %%
