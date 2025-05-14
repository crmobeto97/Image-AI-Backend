from fastapi import APIRouter, Form, HTTPException
import config
from utils.image_utils import move_generated_image

router = APIRouter()

@router.post("/")
def detect_objects(token: str = Form(...)):
    try:
        raw_path = config.TEMP_DIR / token / config.RAW_FOLDER
        processed_path = config.TEMP_DIR / token / config.PROCESSED_FOLDER

        results = []

        if not raw_path.exists():
            raise HTTPException(status_code=404, detail="Temp directory not found.")

        for image_path in raw_path.glob("*.jpg"):
            print(f"Processing: {image_path}")

            result = config.MODEL.detect(image_path)

            move_result = move_generated_image(
                original_image_path=image_path,
                generated_filename=config.GENERATED_FILENAME,
                output_dir=processed_path,
                model_working_dir=config.MODEL_WORKING_DIR,
                suffix=config.OUTPUT_SUFFIX
            )

            result.update(move_result)
            results.append(result)

        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar imágenes: {str(e)}")
