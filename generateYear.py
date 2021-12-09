from pathlib import Path
from datetime import datetime

year = str(datetime.now().year)
Path(year + '/days').mkdir(parents=True, exist_ok=True)

open(year + '/run.py', 'w').write("""import sys
import time

t0 = time.time()
if len(sys.argv) == 1:
  for a in range(1,26):
    t = time.time()
    __import__('days.day{:02d}'.format(a))
    print('Time:',time.time()-t)
    print()
else:
  t = time.time()
  for a in sys.argv[1:]:
    t = time.time()
    __import__('days.day{:02d}'.format(int(a)))
    print('Time:',time.time()-t)
    print()
print('Total Time:',time.time()-t0)
""")

for n in range(1,26):
  day = 'day{:02d}'.format(n)
  open(year + '/days/' + day + '_input.txt', 'w')
  open(year + '/days/' + 'day{:02d}'.format(n) + '.py', 'w').write("""
input = open('days/day{:02d}_input.txt', "r").read().split('\\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day {:d} ~~~~~~~~~~~~~~~~~~~~~~~~~')

# Part 1
def part1():
  return

# Part 2
def part2():
  return

print('part1:' + str(part1()))
print('part2:' + str(part2()))
print()
""".format(n, n))