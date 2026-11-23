# Revisión del capítulo 3 según observaciones de dirección

Fecha: 23/11/2026. Base: `7299b679684a30860b25dc2f551356190297f60f`.

Fuente: `Comentarios sobre la version final de Alexis_parte 2.pdf`, dos páginas, sobre la versión del 17/11/2026. SHA-256 del PDF recibido: `60d4645a06d40a2c9ec17ef2fe5bb9dd42832b74093b543a3f434eda7aded0f0`.

## Cambios aplicados

| Acción | Resultado |
|---|---|
| C3-01 | Se cambia la aparición puntual de «este» por «éste» en 3.2.1, según el pedido editorial. |
| C3-02 | Detección, segmentación y seguimiento se presentan en tres elementos; se conservan sus explicaciones, citas y el párrafo final de 3.3. |
| C3-03 | Se explicita origen superior izquierdo, `x` hacia la derecha e `y` hacia abajo. Se aclara que las esquinas solicitadas corresponden a la alternativa cartesiana con `y` hacia arriba. No se invierten las coordenadas del sistema. |
| C3-04 | La prosa presenta el ancho `w` y el alto `h` en modo matemático. |
| C3-05 | Se incorpora la figura 3.1 con una captura original de cajas azules, referencia cruzada y procedencia. |
| C3-06 | Se aclara TP «por sus siglas en inglés» y se incluye la expresión *true positive*. |
| C3-07 | Se indica expresamente «Un valor elevado de recall…»; recall aparece en cursiva. |
| C3-08 | Se introducen `S`, `D_N` y `D_T` en la oración que define el cociente de rectitud. |
| C3-09 | Se simplifica la frase del rango de `S`, conservando `D_T > 0` en la ecuación. No se afirma positividad estricta de todas las distancias. |
| C3-10 | Se uniforman en la prosa las quince expresiones de la lista: métricas en modo matemático y anglicismos/nombres en cursiva. Los títulos y subtítulos se conservan. |

Se retira además un comentario TODO obsoleto que preguntaba por la existencia de 3.3, sección que ya existe. No se reestructura el resto del capítulo.

## Precisiones de aplicación

- Las esquinas de una caja dependen de la orientación de los ejes. La aclaración de 3.4.1 distingue las dos convenciones y conserva la utilizada por el procesamiento de imágenes.
- `D_N` y `D_T` son no negativos. Un recorrido de ida y vuelta puede tener `D_N = 0`; una trayectoria estacionaria puede tener `D_T = 0`. Se mantiene la condición de definición del índice y la distinción entre rectitud y continuidad temporal.
- Se conserva la grafía `ByteTrack`; la lista de la directora lo menciona como «Byte Track».

## Figura y procedencia

`figures/chapter03/fig03_01_cajas_delimitadoras.png` es una copia byte a byte de `image.png`, imagen proporcionada por el autor y conservada como apoyo del póster. Muestra varias cajas delimitadoras azules sobre el material microscópico.

Se mantiene su resolución nativa de 147 × 127 píxeles y se inserta a un cuarto del ancho de texto, sin alterar los píxeles ni aplicar una mejora sintética. Se descartaron para esta finalidad el video y la imagen de presentación recuperados con nombres alusivos a detecciones: visualmente mostraban una estela del Track 145, sin las cajas necesarias para esta explicación.

La imagen no conserva identificación verificable del video original, número de cuadro ni commit de inferencia; estos campos quedan nulos en `fig03_01_provenance.json`. No se atribuye a una corrida específica ni se presenta como evidencia cuantitativa adicional. Su propósito es ilustrar la diferencia entre caja rectangular y contorno.

## Verificación

- Las 11 ecuaciones de bloque son idénticas a las de la base.
- Los 31 títulos y subtítulos son idénticos y conservan su orden.
- Las 57 llamadas de cita conservan claves y secuencia.
- Se comprueba que las quince expresiones indicadas y recall no quedan sin el formato acordado en la prosa.
- Las siete huellas de entradas experimentales del capítulo 11 siguen coincidiendo. Sus datos, resultados, fórmulas y procedencia no se modifican.
- No se modifica Detection-Morg, no se repite inferencia y no se reentrena el detector.
- Compilación completa con LuaLaTeX y Biber mediante latexmk: correcta, 106 páginas. El registro final no contiene advertencias de LaTeX, referencias o citas indefinidas, caracteres ausentes ni cajas desbordadas.
- Inspección visual del PDF: lista de tareas (página física 31), coordenadas y figura (32), índice de rectitud (39) y cursivas de herramientas (42). La figura permanece legible al tamaño elegido y los títulos mantienen su formato.
