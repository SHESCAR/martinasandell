import datetime

alarmHour = int(input("What our do you want to wake up?"))
alarmMinute = int(input("What minute do you want to wake up?"))
amPm = str(input("am or pm"))

if(amPm == "Pm"):
    alarmHour = alarmHour + 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
        print("Wake up")
        break
    print("exited")