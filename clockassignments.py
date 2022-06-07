
class Clock(object):
    def __init__(self):
        self._hours = 0
        self._minutes = 0

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if value >= 60:
            # Take care, if one adds more than one hour, to
            # take the extra hours into account too:
            self.hours += value // 60
        self._minutes = value % 60

    @hours.setter
    def hours(self, value):
        self._hours = value % 24

    def tic(self):
        self.minutes += 1
        
c = Clock()

assert(c.minutes == 0 and c.hours == 0)

for i in range(24):
    assert(c.hours == i)
    for j in range(60):
        assert(c.hours == i and c.minutes == j)
        c.tic()
        print('{}:{}'.format(c.hours, c.minutes))

assert(c.minutes == 0 and c.hours == 0)