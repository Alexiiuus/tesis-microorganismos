# Aplicación de observaciones de dirección del 20/11/2026

Base: `8661f38251e38dc7128bce0ae9981e5015300d38`. Fuente: `Comentarios sobre la versión final de la tesis de ALEXIS_20nov2026.pdf`, tres páginas, sobre la versión del 17/11/2026. SHA-256: `9f7206aaac31085b04b1c0ec7e41a148f977a517949ec8653950b8fa7a98c4bf`.

Se aplican las acciones del análisis `Correcciones_directora_20nov2026.md`:

| Acción | Resolución |
|---|---|
| D20-01 | El nombre Dra. Débora Analía Pedernera ya era correcto; se conserva. |
| D20-02 | Resumen sin citas, nombre de video ni cifras particulares; se adopta la propuesta de dirección, con concordancia corregida y evidencia limitada a un individuo esférico. |
| D20-03 | Se incorpora «y a las configuraciones». |
| D20-04 y D20-05 | Se explica el registro oral de temperatura en 2.2.3 y 2.3.2 y que el procesamiento de imágenes no lo extrae. |
| D20-06 | Se añade una captura real de inspección individual con el ID 145 en el encabezado, referencia cruzada y procedencia. La captura disponible identifica un solo seguimiento; no muestra ID para todos los objetos. |
| D20-07 | Se presentan `n` y `n - 1` en modo matemático en la prosa. |
| D20-08 y D20-09 | Se unifica la definición de rapidez y se explicita la diferencia vectorial/escalar entre las medias, sin cambiar fórmulas. |
| D20-10 | Las etiquetas «datos insuficientes» y «desconocido» se destacan en cursiva. |
| D20-11 | El factor `s` se introduce en modo matemático en 2.3.2. |
| D20-12 | Se desactiva la partición silábica dentro de los cuadros de los diagramas de los capítulos 4 y 5 y de la figura 6.1, con alcance local a sus estilos. Se comprueba la composición de las siete figuras señaladas. |
| D20-13 | Se sustituye «artefactos» por «productos» en 5.7 y en la arquitectura del mismo capítulo. |
| D20-14 | Se reordena la oración inicial de 12.1 y se distingue la detección mediada por el modelo. |
| D20-15 | Se conserva pendiente la medición del ahorro y se expresa la reducción de intervención manual como finalidad, según la formulación propuesta en el análisis. No se agrega una conclusión de eficiencia sin medición. |
| COH-01 | Se alinea el abstract con el resumen revisado. |

## Figura del capítulo 2

La imagen es el cuadro 0 del fragmento de presentación decodificado desde `media_detecciones.mp4.base64.txt`, conservado por el autor. Se mantienen los píxeles de la captura, el encabezado original con el ID y su relación de aspecto. El cuadro del fragmento no se atribuye a un cuadro exacto del video experimental original. La procedencia y las huellas están en `figures/chapter02/fig02_02_provenance.json`.

No se repite inferencia, no se agregan etiquetas sintéticas y no se atribuyen identidades a los demás microorganismos visibles. La figura ilustra el concepto de observaciones por identificador mediante una inspección individual.

## Validación

- Las 37 ecuaciones de bloque de la tesis se conservan exactamente frente a la base.
- Las citas de los capítulos conservan sus claves y secuencia. Se retiran únicamente las citas de resumen y abstract, según el cambio solicitado y su traducción coherente.
- Se conservan los datos experimentales, sus archivos de procedencia y el capítulo 3 ya corregido.
- Se mantienen las cursivas de `pipeline`, `score` y `scores`.
- `git diff --check` correcto.
- Compilación completa con LuaLaTeX, Biber y latexmk: correcta, 108 páginas. Sin errores, referencias o citas indefinidas, caracteres ausentes ni cajas desbordadas.
- El registro conserva tres avisos de cajas con espaciado insuficiente (`Underfull hbox`) en párrafos de los capítulos 6 y 9 y del apéndice; no corresponden a palabras partidas en los diagramas.
- Inspección visual de resumen, abstract, nueva figura, las siete figuras solicitadas y el inicio de las conclusiones: composición legible, cuadros sin particiones silábicas ni solapamientos.
