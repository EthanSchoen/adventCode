import re

lines = open('day2_input.txt', "r").read().split('\n')

valid = 0
for line in lines:
  rule_min, rule_max, char, password = re.split('[ \-:]+', line)
  rule_min = int(rule_min)
  rule_max = int(rule_max)
  if password.count(char) >= rule_min and password.count(char) <= rule_max:
    valid = valid + 1

print('First policy number valid: ', valid)

valid = 0
for line in lines:
  rule_ind1, rule_ind2, char, password = re.split('[ \-:]+', line)
  rule_ind1 = int(rule_ind1)-1
  rule_ind2 = int(rule_ind2)-1
  # xor
  if bool(password[rule_ind1] == char) ^ bool(password[rule_ind2] == char):
    valid = valid + 1

print('Second policy number valid: ', valid)