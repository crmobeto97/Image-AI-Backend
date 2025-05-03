from fastapi import APIRouter, File, UploadFile, HTTPException, Query, Form
from fastapi.responses import FileResponse
import os
from pathlib import Path
from typing import List
import uuid

router = APIRouter()

TEMP_DIR =  Path("/temp") 
RAW_FOLDER =  Path("raw") 
PROCESSED_FOLDER =  Path("processed") 
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

@router.get("/raw")
async def check_folder(uuid: str = Query(..., title="UUID de la carpeta")):
    try:
        folder_path = TEMP_DIR / uuid / RAW_FOLDER 
 
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

@router.post("/raw")
async def upload_file(token: str = Form(...), files: List[UploadFile] = File(...)):
    try:

        folder_path = TEMP_DIR / token / RAW_FOLDER 

        for file in files: 
            file_extension = file.filename.split(".")[-1]
            new_filename = f"{uuid.uuid4()}.{file_extension}"  # Generar un nuevo nombre único
            print(folder_path)
            file_location = folder_path / new_filename  # Ruta con el nuevo nombre
            with open(file_location, "wb") as file_object:
                file_object.write(await file.read()) 

        return {"message": "Archivos guardados exitosamente"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar archivo: {str(e)}")

@router.get("/file")
async def get_image_file(uuid: str = Query(..., title="UUID de la carpeta"), status_process: bool = Query(..., title="false = raw, true = processed") , filename: str = Query(..., title="nombre del archivo")):
    try:
        folder = RAW_FOLDER
        if status_process:
            folder = PROCESSED_FOLDER
        
        file_path = TEMP_DIR / uuid / folder / filename

        if not file_path.exists() or not file_path.is_file():
            raise HTTPException(status_code=404, detail="Archivo no encontrado")

        return FileResponse(
            path=file_path,
            media_type="image/jpeg",
            filename=filename
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener archivo: {str(e)}")

@router.get("/processed")
async def check_folder(uuid: str = Query(..., title="UUID de la carpeta")):
    try:
        folder_path = TEMP_DIR / uuid / PROCESSED_FOLDER 
 
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

# @router.post("/processed")
# async def upload_file(token: str = Form(...), files: List[UploadFile] = File(...)):
#     try:

#         folder_path = TEMP_DIR / token / PROCESSED_FOLDER 

#         for file in files: 
#             file_extension = file.filename.split(".")[-1]
#             new_filename = f"{uuid.uuid4()}.{file_extension}"  # Generar un nuevo nombre único
#             print(folder_path)
#             file_location = folder_path / new_filename  # Ruta con el nuevo nombre
#             with open(file_location, "wb") as file_object:
#                 file_object.write(await file.read()) 

#         return {"message": "Archivos guardados exitosamente"}
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error al guardar archivo: {str(e)}")