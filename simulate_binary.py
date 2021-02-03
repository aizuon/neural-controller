import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from physics import Physics
from drone import Drone


if __name__ == "__main__":
    total_time = 30
    total_step = int(total_time / Physics.timestep)

    matplotlib.use("TkAgg")
    plt.ion()
    fig, axes = plt.subplots(nrows=3)
    fig.canvas.set_window_title("Simulation")
    axes[0].set(xlabel="Time", ylabel="Position")
    axes[0].grid()
    position_hl, = axes[0].plot([], [])
    axes[1].set(xlabel="Time", ylabel="Velocity")
    axes[1].grid()
    velocity_hl, = axes[1].plot([], [])
    axes[2].set(xlabel="Time", ylabel="Acceleration")
    axes[2].grid()
    acceleration_hl, = axes[2].plot([], [])
    fig.tight_layout()

    drone = Drone(10.0)
    static_rpm = 700
    drone.rpm = static_rpm
    for i in range(total_step):
        err = drone.update()

        if err < 0:
            drone.rpm = 0
        elif err > 0:
            drone.rpm = static_rpm

        position_hl.set_xdata(np.append(position_hl.get_xdata(), drone.time))
        position_hl.set_ydata(np.append(position_hl.get_ydata(), drone.position))
        axes[0].relim()
        axes[0].autoscale_view()
        velocity_hl.set_xdata(np.append(velocity_hl.get_xdata(), drone.time))
        velocity_hl.set_ydata(np.append(velocity_hl.get_ydata(), drone.velocity))
        axes[1].relim()
        axes[1].autoscale_view()
        acceleration_hl.set_xdata(np.append(acceleration_hl.get_xdata(), drone.time))
        acceleration_hl.set_ydata(np.append(acceleration_hl.get_ydata(), drone.acceleration))
        axes[2].relim()
        axes[2].autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()

    plt.ioff()
    plt.show()
