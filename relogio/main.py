from ClockDisplay import ClockDisplay


# instance the clock
clock = ClockDisplay(0, 0, 0)
# show inital display
clock.getTime()
# run a desired amount of seconds on the clock
clock.runClock(3600)
