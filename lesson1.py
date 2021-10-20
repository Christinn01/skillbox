red = int(input('Введите кол-во красных машин'))
white = int(input('Введите кол-во белых машин'))
decision = ''

if (red > 2 * white) or (white > 2 * red):
  print ('Нет решения')
elif red >= white:
  a = red - white
  for rwr in range(a):
    decision += 'RWR'
  for rw in range(white - a):
    decision += 'RW'
else:
  a = white - red
  for wrw in range(a):
    decision += 'WRW'
  for wr in range(red - a):
    decision += 'WR'
print(decision)