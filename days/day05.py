lines = open('days/day05_input.txt', "r").read().split('\n')
print('~~~~~~~~~~~~~~~~~~~~~~~~~ Day 5 ~~~~~~~~~~~~~~~~~~~~~~~~~')

ids = []
highest = -1
lowest = 99999999999999
for l in lines:
  row = l[:7]
  col = l[-3:]
  row = row.replace('B','1')
  row = row.replace('F','0')
  col = col.replace('R','1')
  col = col.replace('L','0')
  seat_id = int(row, 2) * 8 + int(col, 2)
  ids.append(seat_id)
  highest = max(highest, seat_id)
  lowest = min(lowest, seat_id)
print('heighest seat id:', highest)

all_ids = [i for i in range(lowest,highest+1)]
for i in ids:
  all_ids.remove(i)
print('my seat:',all_ids)

print()