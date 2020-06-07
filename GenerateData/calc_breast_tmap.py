import numpy as np
import math
from scipy.interpolate import SmoothBivariateSpline


_x_breast = np.array([])
_y_breast = np.array([])

_x_armpit = 0
_y_armpit = 0
_r_armpit = 0


def calc_t_map(t_values, breast_side):
    _init(breast_side)
    f = SmoothBivariateSpline(x=_x_breast, y=_y_breast, z=t_values[:-1], kx=2, ky=2)

    temperature_table = _fill_table(
        x_range=np.arange(-1, 1.01, 0.01),
        y_range=np.arange(-1, 1.01, 0.01),
        f=f,
        circle_x=_x_armpit,
        circle_y=_y_armpit,
        circle_r=_r_armpit,
        circle_value=t_values[-1])

    min = _not_negative_min(temperature_table)
    max = _max(temperature_table)

    return temperature_table, min, max


def _init(breast_side):
    global _x_breast, _x_armpit, _y_breast, _y_armpit, _r_armpit
    __midpoint = math.sqrt(2) / 2

    if breast_side == 'right':
        _x_breast = np.array([0, 0, __midpoint, 1, __midpoint, 0, -__midpoint, -1, -__midpoint])
        _x_armpit = -1 + 0.11
    elif breast_side == 'left':
        _x_breast = np.array([0, 0, -__midpoint, -1, -__midpoint, 0, __midpoint, 1, __midpoint])
        _x_armpit = 1 - 0.11

    _y_breast = np.array([0, 1, __midpoint, 0, -__midpoint, -1, -__midpoint, 0, __midpoint])
    _y_armpit = 1 - 0.11
    _r_armpit = 0.1


def _fill_table(x_range, y_range, f, circle_x, circle_y, circle_r, circle_value):
    table = []
    for y in y_range:
        line = []
        for x in x_range:
            if x * x + y * y > 1:
                x_moved = x - circle_x
                y_moved = y - circle_y
                if x_moved * x_moved + y_moved * y_moved <= circle_r * circle_r:
                    line.append(circle_value)
                else:
                    line.append(-1)
            else:
                line.append(f.ev(x, y))
        table.append(line)
    return table


def _not_negative_min(ar):
    _min = math.inf
    for line in ar:
        for item in line:
            if 0 < item < _min:
                _min = item
    return _min


def _max(ar):
    _max = -math.inf
    for line in ar:
        for item in line:
            if _max < item:
                _max = item
    return _max