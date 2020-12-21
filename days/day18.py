import re

# lines = open('days/day18_input.txt', "r").read().split('\n')
lines = open('test.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 18 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def eval(inp):
  stack = []
  for t in inp:
    print(stack)
    if re.match(r'\d', t) is not None:
      stack.insert(0,int(t))
      # stack.append(int(t))
    else:
      if t == '+':
        a, b = stack.pop(), stack.pop()
        stack.append(a + b)
      if t == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(a - b)
      if t == '*':
        a, b = stack.pop(), stack.pop()
        stack.append(a * b)
      if t == '/':
        a, b = stack.pop(), stack.pop()
        stack.append(a / b)
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
    elif re.match(r'[\+\-\*\/]', c) is not None or c == '(':
      opp.append(c)
    elif c == ')':
      top = opp.pop()
      while top != '(':
        output.append(top)
        top = opp.pop()
  while opp:
    output.append(opp.pop())
  print(output)   
  print(exp,' = ', eval(output))
  print() 
  # total = total + eval(output)
print('Part 1:', total)

print()