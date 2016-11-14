import matplotlib.pyplot as plt
import pandas as pd

import prince


df = pd.read_csv('doc/data/presidentielles07.csv', index_col=0)

ca = prince.CA(df, nbr_components=-1)

fig1, ax1 = ca.plot_cumulative_inertia()
fig2, ax2 = ca.plot_rows_columns(show_row_labels=True, show_variable_labels=True)

plt.show()