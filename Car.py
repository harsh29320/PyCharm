#example program for pycharm 

class Car:
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print('I am going {} kph'.format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time  += 1

    def average_speed(self):
        return self.odometer/ self.time


if __name__ == '__main__':
    my_car = Car()
    print("I am car !")
    while True:
        action = input("What Should I do [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do this")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilomteres".format(my_car.odometer))
        elif action == 'S':
            print ("The cars average speed was {} kph".format(my_car.average_speed()))

        my_car.step()
        my_car.say_state()
