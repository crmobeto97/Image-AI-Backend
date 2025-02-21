from fastapi import APIRouter, File, UploadFile, HTTPException, Query, Form
import os
from pathlib import Path
from typing import List
import uuid

router = APIRouter()

TEMP_DIR =  Path("/temp") 
TEMP_DIR.mkdir(parents=True, exist_ok=True)  

@router.get("/")
async def check_folder(uuid: str = Query(..., title="UUID de la carpeta")):
    try:
        folder_path = TEMP_DIR / uuid  
 
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            return {"message": "Carpeta creada", "files": []}

        image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
        image_files = [
            file.name for file in folder_path.iterdir()
            if file.is_file() and file.suffix.lower() in image_extensions
        ]

        return {"status": True, "message": "Carpeta encontrada", "data": image_files}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al verificar carpeta: {str(e)}")

@router.post("/")
async def upload_file(token: str = Form(...), files: List[UploadFile] = File(...)):
    try:

        folder_path = TEMP_DIR / token  

        for file in files: 
            file_extension = file.filename.split(".")[-1]
            new_filename = f"{uuid.uuid4()}.{file_extension}"  # Generar un nuevo nombre único
            file_location = folder_path / new_filename  # Ruta con el nuevo nombre
            with open(file_location, "wb") as file_object:
                file_object.write(await file.read()) 

        return {"message": "Archivos guardados exitosamente"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar archivo: {str(e)}")