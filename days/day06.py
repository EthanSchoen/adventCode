lines = open('days/day06_input.txt', "r").read().split('\n\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 6 ~~~~~~~~~~~~~~~~~~~~~~~~~')

tally = {}
for group in lines:
  answers = []
  for ans in group.split('\n'):
    for c in ans:
      if c not in answers:
        answers.append(c)
  for a in answers:
    tally[a] = 1 if a not in tally else tally[a]+1
print('part 1:', sum(tally.values()))

tally = {}
for group in lines:
  answers = {}
  group = group.split('\n')
  for ans in group:
    for c in ans:
      answers[c] = 1 if c not in answers else answers[c] + 1
  all_answered = []
  for q in answers.keys():
    if answers[q] == len(group):
      all_answered.append(q)
  for a in all_answered:
    tally[a] = 1 if a not in tally else tally[a]+1
print('part 2:', sum(tally.values()))

print()