"""
Clipper unit tests.

:copyright: © 2014 Mikko Ronkainen <firstname@mikkoronkainen.com>
:license: MIT License, see the LICENSE file.
"""

import numpy as np

from pymazing import clipper, color


def test_clip_world_space_triangle_by_z():
    v0 = np.array([0.0, 1.0, -15.0, 1.0])
    v1 = np.array([-3.0, 1.0, 2.0, 1.0])
    v2 = np.array([3.0, 1.0, 3.0, 1.0])
    triangle = (v0, v1, v2, None)

    clipper.clip_view_space_triangle_by_z(triangle, 1.0, 10.0)


def test_clip_screen_space_triangle():
    screen_space_triangle = (np.array([40.0, -30.0, 1.0]), np.array([-40.0, 20.0, 1.0]), np.array([-80.0, -40.0, 1.0]), color.from_int(255, 255, 255), 1.0)
    clipped_triangles = clipper.clip_screen_space_triangle(screen_space_triangle, 100, 100)