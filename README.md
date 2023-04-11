# Diagrama-de-Voronoi-Tesis
Este programa te permite calcular los diagramas de Voronoi, el cual fue utilizado para generar los diagramas MW usados en la tesis de nombre "Una aplicación de los diagramas de Voronoi en análisis de patrones de conducta"

Autor: Brenda Zarahi Medina Pérez

Diagramas de Voronoi

Dado un conjunto finito de n puntos (x_1,y_1 ),(x_2,y_2 ),…, (x_n,y_n) en el plano, un diagrama de Voronoi es una división de éste en n regiones, a los n puntos se les conoce como generadores. Cabe destacar que a cada región le corresponde un único generador. Las regiones están compuestas por aquellos puntos que se encuentran más cercanos a algún generador, estas regiones reciben el nombre de polígonos de Voronoi.

aristas.png

En la figura anterior se muestran los polígonos de Voronoi de cuatro puntos en el plano, estos se identifican por diferentes colores.

En el caso anterior, los generadores se encuentran uniformemente ponderados; es decir, todos tienen el mismo valor o peso. Si a éstos se les asigna diferente valor o peso, entonces se pueden generar diagramas de Voronoi ponderados. En este programa se consideran los diagramas de Voronoi ponderados multiplicativamente.
