class TooYoungException(Exception):
    def __init__(self, description):
        self.description = description

class TooOldException(Exception):
    def __init__(self, description):
        self.description = description

age = int(input("Enter your age: "))
if age > 60:
    raise TooOldException("Your age is already crossed marriage age, No chance of getting marriage")
elif age < 18:
    raise TooYoungException("Please wait some more time, definitely you will get a perfect match")
else:
    print("You will get match details by mail soon...")