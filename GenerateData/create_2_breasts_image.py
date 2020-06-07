import GenerateData.calc_breast_tmap as calc_breast
import GenerateData.draw_axe as draw_axe
import matplotlib.pyplot as plt


def create(left_t_values, right_t_values):
    (l_table, l_min, l_max) = calc_breast.calc_t_map(t_values=left_t_values, breast_side='left')
    (r_table, r_min, r_max) = calc_breast.calc_t_map(t_values=right_t_values, breast_side='right')
    min = l_min if l_min < r_min else r_min
    max = l_max if l_max > r_max else r_max

    fig, subplots = plt.subplots(nrows=1, ncols=2, figsize=(4, 2))

    draw_axe.set_axes_breast(temperature_table=r_table, min_t=min, max_t=max, axes=fig.axes[0])
    draw_axe.set_axes_breast(temperature_table=l_table, min_t=min, max_t=max, axes=fig.axes[1])

    return fig
