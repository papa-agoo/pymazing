"""
Game initialization and main loop management.

Copyright: Copyright © 2014 Mikko Ronkainen <firstname@mikkoronkainen.com>
License: MIT License, see the LICENSE file.
"""

import sfml as sf
import OpenGL.GL as gl
import time

from pymazing import fpscounter as fc

class GameEngine:
    def __init__(self, window, framebuffer):
        self.should_run = True
        self.window = window
        self.framebuffer = framebuffer
        self.fps_counter = fc.FpsCounter()
        self.fps_font = sf.Font.from_file("data/fonts/dejavu-sans-mono-bold.ttf")
        self.fps_text = sf.Text("56", self.fps_font, 16)
        self.fps_text.position = (4, 2)
        self.fps_text.style = sf.Text.REGULAR
        self.fps_text.color = sf.Color(255, 255, 255, 255)

    def run(self):
        previous_time = time.clock()

        while self.should_run:
            current_time = time.clock()
            frame_time = current_time - previous_time
            previous_time = current_time

            if frame_time > 0.25:
                frame_time = 0.25

            self._update(frame_time)
            self._render()

    def _update(self, time_step):
        for event in self.window.events:
            if type(event) is sf.CloseEvent:
                self.should_run = False

            if type(event) is sf.ResizeEvent:
                gl.glViewport(0, 0, event.size.x, event.size.y)

        if sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            self.should_run = False

        self.fps_text.string = self.fps_counter.get_fps()

    def _render(self):
        self.window.clear(sf.Color.RED)
        self.framebuffer.render()
        self.window.push_GL_states()
        self.window.draw(self.fps_text)
        self.window.pop_GL_states()
        self.window.display()
        self.framebuffer.clear()
        self.fps_counter.tick()
