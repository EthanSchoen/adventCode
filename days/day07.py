def num_bags(rules, color):
  bags = 1
  for c in rules[color].keys():
    bags = bags + rules[color][c] * num_bags(rules, c)
  return bags

lines = open('days/day07_input.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 7 ~~~~~~~~~~~~~~~~~~~~~~~~~')

rules = {}
for rule in lines:
  rule = rule.split(' ')
  bag_color = ' '.join(rule[:2])
  contains = ' '.join(rule[4:]).split(',')
  contain_dict = {}
  for c in contains:
    c = c.strip().split(' ')
    if c[0] == 'no':
      break
    color = ' '.join(c[1:3])
    contain_dict[color] = int(c[0])
  rules[bag_color] = contain_dict

valid = 0
for r in rules:
  children = rules[r].keys()
  while len(children) > 0:
    new_list = []
    try:
      for c in children:
        if c == 'shiny gold':
          raise StopIteration
        else:
          for k in rules[c].keys():
            new_list.append(k)
    except StopIteration:
      valid = valid + 1
      break
    children = new_list
print('Part 1:',valid)

bags = num_bags(rules, 'shiny gold')-1
print('Part 2:', bags)

print()