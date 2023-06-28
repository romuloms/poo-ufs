from ClockDisplay import ClockDisplay


clock = ClockDisplay(9, 55, 56)
clock.getTime()

for i in range(80):
    clock.timeTick()
    clock.getTime()
