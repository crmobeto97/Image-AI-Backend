# utils/image_utils.py

from pathlib import Path
import shutil

def move_generated_image(
    original_image_path: Path,
    generated_filename: str,
    output_dir: Path,
    model_working_dir: Path,
    suffix: str = "-processed"
) -> dict:
    """
    Mueve una imagen generada por un modelo IA a una carpeta de destino,
    renombrándola con base en la imagen original.

    Parámetros:
    - original_image_path: ruta de la imagen que se procesó
    - generated_filename: nombre del archivo generado por el modelo (ej. "predictions.jpg")
    - output_dir: carpeta de destino para mover la imagen generada
    - model_working_dir: carpeta donde se encuentra el archivo generado
    - suffix: sufijo para renombrar la imagen de salida

    Retorna:
    - dict con información del movimiento
    """
    try:
        image_name_without_ext = original_image_path.stem
        output_filename = f"{image_name_without_ext}{suffix}.jpg"
        output_path = output_dir / output_filename

        # Asegura que la carpeta de salida existe
        output_dir.mkdir(parents=True, exist_ok=True)

        # Ruta completa del archivo generado por el modelo
        source_path = model_working_dir / generated_filename

        if not source_path.exists():
            return {
                "processed_filename": None,
                "error": f"{generated_filename} not found in {model_working_dir}"
            }

        # Usamos shutil en lugar de subprocess para portabilidad
        shutil.move(str(source_path), str(output_path))

        return {
            "processed_filename": output_filename,
            "output_path": str(output_path)
        }

    except Exception as e:
        return {
            "processed_filename": None,
            "error": str(e)
        }
