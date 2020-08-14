# Anti-patrones

## Integrantes 

- Edwin Alejandro Fiesco Parra (20182020108)

- Lindsey Katherine Camargo Beltrán (20172020037)

## Fantasma 

Demasiadas clases en un programa o tablas en una base de datos. Varias clases o tablas con mínimas responsabilidades. Muchas veces se utiliza para disfrazar la presencia del anti-patrón The God. Se colocan clases inútiles, que disfrazan el hecho que todo el sistema se encuentra construido en uno, o unos cuantos archivos, módulos o clases. Este anti-patrón sugiere un modelo de análisis y/o diseño inestable: el diseño no coincide con la implementación, y por ello es imposible hacer extensiones al sistema, porque entre tanto “fantasma”, encontrar los elementos relevantes es imposible.

## Código muerto

Algo así como “programar al estilo volcán”. Es construir grandes cantidades de código de manera desordenada, con poca documentación y poca claridad de su función en el sistema. Conforme el sistema avanza en su desarrollo, y crece, se dice que estos flujos de lava se solidifican, es decir, se vuelve mucho más complicado corregir los problemas que originan, y el desorden va creciendo geométricamente. Esto se hace patente cuando: 

1. Se declaran variables no justificadas. 

2. Se construyen clases o bloques de código muy grandes y complejas sin documentar, o que no se relacionan claramente con la arquitectura. 

3. Usando un inconsistente y difuso estilo de evolución de una arquitectura. 

4. Cuando en el sistema existen muchas áreas con código por terminar o reemplazar. 

5. Y claro, cuando dejamos código sin uso abandonado; interfaces o componentes obsoletos en el cuerpo del sistema. Los resultados son predecibles: conforme los flujos se endurecen y solidifican (se escribe código y pasa el tiempo), rápidamente se vuelve imposible documentar el código o entender su arquitectura lo suficientemente bien como para hacer mejoras.

## Código en espagueti
