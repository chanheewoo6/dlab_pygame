print('어서오세요, 디랩 항공사입니다!')
flights = ['0:20', '5:30', '8:40', '12:00', '12:40', 
           '13:30', '15:00', '15:20', '18:25', '21:00']
myFlight = []

time = int(input("원하는 시간대(0~23): "))

flight_hours = []
for f in flights:
    hour = int(f.split(':')[0])
    flight_hours.append(hour)

if time >= 24:
  print("잘못 입력")
elif time in flight_hours:
  for i in range(len(flight_hours)):
    if flight_hours[i] == time:
      myFlight.append(flights[i])
  print("가능한 시간: ",myFlight)
else:
  print("가능한 시간: ", myFlight)