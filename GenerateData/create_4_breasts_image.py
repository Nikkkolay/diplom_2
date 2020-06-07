import GenerateData.calc_breast_tmap as calc_breast
import GenerateData.draw_axe as draw_axe
import matplotlib.pyplot as plt


def create(left_up_t_values, right_up_t_values, left_dawn_t_values, right_dawn_t_values):
    (l_deep_table, l_deep_min, l_deep_max) = calc_breast.calc_t_map(t_values=left_up_t_values, breast_side='left')
    (r_deep_table, r_deep_min, r_deep_max) = calc_breast.calc_t_map(t_values=right_up_t_values, breast_side='right')
    (l_skin_table, l_skin_min, l_skin_max) = calc_breast.calc_t_map(t_values=left_dawn_t_values, breast_side='left')
    (r_skin_table, r_skin_min, r_skin_max) = calc_breast.calc_t_map(t_values=right_dawn_t_values, breast_side='right')
    _min = min(l_deep_min, r_deep_min, l_skin_min, r_skin_min)
    _max = max(l_deep_max, r_deep_max, l_skin_max, r_skin_max)

    fig, subplots = plt.subplots(nrows=2, ncols=2, figsize=(4, 4))

    draw_axe.set_axes_breast(temperature_table=r_deep_table, min_t=_min, max_t=_max, axes=fig.axes[0])
    draw_axe.set_axes_breast(temperature_table=l_deep_table, min_t=_min, max_t=_max, axes=fig.axes[1])
    draw_axe.set_axes_breast(temperature_table=r_skin_table, min_t=_min, max_t=_max, axes=fig.axes[2])
    draw_axe.set_axes_breast(temperature_table=l_skin_table, min_t=_min, max_t=_max, axes=fig.axes[3])

    return fig
