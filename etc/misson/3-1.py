# 변수 t의 숫자를 바꿔도 좋습니다. 단, 형식(시:분)은 지켜주세요.
# ex) 12:00, 5:30, 9:25 등
t = '12:40'

if 12 == int(t[:2]):
  print(t, "PM")
elif 12 < int(t[:2]):
  print(t, "PM")
else:
  print(t, "AM")