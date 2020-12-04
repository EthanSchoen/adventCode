import sys

if len(sys.argv) == 1:
  for a in range(1,26):
    if a < 10:
      __import__('days.day0'+str(a))
    else:
      __import__('days.day'+str(a))
else:
  for a in sys.argv[1:]:
    if int(a) < 10:
      __import__('days.day0'+a)
    else:
      __import__('days.day'+a)