lines = open('days/day08_input.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 8 ~~~~~~~~~~~~~~~~~~~~~~~~~')

def run_code(code):
  acc = 0
  ran = set()
  cur = 0
  line = code[cur]
  while True:
    ran.add(cur)
    line = line.split(' ')
    if line[0] == 'jmp':
      cur = cur + int(line[1][1:]) if line[1][0] == '+' else cur - int(line[1][1:])
    else:
      if line[0] == 'acc':
        acc = acc + int(line[1][1:]) if line[1][0] == '+' else acc - int(line[1][1:])
      cur = cur + 1
    if cur == len(code):
      return {'success': True, 'acc': acc}
    line = code[cur]
    if cur in ran:
      return {'success': False, 'acc': acc}
print('Part 1:', run_code(lines)['acc'])

index = 0
res = run_code(lines)
while not res['success']:
  code = []
  while code == []:
    l = lines[index]
    if l.split(' ')[0] == 'jmp':
      code = lines[:index] + ['nop '+l.split(' ')[1]] + lines[index+1:]
    if l.split(' ')[0] == 'nop':
      code = lines[:index] + ['jmp '+l.split(' ')[1]] + lines[index+1:]
    index = index + 1
  res = run_code(code)
print('Part 2:', res['acc'])

print()