score = int(input("Введите вашу оценку: "))

if score >= 90:
    print("Отлично! Ваша оценка А")
else:
    if score >= 80:
      print("Здорово! Ваша оценка - B")
    else:
      if score >= 70:
        print("Хорошо! Ваша оценка - C")
      else:
        if score >= 60:
          print("Ваша оценка - D. Стоит повторить материал.")
        else:
          print("Вы не сдали экзамен")