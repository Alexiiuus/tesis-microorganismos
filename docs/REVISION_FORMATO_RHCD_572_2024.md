# Revisión de edición — RHCD 572/2024

Revisión del borrador escrito (capítulos 1 a 11), sobre la rama `feature/latex-initial-migration`, a partir de `b410bfa6d1a6ecaeaa7a0c4bf47f59bdfb0fbd06`. No se encontraron commits posteriores al iniciar la revisión. Este informe distingue el formato corregible de los trámites propios de una entrega final aprobada.

## Fuentes

- RHCD-2024-572-E-UNC-DEC#FAMAF, artículos 1 a 7 y anexos I y II: copia íntegra aportada por el autor. [Copia publicada por FAMAF](https://www.famaf.unc.edu.ar/documents/5172/RHCD-2024-572-E-UNC-DECFAMAF.pdf).
- [Biblioteca FAMAF: presentación de trabajos finales](https://www.famaf.unc.edu.ar/la-facultad/institucional/areas-y-departamentos/biblioteca/), apartados de grado, licencia y autorización.
- [Modelo de aval del tribunal](https://www.famaf.unc.edu.ar/documents/567/Sugerencia_para_firma_de_Tribunal.pdf).
- [Formulario de autorización para el RDU](https://www.famaf.unc.edu.ar/documents/532/Formulario_de_autorizaci%C3%B3n_RDU_imprimir_las_dos_p%C3%A1ginas_en_una_sola_hoja_si_es_posible.pdf).

El Anexo II corresponde a la Licenciatura. El Anexo I corresponde a Profesorados y no se aplica a este trabajo. La resolución no fija márgenes, estilo bibliográfico, extensión, tamaño de títulos ni número de capítulos; no se introdujeron obligaciones sobre esos puntos.

## Matriz de cumplimiento

| Requisito | Evidencia inicial | Estado y ajuste |
| --- | --- | --- |
| Art. 1: papel IRAM A4 | `main.tex` y `geometry` ya usan A4. | Conservado. |
| Art. 1: cuerpo de 12 pt | Clase `book` en 11 pt. | Corregido a 12 pt. |
| Art. 1: Arial o Times New Roman | Paquete `libertinus`. | Reemplazado por `fontspec`: Times New Roman; Arial solo si la primera no está instalada. La compilación se detiene si faltan ambas; no hay sustitución silenciosa. |
| Art. 1: espacio simple | `setstretch{1.18}`. | Corregido con `singlespacing`. |
| Art. 1: castellano, estilo especializado | Capítulos escritos en castellano, ecuaciones, referencias y terminología técnica. | Se conserva. La revisión editorial integral excede esta comprobación de formato. |
| Art. 1: resumen castellano e inglés | `frontmatter/resumen.tex` y `frontmatter/abstract.tex`. | Presentes e incluidos. Su actualización con los resultados definitivos queda para el cierre de la escritura. |
| Arts. 2 y 3 / Anexo II: carátula | Logos, título, autor y dirección presentes; el grado se expresaba como carrera. Faltaba la licencia y la fecha era provisional. | Ajustada la presentación y la denominación a “Licenciado en Ciencias de la Computación”, conservando título y nombres registrados. La fecha se declara pendiente de la defensa oficial. |
| Art. 4: guarda anterior y posterior | Ausentes. | Se agrega una hoja completa en blanco al principio y otra al final: dos carillas por hoja, sin número ni encabezado. La carátula se mantiene en recto. |
| Art. 4: última hoja de aval con al menos dos firmas | Ausente. | Se agrega `backmatter/aval_tribunal.tex` después de la bibliografía, antes de la guarda final; incluye tres espacios y advierte que está pendiente. No acredita aprobación ni firmas. |
| Art. 5 / Anexo II: licencia, logo y enlace | Ausentes. | Pendiente de elección del autor. La carátula reserva el bloque mediante `ThesisLicense`; no se aplica una licencia sin esa decisión. La Biblioteca publica CC Atribución 4.0 Internacional como referencia. Una vez definida, incorporar el icono oficial, denominación y enlace. |
| Art. 5: autorización de incorporación al RDU y catálogo | No documentada. | Pendiente de completar y firmar el formulario institucional; no se sustituye por una declaración automática dentro de la tesis. |
| Art. 2: original impreso a doble cara, anillado y tapas provistas por la Facultad | Es un borrador digital. | La clase explicita `twoside`. La impresión, el anillado y las tapas se resuelven en la entrega; no pueden acreditarse desde el PDF. |
| Art. 2: identidad de ejemplar impreso y electrónico, versión final aprobada y declaración jurada | Tesis en desarrollo. | Pendiente del cierre. Imprimir exactamente el PDF final aprobado y cumplimentar la declaración; esta compilación no se presenta como versión final. |
| Art. 2: envío electrónico en el formato indicado por Biblioteca | Salida PDF mediante LuaLaTeX. | El formato coincide con el PDF solicitado en la página de Biblioteca; envío pendiente. No se envió ningún archivo a terceros. |

Los artículos 6 y 7 son disposiciones derogatorias y administrativas, sin ajustes adicionales al manuscrito.

## Decisiones conservadas

Se mantienen los márgenes existentes (interior 30 mm, exterior 25 mm, superior e inferior 25 mm), las citas numéricas, los resultados experimentales y las figuras. La norma solo exige 12 pt para el cuerpo: títulos, pies y ecuaciones conservan su jerarquía tipográfica. Las fórmulas y el código pueden usar fuentes específicas; el texto corrido usa la fuente exigida.

Las hojas en blanco insertadas por `cleardoublepage` permiten mantener el comienzo de las secciones preliminares y el aval en recto. No deben eliminarse al preparar la impresión a doble cara. Las guardas completas forman parte de este mismo PDF, para conservar la identidad entre la copia electrónica y la impresa.

## Pendientes de cierre

1. Registrar mes y año oficial de defensa en `config/metadata.tex`.
2. Definir la licencia y completar `ThesisLicense` con icono, nombre y enlace.
3. Obtener el aval de al menos dos integrantes del tribunal y retirar el aviso de hoja pendiente solo cuando corresponda.
4. Completar la autorización institucional y la declaración de fidelidad de las versiones.
5. Actualizar los resúmenes con el trabajo completo y volver a verificar el PDF definitivo antes de imprimir.

## Continuación de la escritura

Los capítulos 12 (discusión) y 13 (conclusiones y trabajo futuro) siguen pendientes; su ausencia no se atribuye a una exigencia de esta resolución. El capítulo 2 anuncia objetivos y preguntas, pero todavía no contiene apartados que los formalicen. Antes de evaluar su cumplimiento en el capítulo 12, recuperar su formulación aprobada de las fuentes del proyecto y validarla con el autor, sin reconstruirla a partir de los resultados.

Esquema propuesto para el capítulo 12: relación con los objetivos; interpretación del detector y seguimiento; confiabilidad de las magnitudes; alcance de la clasificación; aportes al trabajo experimental; limitaciones y validez. Usar un cuadro de objetivo, evidencia, alcance y pendiente, una vez verificados los objetivos. Evitar duplicar la discusión de 11.10 y no cuantificar ahorro de tiempo sin mediciones comparables.

## Verificación de la versión corregida

- Compilación completa con LuaLaTeX y Biber 2.19: PDF de 96 páginas, incluidas las guardas.
- Sin errores, advertencias de LaTeX, citas o referencias sin resolver, caracteres faltantes ni cajas desbordadas.
- Tamaño A4 comprobado en todas las páginas; Times New Roman embebida y cuerpo nominal de 12 pt.
- Las primeras dos carillas y las últimas dos no contienen texto ni imágenes. La carátula y el aval quedan en recto. Las páginas intermedias de separación tampoco muestran numeración.
- Revisión visual de las 96 páginas mediante hojas de contacto y de las páginas afectadas a mayor escala: carátula, resúmenes, índices, títulos largos, tablas, figuras y aval.
- Ajustes de composición: espacio de números ampliado en el índice, títulos con alineación izquierda para permitir cortes, saltos en identificadores largos y reflujo de un párrafo de coordenadas sin modificar cifras. Se mantiene la alineación izquierda de las tablas largas con espacio flexible a la derecha. Se evita estirar los espacios verticales entre bloques.
- Los valores experimentales y los datos de origen permanecen sin cambios. No se aplicó licencia ni se firmó o envió ningún documento.

El entorno de esta revisión requirió añadir los paquetes de BibLaTeX, LuaLaTeX, español y siunitx, Biber y las fuentes Times New Roman. La compilación se ejecutó en una carpeta temporal limpia para evitar auxiliares incompletos del directorio compartido. En una instalación local completa se utiliza el comando del README.
