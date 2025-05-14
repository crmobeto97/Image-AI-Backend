from pathlib import Path
from ia_model.darknet_detector import DarknetDetector  # Sustituye por otro si cambias el modelo

# Carpetas de imágenes
TEMP_DIR = Path("/temp")
RAW_FOLDER = Path("raw")
PROCESSED_FOLDER = Path("processed")

# Modelo de detección actual (injección)
MODEL = DarknetDetector()

# Config del modelo
GENERATED_FILENAME = "predictions.jpg"            # Archivo que genera el modelo
MODEL_WORKING_DIR = Path("ia_model/darknet")      # Directorio de ejecución del modelo
OUTPUT_SUFFIX = "-processed"                      # Sufijo para las imágenes generadas
