# Tesis — Microorganismos

Código fuente LaTeX de la tesis de Licenciatura en Ciencias de la Computación.

## Estado

La rama \`feature/latex-initial-migration\` contiene la primera migración del borrador de Google Docs a LaTeX.

Se trasladaron:

- portada base;
- resumen y abstract;
- capítulos 1 a 4;
- referencias bibliográficas a BibLaTeX/Biber;
- fuentes Mermaid de las Figuras 4.1–4.3;
- configuración inicial para VS Code + LaTeX Workshop.

## Compilación local

Configuración recomendada en Windows:

1. MiKTeX;
2. VS Code;
3. extensión **LaTeX Workshop**.

Abrir este repositorio y compilar \`main.tex\`.

Desde terminal:

\`\`\`bash
latexmk -lualatex main.tex
\`\`\`

La bibliografía utiliza Biber y el estilo numérico IEEE.

## Logos institucionales

Agregar los archivos oficiales:

\`\`\`text
assets/logos/unc.pdf
assets/logos/famaf.pdf
\`\`\`

Mientras no estén presentes, la portada muestra placeholders y el documento sigue siendo compilable.

## Figuras Mermaid

Los fuentes editables están en \`figures/chapter04/\`.

Para generar las versiones PDF vectoriales:

\`\`\`bash
npx -p @mermaid-js/mermaid-cli mmdc -i figures/chapter04/fig04_01_metodologia.mmd -o figures/chapter04/fig04_01_metodologia.pdf
npx -p @mermaid-js/mermaid-cli mmdc -i figures/chapter04/fig04_02_datos_unidades.mmd -o figures/chapter04/fig04_02_datos_unidades.pdf
npx -p @mermaid-js/mermaid-cli mmdc -i figures/chapter04/fig04_03_calibracion.mmd -o figures/chapter04/fig04_03_calibracion.pdf
npx -p @mermaid-js/mermaid-cli mmdc -i figures/chapter04/fig04_04_procedimiento.mmd -o figures/chapter04/fig04_04_procedimiento.pdf
\`\`\`

Si los PDF todavía no existen, LaTeX muestra un placeholder en su lugar.

## Organización

\`\`\`text
main.tex
config/
frontmatter/
chapters/
figures/
assets/
bibliography/
\`\`\`

## Migración

La fuente de contenido es la pestaña **version 2** del Google Docs de trabajo.

Antes de fusionar esta primera migración, revisar \`MIGRATION_NOTES.md\`, especialmente la comparación de ecuaciones con el documento original.


## Si las citas aparecen como claves

Si en el PDF aparece algo como `mader2006` en lugar de `[1]`, significa que Biber no se ejecutó o que quedaron archivos auxiliares de una compilación anterior.

En ese caso:

```bash
biber --version
```

debe responder correctamente. Luego limpiar los archivos auxiliares y recompilar con la receta **LuaLaTeX + Biber + LuaLaTeX x2**.

En VS Code:

1. `Ctrl+Shift+P`;
2. **LaTeX Workshop: Clean up auxiliary files**;
3. **LaTeX Workshop: Build with recipe**;
4. elegir **LuaLaTeX + Biber + LuaLaTeX x2**.

La bibliografía se imprime automáticamente al final del documento mediante `\printbibliography`.
