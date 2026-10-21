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

Se utilizó el sistema en la revisión `cf1db739a9e22a2201c9bad20ab9baa328194f54`. La revisión de la ejecución histórica no consta en sus metadatos. El script verifica las huellas Git de los nueve módulos utilizados antes de ejecutar el posprocesamiento.

Con Python, NumPy, Pandas y Matplotlib disponibles, ejecutar desde la raíz de esta tesis:

```bash
python scripts/generate_ch11_results.py --system-root /ruta/al/sistema
```

Genera tres figuras vectoriales en `figures/chapter11/`, las comparaciones por cuadro e intervalo y `results.json`. No ejecuta detección ni seguimiento, no requiere los pesos y no calcula métricas de toda la población del video. El cálculo independiente contrasta rapidez por segmento, distancia acumulada, suavizado, inactividad y variación escalar de rapidez con las funciones del sistema.

`provenance.json` registra la revisión, las huellas y la identificación de las fuentes. La alineación vertical utiliza exclusivamente el primer par de posiciones: `y_aligned = y_model(0) + y_manual(0) - y_manual`. Las métricas de posición posteriores excluyen ese anclaje y conservan X. El contraste de rapidez utiliza los mismos extremos de los intervalos de ambas series y sí utiliza el primer punto como extremo inicial.

La clasificación se calcula con los módulos del sistema desarrollado y sus parámetros predeterminados. Sus salidas no son etiquetas independientes de referencia. La escala física permanece **A DEFINIR**.
