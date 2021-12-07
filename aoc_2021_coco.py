# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Coconut
#     language: coconut
#     name: coconut
# ---

# %% [markdown]
# # Advent of Code 2021
#
# This solution (Jupyter notebook; coconut 1.5.0 on python 3.7.11) by kannix68, @ 2021-12.  \
# Using anaconda distro, conda v4.10.3, and coconut language. installation on MacOS v10.14.6 "Mojave".

# %%
import sys
import logging
import itertools
import re

import numpy as np
import pandas as pd

import pylib.aochelper as aoc
#from pylib.aochelper import map_list as mapl
#from pylib.aochelper import filter_list as filterl

print("Python version:", sys.version)
print("Version info:", sys.version_info)

log = aoc.getLogger(__name__)
print(f"Initial log-level={aoc.getLogLevelName(log.getEffectiveLevel())}.")

# %% [markdown]
# ## Problem domain code

# %% [markdown]
# ### Day 1: Sonar Sweep

# %%
"Day 1" |> print

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
def solve01pt1(inp):
  """Solve Day 1 part 1."""
  inp = inp |> .split() |> map$(int)
  #f"input-len={inp |> len}" |> log.debug
  outp = pd.Series(inp).diff()[1:].astype(int).tolist()
  outp = outp |> filter$(it -> it > 0)
  #f"rc={outp |> len}" |> log.debug
  return outp |> list |> len


# %%
expected = 7
#log.setLevel(logging.DEBUG)
result = solve01pt1(tests)
aoc.assert_msg("test solve day 1 part 1", result == expected) 

# %%
ins = aoc.read_file_to_str("./in/day01.in")
out = solve01pt1(ins)
print("day 1 part 1 output:", out)

# %%
"Day 1 part 2" |> print


# %%
def solve01pt2(inp):
  """Solve Day 1 part 2."""
  inp = inp |> .split() |> map$(int)
  outp = pd.Series(inp).rolling(3).sum().diff()[3:].astype(int).tolist()
  outp |>= filter$(-> _ > 0) 
  return outp |> list |> len


# %%
expected = 5
result = solve01pt2(tests)
aoc.assert_msg("test solve day 1 part 1", result == expected) 

# %%
out = solve01pt2(ins)
print("day 1 part 2 output:", out)

# %%
