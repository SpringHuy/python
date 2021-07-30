def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield

class AirbusA319():
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23), "ABCDEFGHJK"

class Boeing777():
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1,23), "ABCDEFGHJK"