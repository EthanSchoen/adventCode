import re

passports = open('days/day4_input.txt', "r").read().split('\n\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 4 ~~~~~~~~~~~~~~~~~~~~~~~~~')
valid = 0
for p in passports:
  fields = re.split('[ \n]', p)
  required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  for f in fields:
    if required.count(f[:3]) > 0:
      required.remove(f[:3])
  if(len(required) == 0):
    valid = valid + 1

print('part 1: ', valid)

valid = 0
for p in passports:
  fields = re.split('[ \n]', p)
  required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
  for f in fields:
    if required.count(f[:3]) > 0:
      value = f[4:]
      if f[:3] == 'byr':
        value = int(value)
        if 1920 <= value <= 2002:
          required.remove(f[:3])

      if f[:3] == 'iyr':
        value = int(value)
        if 2010 <= value <= 2020:
          required.remove(f[:3])

      if f[:3] == 'eyr':
        value = int(value)
        if 2020 <= value <= 2030:
          required.remove(f[:3])

      if f[:3] == 'hgt':
        unit = value[-2:]
        if not(unit == 'cm' or unit == 'in'):
          continue
        v = int(value[:-2])
        if (unit == 'cm' and (150 <= v <= 193)) or (unit == 'in' and (59 <= v <= 76)):
          required.remove(f[:3])

      if f[:3] == 'hcl':
        if len(value) == 7 and re.match('#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', value):
          required.remove(f[:3])

      if f[:3] == 'ecl':
        if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
          required.remove(f[:3])

      if f[:3] == 'pid':
        if len(value) == 9 and re.match('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', value):
          required.remove(f[:3])
  if(len(required) == 0):
    valid = valid + 1

print('part 2: ', valid)
print()