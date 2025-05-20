# Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # khud ko hi return karta hai (iterator ban gaya)

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Loop ko rokne ka signal
        value = self.current
        self.current -= 1
        return value

# ✅ For loop me chala sakte hain!
for number in Countdown(5):
    print(number)
