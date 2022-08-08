duration = int(input('Введите промежуток времени в секундах - '))
d = duration//86400
h = (duration%86400)//3600
m = (duration%86400)%3600//60
s = (duration%86400)%3600%60

if duration < 60:
  print(s, "сек")
elif duration < 3600:
  print(m, "мин", s, "сек")
elif duration < 86400:
  print(h, "час", m, "мин", s, "сек")
elif duration > 86400:
  print(d, "дн", h, "час", m, "мин", s, "сек")
