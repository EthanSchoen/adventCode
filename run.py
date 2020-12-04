import sys

# a = open('days/__init__.py', 'w')
# a.write("__all__ = [")

# for i in range(5,26):
#   a = open("days/day"+str(i)+ ".py", "w")
#   a.write("lines = open('days/day" + str(i) + "_input.txt', \"r\").read().split('\\n')")
#   a.write("\nprint('~~~~~~~~~~~~~~~~~~~~~~~~~ Day " + str(i) + " ~~~~~~~~~~~~~~~~~~~~~~~~~')")
#   a.write("\nprint()")
#   a.close()
#   a = open("days/day"+str(i)+ "_input.txt", "w")
#   a.close()

if len(sys.argv) == 1:
  for a in range(1,26):
    __import__('days.day'+str(a))
else:
  for a in sys.argv[1:]:
    __import__('days.day'+a)