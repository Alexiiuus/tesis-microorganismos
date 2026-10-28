# Evidencia del capítulo 11

Las fuentes se conservan sin modificar. El autor confirmó que las pruebas corresponden a `primer_minuto.mp4` y que `prueba_traker` es otro video. El campo `video` de `ground_truth.json` conserva el texto original `prueba_tracker.mp4`; no se interpreta como un nombre alternativo del video de prueba.

| Archivo | Fuente en Drive |
|---|---|
| `Track_145.csv` | https://drive.google.com/file/d/14DrfsyfycHRRr2j3C__gff7aN8rCsqvc/view |
| `ground_truth.json` | https://drive.google.com/file/d/1VdYd5gH2abKwyzww-9sGW6XiiQ7SCQZ5/view |
| `run_metadata.json` | https://drive.google.com/file/d/1b_ThoNKzHPOIHy6tq-rz183aDG-gNhez/view |
| `entrenamiento_v1.csv` (carpeta `train2`) | https://drive.google.com/file/d/1gm2NWY6_W7YFaEAd-H4Fc8UJirTQOa_M/view |
| `entrenamiento_v2.csv` (carpeta `train`) | https://drive.google.com/file/d/1pbAcsIthuRlojRKUtKapJ3ETsiINFKIT/view |

## Identificación de datasets y corridas

Los sufijos de los CSV y las claves `v1`/`v2` de `results.json` se conservan por compatibilidad con los archivos ya publicados. Son identificadores históricos, no versiones de Roboflow ni orden cronológico. No se modificaron los CSV originales.

| Corrida | Carpeta conservada | CSV local | Ruta de datos registrada en `args.yaml` |
|---|---|---|---|
| Primera | `train` | `entrenamiento_v2.csv` | `/content/Micro-2/data.yaml` |
| Segunda, pesos usados en la prueba | `train2` | `entrenamiento_v1.csv` | `/content/Micro-4/data.yaml` |

| Exportación | Imágenes train/valid/test | Función |
|---|---|---|
| `Micro.v2-poc_morg_v1.yolov11` | 100 / 6 / 4 | Primer entrenamiento funcional, confirmado por el autor. Incluye aumentos; clase `Morg`. |
| `Micro.v5-poc_morg_v3.yolov11` | 580 / 71 / 34 | Conjunto ampliado conservado con aumentos; clase `E`. |
| `Micro.v6-poc_datasetv1.yolov11` | 58 / 71 / 34 | Imágenes sin aumentar para el uso posterior de sus detecciones; clase `E`. No es el dataset del primer entrenamiento. |

La segunda corrida registra `Micro-4`; esa ruta no demuestra identidad exacta con la exportación `Micro.v5` conservada. Las tablas y curvas identifican los resultados por corrida. La comparación no representa un experimento entre una exportación sin aumentos y otra con aumentos. La composición y los archivos descriptivos consultados se registran en `dataset_sources.json`.

## Reproducción

Se distinguen tres versiones:

- **Software actual:** incorpora correcciones posteriores de presentación y documentación; no es la revisión fijada para reconstruir esta evidencia.
- **Reconstrucción del capítulo 11:** utiliza exactamente `cf1db739a9e22a2201c9bad20ab9baa328194f54`. `provenance.json` conserva las huellas Git de los nueve módulos verificados antes del cálculo.
- **Inferencia original:** su commit exacto no quedó registrado. No se le atribuye el commit de la reconstrucción ni el de la versión actual.

Desde la raíz de la tesis, con Git y acceso de lectura al repositorio del sistema, crear **una copia independiente** (el directorio de destino no debe existir):

```bash
git clone https://github.com/Alexiiuus/Detection-Morg.git ../Detection-Morg-ch11
git -C ../Detection-Morg-ch11 checkout --detach cf1db739a9e22a2201c9bad20ab9baa328194f54
git -C ../Detection-Morg-ch11 rev-parse HEAD
git -C ../Detection-Morg-ch11 status --short
```

El tercer comando debe imprimir el commit indicado y el cuarto no debe mostrar cambios. El estado «detached HEAD» es esperado: la copia queda fijada a una revisión y no modifica la instalación actual. Si Git solicita autenticación, se necesita acceso de lectura al repositorio.

Para el posprocesamiento basta un entorno de Python 3.12 con NumPy, Pandas y Matplotlib; no se requiere instalar YOLO ni PyTorch. Ejemplo en Linux/macOS o Git Bash:

```bash
python3.12 -m venv .venv-ch11
source .venv-ch11/bin/activate
python -m pip install numpy==2.2.6 pandas==2.2.3 matplotlib==3.10.8
python scripts/generate_ch11_results.py --system-root ../Detection-Morg-ch11
```

En Windows puede crearse el entorno con `py -3.12 -m venv .venv-ch11` y activarse desde Git Bash con `source .venv-ch11/Scripts/activate`.

Una falla por diferencia de huellas significa que no se está utilizando exactamente el código documentado; **no demuestra por sí sola una discrepancia científica**. Por ejemplo, una corrección de etiquetas o gráficos también cambia una huella. No se deben reemplazar las huellas históricas para omitir ese control: comprobar la ruta y utilizar la copia fijada al commit anterior.

Genera tres figuras vectoriales en `figures/chapter11/`, las comparaciones por cuadro e intervalo y `results.json`. No ejecuta detección ni seguimiento, no requiere los pesos y no calcula métricas de toda la población del video. El cálculo independiente contrasta rapidez por segmento, distancia acumulada, suavizado, inactividad y variación escalar de rapidez con las funciones del sistema.

`provenance.json` registra la revisión, las huellas y la identificación de las fuentes. La alineación vertical utiliza exclusivamente el primer par de posiciones: `y_aligned = y_model(0) + y_manual(0) - y_manual`. Las métricas de posición posteriores excluyen ese anclaje y conservan X. El contraste de rapidez utiliza los mismos extremos de los intervalos de ambas series y sí utiliza el primer punto como extremo inicial.

La clasificación se calcula con los módulos del sistema desarrollado y sus parámetros predeterminados. Sus salidas no son etiquetas independientes de referencia. La calibración óptica y la conversión a unidades físicas son externas al alcance de la tesis; la evaluación permanece en píxeles.


## Alcance de la identificación histórica

El autor confirmó expresamente primer_minuto.mp4 como video de evaluación. No se realizó una comprobación independiente con el video original, el proyecto de Tracker y los pesos. ground_truth.json conserva su etiqueta histórica incorrecta prueba_tracker.mp4; las coordenadas y los archivos originales no se modifican. provenance.json distingue video_identity, historical_inference y postprocessing. El commit de reconstrucción no identifica la inferencia histórica; los hashes no disponibles del video y pesos permanecen nulos. Los umbrales conservados son 0,4/0,4 y el modelo registrado procede de train2.

## Criterio histórico del punto manual

La metadata conservada en `ground_truth.json` registra video, FPS, método Tracker y `spatial_scale: null`, pero no el criterio del punto seleccionado por el anotador. Tampoco se recuperó esa definición de los demás registros disponibles. No se presupone centro geométrico ni centro de masa. El centro de la caja automática y el punto manual pueden representar referencias distintas: los 5,33 px son una discrepancia después de la alineación, no un error atribuible exclusivamente a detección o seguimiento. Se conservan las posiciones originales; para futuras anotaciones se debe fijar y registrar el criterio antes de comparar.
