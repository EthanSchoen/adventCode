import re

lines = open('days/day18_input.txt', "r").read().split('\n')
# lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 18 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def eval(inp):
  stack = []
  for t in inp:
    if re.match(r'\d', t) is not None:
      stack.append(int(t))
    else:
      if t == '+':
        a, b = stack.pop(), stack.pop()
        stack.append(a + b)
      if t == '*':
        a, b = stack.pop(), stack.pop()
        stack.append(a * b)
  return stack.pop()

total = 0
for exp in lines:
  output = []
  opp = []
  for c in exp:
    if c == ' ':
      continue
    if re.match(r'\d', c) is not None:
      output.append(c)
    elif re.match(r'[\+\*]', c) is not None:
      while opp and re.match(r'[\+\*]', opp[-1]) is not None:
        output.append(opp.pop())
      opp.append(c)
    elif c == '(':
      opp.append(c)
    elif c == ')':
      top = opp.pop()
      while top != '(':
        output.append(top)
        top = opp.pop()
  while opp:
    output.append(opp.pop())
  total = total + eval(output)
print('Part 1:', total)

total = 0
for exp in lines:
  output = []
  opp = []
  for c in exp:
    if c == ' ':
      continue
    if re.match(r'\d', c) is not None:
      output.append(c)
    elif re.match(r'[\+\*]', c) is not None:
      if c == '*':
        while opp and re.match(r'[\+\*]', opp[-1]) is not None:
          output.append(opp.pop())
      if c == '+':
        while opp and re.match(r'[\+\*]', opp[-1]) is not None and opp[-1] == '+':
          output.append(opp.pop())
      opp.append(c)
    elif c == '(':
      opp.append(c)
    elif c == ')':
      top = opp.pop()
      while top != '(':
        output.append(top)
        top = opp.pop()
  while opp:
    output.append(opp.pop())
  total = total + eval(output)
print('Part 2:', total)

print()