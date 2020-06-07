import matplotlib.pyplot as plt


def set_axes_breast(temperature_table, min_t, max_t, axes):
    # настраиваем палитру
    palette = plt.cm.RdYlGn_r
    palette.set_under('w')

    # настраиваем площадку для рисунка
    axes.get_xaxis().set_ticks([])
    axes.get_yaxis().set_ticks([])

    # рисуем на площадке
    axes.pcolormesh(temperature_table, cmap=palette, vmin=min_t, vmax=max_t, antialiased=True)
