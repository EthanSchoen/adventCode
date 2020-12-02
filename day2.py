lines = open('day2_input.txt', "r").read().split('\n')

valid = 0
for line in lines:
  line = line.split(':')
  rule = line[0].strip()
  char = rule[-1]
  rule = rule[:-1].split('-')
  rule_min = int(rule[0])
  rule_max = int(rule[1])
  password = line[1].strip()
  if password.count(char) >= rule_min and password.count(char) <= rule_max:
    valid = valid + 1

print('First policy number valid: ', valid)

valid = 0
for line in lines:
  line = line.split(':')
  rule = line[0].strip()
  char = rule[-1]
  rule = rule[:-1].split('-')
  rule_ind1 = int(rule[0])-1
  rule_ind2 = int(rule[1])-1
  password = line[1].strip()
  # xor
  if bool(password[rule_ind1] == char) ^ bool(password[rule_ind2] == char):
    valid = valid + 1

print('Second policy number valid: ', valid)