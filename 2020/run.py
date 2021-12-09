import sys
import time

t0 = time.time()
if len(sys.argv) == 1:
  for a in range(1,26):
    t = time.time()
    if a < 10:
      __import__('days.day0'+str(a))
    else:
      __import__('days.day'+str(a))
    print('Time:',time.time()-t)
    print()
else:
  t = time.time()
  for a in sys.argv[1:]:
    t = time.time()
    if int(a) < 10:
      __import__('days.day0'+a)
    else:
      __import__('days.day'+a)
    print('Time:',time.time()-t)
    print()
print('Total Time:',time.time()-t0)