"""FPS counter with smooth averaging."""
# Copyright © 2014 Mikko Ronkainen <firstname@mikkoronkainen.com>
# License: MIT, see the LICENSE file.

import time


class FpsCounter:
    def __init__(self):
        self.last_update_time = time.clock()
        self.frame_time_sum = 0.0
        self.frame_time_sum_counter = 0
        self.last_moving_average_calculation_time = 0.0
        self.moving_average_frame_time = 1.0 / 30
        self.previous_moving_average_frame_time = 1.0 / 30
        self.fps_string = "0"

    def tick(self):
        """
        Record a single frame.
        """
        current_time = time.clock()
        frame_time = current_time - self.last_update_time
        self.last_update_time = current_time

        # filter out too large changes in the frametime
        if frame_time > (2 * self.moving_average_frame_time):
            frame_time = 2 * self.moving_average_frame_time

        self.frame_time_sum += frame_time
        self.frame_time_sum_counter += 1

        # only calculate the moving average 15 times per second
        if (current_time - self.last_moving_average_calculation_time) > (1.0 / 15):
            alpha = 0.25
            self.moving_average_frame_time = alpha * (self.frame_time_sum / self.frame_time_sum_counter) + (1.0 - alpha) * self.previous_moving_average_frame_time

            self.previous_moving_average_frame_time = self.moving_average_frame_time
            self.last_moving_average_calculation_time = current_time

            self.frame_time_sum = 0
            self.frame_time_sum_counter = 0

            self.fps_string = str(int(1.0 / self.moving_average_frame_time))

    def get_fps(self):
        """
        Get the FPS as a preformatted string.
        """
        return self.fps_string
