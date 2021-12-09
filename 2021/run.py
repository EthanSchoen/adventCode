import sys
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
