# Revisión de edición — RHCD 572/2024

Revisión inicial del borrador escrito (capítulos 1 a 11), sobre la rama `feature/latex-initial-migration`, a partir de `b410bfa6d1a6ecaeaa7a0c4bf47f59bdfb0fbd06`. No se encontraron commits posteriores al iniciar la revisión. Este informe distingue el formato corregible de los trámites propios de una entrega final aprobada.

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
| Art. 4: guarda anterior y posterior | Ausentes. | Preparadas para la entrega final. Por indicación posterior del autor, el borrador se genera sin guardas; `ThesisFinalLayouttrue` incorpora una hoja completa (dos carillas) al principio y otra al final, sin número ni encabezado. |
| Art. 4: última hoja de aval con al menos dos firmas | Ausente. | Se agrega `backmatter/aval_tribunal.tex` después de la bibliografía, antes de la guarda final; incluye tres espacios y advierte que está pendiente. No acredita aprobación ni firmas. |
| Art. 5 / Anexo II: licencia, logo y enlace | Ausentes. | Pendiente de elección del autor. La carátula reserva el bloque mediante `ThesisLicense`; no se aplica una licencia sin esa decisión. La Biblioteca publica CC Atribución 4.0 Internacional como referencia. Una vez definida, incorporar el icono oficial, denominación y enlace. |
| Art. 5: autorización de incorporación al RDU y catálogo | No documentada. | Pendiente de completar y firmar el formulario institucional; no se sustituye por una declaración automática dentro de la tesis. |
| Art. 2: original impreso a doble cara, anillado y tapas provistas por la Facultad | Es un borrador digital. | La clase explicita `twoside`. La impresión, el anillado y las tapas se resuelven en la entrega; no pueden acreditarse desde el PDF. |
| Art. 2: identidad de ejemplar impreso y electrónico, versión final aprobada y declaración jurada | Tesis en desarrollo. | Pendiente del cierre. Imprimir exactamente el PDF final aprobado y cumplimentar la declaración; esta compilación no se presenta como versión final. |
| Art. 2: envío electrónico en el formato indicado por Biblioteca | Salida PDF mediante LuaLaTeX. | El formato coincide con el PDF solicitado en la página de Biblioteca; envío pendiente. No se envió ningún archivo a terceros. |

Los artículos 6 y 7 son disposiciones derogatorias y administrativas, sin ajustes adicionales al manuscrito.

## Decisiones conservadas

Se mantienen los márgenes existentes (interior 30 mm, exterior 25 mm, superior e inferior 25 mm), las citas numéricas, los resultados experimentales y las figuras. La norma solo exige 12 pt para el cuerpo: títulos, pies y ecuaciones conservan su jerarquía tipográfica. Las fórmulas y el código pueden usar fuentes específicas; el texto corrido usa la fuente exigida.

Por indicación del autor, el borrador no incluye guardas ni separadores en blanco. En `config/metadata.tex`, `ThesisFinalLayoutfalse` mantiene esta presentación; al preparar la entrega final, cambiar a `ThesisFinalLayouttrue` para incorporar las guardas y recuperar los inicios en recto. Esa versión final deberá conservar la identidad entre el ejemplar impreso y el electrónico.

## Pendientes de cierre

1. Registrar mes y año oficial de defensa en `config/metadata.tex`.
2. Definir la licencia y completar `ThesisLicense` con icono, nombre y enlace.
3. Obtener el aval de al menos dos integrantes del tribunal y retirar el aviso de hoja pendiente solo cuando corresponda.
4. Completar la autorización institucional y la declaración de fidelidad de las versiones.
5. Actualizar los resúmenes con el trabajo completo y volver a verificar el PDF definitivo antes de imprimir.

## Continuación de la escritura

La tesis comprende doce capítulos y un apéndice. El capítulo 11 integra evaluación experimental, resultados y discusión; su sección 11.10 concentra la interpretación de los resultados, sus aportes y sus limitaciones. El capítulo 12 desarrolla «Conclusiones y trabajo futuro» y el Apéndice A reúne la guía de ejecución y reproducción de resultados. Se descarta el capítulo independiente de discusión.

Por decisión del autor, las preguntas de investigación se eliminaron de los capítulos iniciales para reducir su extensión; no deben recuperarse como requisito para continuar. Se corrigieron los anuncios de apartados de preguntas, objetivos y justificación que no figuran en el capítulo 2. La discusión utiliza la propuesta y el alcance ya escritos, las pruebas y los resultados disponibles. La reducción del tiempo de trabajo sigue pendiente de mediciones comparables.

## Verificación inicial de la adecuación (antes de retirar las páginas en blanco)

- Compilación completa con LuaLaTeX y Biber 2.19: PDF de 96 páginas, incluidas las guardas.
- Sin errores, advertencias de LaTeX, citas o referencias sin resolver, caracteres faltantes ni cajas desbordadas.
- Tamaño A4 comprobado en todas las páginas; Times New Roman embebida y cuerpo nominal de 12 pt.
- Las primeras dos carillas y las últimas dos no contienen texto ni imágenes. La carátula y el aval quedan en recto. Las páginas intermedias de separación tampoco muestran numeración.
- Revisión visual de las 96 páginas mediante hojas de contacto y de las páginas afectadas a mayor escala: carátula, resúmenes, índices, títulos largos, tablas, figuras y aval.
- Ajustes de composición: espacio de números ampliado en el índice, títulos con alineación izquierda para permitir cortes, saltos en identificadores largos y reflujo de un párrafo de coordenadas sin modificar cifras. Se mantiene la alineación izquierda de las tablas largas con espacio flexible a la derecha. Se evita estirar los espacios verticales entre bloques.
- Los valores experimentales y los datos de origen permanecen sin cambios. No se aplicó licencia ni se firmó o envió ningún documento.

El entorno de esta revisión requirió añadir los paquetes de BibLaTeX, LuaLaTeX, español y siunitx, Biber y las fuentes Times New Roman. La compilación se ejecutó en una carpeta temporal limpia para evitar auxiliares incompletos del directorio compartido. En una instalación local completa se utiliza el comando del README.

## Ajuste posterior solicitado por el autor

Se retiran del borrador todas las páginas en blanco, incluidas las guardas y los separadores a recto. El cumplimiento de ese requisito se pospone a la preparación de la entrega final. La configuración queda centralizada en `ThesisFinalLayout`, inicialmente desactivada. El contenido escrito y el resto del formato se conservan.

Verificación de este ajuste: PDF de 90 páginas, sin páginas en blanco, errores ni advertencias de compilación.

## Redacción del cierre y el apéndice

Se incorporaron el capítulo 12 y el Apéndice A. La indicación inicial de calibración pendiente fue sustituida por la decisión del autor del 28/10/2026: evaluación en píxeles y calibración óptica externa al alcance, sin factores ni procedimientos añadidos. La guía se contrastó con los archivos reales del sistema en `cf1db739a9e22a2201c9bad20ab9baa328194f54`: entradas, firma del procesamiento, inspección, guardado, metadatos y verificador de entorno. La ejecución del pipeline requiere pesos y video externos; el apéndice diferencia los ejemplos de uso de la reconstrucción de resultados a partir de posiciones conservadas.

Verificación de esta redacción: compilación LuaLaTeX/Biber de 97 páginas, sin advertencias, referencias pendientes, caracteres faltantes ni cajas desbordadas; sin páginas en blanco. Revisión visual de los capítulos nuevos, índice y referencias cruzadas. Los bloques de código se mantienen completos entre páginas y el encabezado identifica «Apéndice A».

Los argumentos del ejemplo de procesamiento se contrastaron con la firma real, sin ejecutar inferencia sobre videos. Los ejemplos de inspección y exportación se ejecutaron sobre las 929 observaciones conservadas de Track_145: cuatro gráficos y un CSV con correspondencia de filas verificada. Los tres scripts de figuras se ejecutaron en una copia temporal de los datos, con Python 3.12.14, NumPy 2.3.5, Matplotlib 3.10.8 y Pandas 2.2.3; las huellas de los módulos coinciden con la revisión documentada. La reconstrucción reprodujo el error medio de posición, las discrepancias de rapidez y la categoría informados en el capítulo 11. No se modificaron las entradas, resultados ni figuras ya versionados de ese capítulo.
