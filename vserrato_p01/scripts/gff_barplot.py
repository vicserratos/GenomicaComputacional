#!/home/serrato/programs/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Crea el dataset con << tus datos obtenidos en barplot_data.txt >>
frecuencias = [13, 1, 1, 11, 27, 5]
categorias = ['CDS', 'five_prime_UTR', 'three_prime_UTR', 'gene', 'mature_protein_region_of_CDS', 'stem_loop']
categorias = [ '\n'.join(wrap(l, 11)) for l in categorias]

y_pos = np.arange(len(categorias))

# Gráfico de barras
plt.bar(y_pos, frecuencias)

# Nombres en el eje-x
plt.xticks(y_pos, categorias)

# Mostrar la gráfica
plt.show()
