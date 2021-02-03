from physics import Physics

class Drone(object):
    __max_rpm = 1000

    def __init__(self, aimed_position):
        self.__rpm = 0

        self.__mass = 2

        self.__position = 0.0
        self.__velocity = 0.0
        self.__acceleration = 0.0

        self.__aimed_position = aimed_position

        self.__time = 0.0

    def update(self):
        force = self.__rpm * 0.05

        acceleration = (force / self.__mass) + Physics.g
        if acceleration < 0.0 and self.__position == 0:
            self.__acceleration = 0.0
        else:
            self.__acceleration = acceleration

        delta_velocity = self.__acceleration * Physics.timestep
        velocity = self.__velocity + delta_velocity
        if velocity < 0.0 and self.__position == 0:
            self.__velocity = 0.0
        else:
            self.__velocity = velocity

        delta_position = self.__velocity * Physics.timestep + 0.5 * self.__acceleration * Physics.timestep * Physics.timestep
        position = self.__position + delta_position
        if position < 0.0:
            self.__position = 0.0
        else:
            self.__position = position

        self.__time += Physics.timestep

        return (self.__aimed_position - self.__position) / self.__aimed_position

    @property
    def rpm(self):
        return self.__rpm

    @rpm.setter
    def rpm(self, new_rpm):
        if new_rpm > Drone.__max_rpm:
            self.__rpm = Drone.__max_rpm
        else:
            self.__rpm = new_rpm

    @property
    def position(self):
        return self.__position

    @property
    def velocity(self):
        return self.__velocity

    @property
    def acceleration(self):
        return self.__acceleration

    @property
    def time(self):
        return self.__time
