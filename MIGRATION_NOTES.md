# Notas de migración inicial

Fecha de migración: 18 de septiembre de 2026.

## Alcance

Se migró el contenido redactado hasta el **Capítulo 4 inclusive** desde la pestaña \`version 2\` del Google Docs de trabajo.

La intención de esta rama es establecer la estructura LaTeX y permitir una primera compilación local. No reemplaza todavía la revisión final del contenido.

## Ecuaciones

La API de Google Docs expone las ecuaciones como objetos, pero no devuelve su contenido matemático textual. Por ese motivo:

- se transcribieron a LaTeX las ecuaciones cuya definición se desprende de forma inequívoca de la redacción y de las correcciones ya realizadas;
- antes de fusionar esta rama debe realizarse una comparación visual, ecuación por ecuación, contra el documento fuente;
- cualquier diferencia encontrada debe resolverse tomando el Google Docs como fuente de verdad.

En particular deben auditarse cuidadosamente las ecuaciones del Capítulo 2 y las calibraciones del Capítulo 4.

## Numeración del Capítulo 3

El borrador fuente pasa de la sección **3.2** a la **3.4**. Se preservó esa organización conceptual, pero LaTeX renumerará automáticamente las secciones. Antes de la versión final debe decidirse si falta una sección o si corresponde renumerar el capítulo.

## Figuras

Las Figuras 4.1–4.3 se almacenan como fuentes Mermaid. LaTeX espera sus versiones PDF vectoriales. Mientras no existan, muestra un placeholder para mantener el documento compilable.

## Pendientes de portada

Falta incorporar:

- archivos oficiales de los logos UNC y FAMAF;
- nombre definitivo del director/a;
- mes de presentación.
