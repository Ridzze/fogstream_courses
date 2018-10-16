"""
В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут. Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок. Выведите два целых числа: время окончания урока в часах и минутах.
"""

h = 9                                      #начальное время, часы
m = 0                                      #минуты
l = int (input('Введите номер урока:'))

lchet = (l-1) // 2                         #получаем кол-во перемен "четных"/15 мин
lnechet = ((l-1) % 2) + lchet              #"нечетных"/5 мин
lsum = (lchet * 15) + (lnechet * 5)        #общее кол-во минут

sum = (l*45) + lsum + (9*60)                #общее кол-во минут
h = sum // 60
m = sum % 60

if l == 1 or l == 4 or l == 5 or l == 9 or l == 10:
  print (str(l)+'-ый урок закончится в: ',h,' часов ',m, 'минут',)

elif l == 2 or l == 6 or l == 7 or l == 8:
  print (str(l)+'-ой урок закончится в: ',h,' часов ',m, 'минут',)

elif l == 3:
  print (str(l)+'-ий урок закончится в: ',h,' часов ',m, 'минут',)
