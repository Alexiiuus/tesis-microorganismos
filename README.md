# Tesis — Microorganismos

Código LaTeX del Trabajo Especial de Licenciatura en Ciencias de la Computación. La rama `feature/latex-initial-migration` contiene el borrador con resumen, abstract y capítulos 1 a 12 y un apéndice. El capítulo 11 integra la evaluación experimental, los resultados y su discusión; el 12 reúne las conclusiones y el trabajo futuro. El Apéndice A documenta ejecución, inspección, formatos y reproducción de resultados. La calibración espacial y la conversión a unidades físicas permanecen **A DEFINIR**.

## Compilación

Requiere LuaLaTeX, Biber, BibLaTeX, soporte de español (incluidos sus patrones de separación de palabras), siunitx y Times New Roman o Arial instaladas legalmente en el sistema. Se prioriza Times New Roman. La compilación falla si faltan ambas fuentes, para evitar una sustitución que incumpla la RHCD 572/2024.

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

En Windows puede usarse MiKTeX, VS Code y LaTeX Workshop con la receta **LuaLaTeX + Biber + LuaLaTeX x2**. Si las citas aparecen como claves, comprobar `biber --version`, limpiar auxiliares y recompilar. El estilo bibliográfico es numérico, con orden de aparición.

## Formato y entrega

A4, cuerpo de 12 pt, espacio simple y preparación a doble cara. El borrador incluye la carátula del Anexo II y una hoja de aval pendiente de firma, sin guardas ni páginas de separación en blanco. Para preparar la entrega final, cambiar `\ThesisFinalLayoutfalse` por `\ThesisFinalLayouttrue` en `config/metadata.tex`; esto incorpora las guardas y restablece los inicios en recto. La fecha de defensa y la licencia se completan en `config/metadata.tex` antes de la entrega final. El borrador no acredita aprobación del tribunal ni autorización para su depósito.

La matriz de requisitos, cambios y pendientes está en [docs/REVISION_FORMATO_RHCD_572_2024.md](docs/REVISION_FORMATO_RHCD_572_2024.md).

Los logos usados son `assets/logos/unc.png` y `assets/logos/famaf.png`. Las figuras PDF están versionadas; se conservan fuentes Mermaid y scripts de generación donde corresponde.

## Organización

- `main.tex`: orden de lectura.
- `config/`: metadatos, paquetes y comandos.
- `frontmatter/`: carátula y resúmenes.
- `chapters/`: capítulos 1 a 12.
- `appendices/`: guía de ejecución y reproducción de resultados.
- `backmatter/`: hoja de aval del tribunal.
- `bibliography/`: referencias BibLaTeX.
- `figures/`, `data/` y `scripts/`: figuras y respaldo reproducible.
- `docs/`: revisión de requisitos editoriales.

La procedencia y los límites de los resultados experimentales están documentados en `data/chapter11/README.md` y `data/chapter11/provenance.json`. La información histórica de la migración se conserva en `MIGRATION_NOTES.md`.
