from fastapi import APIRouter, File, UploadFile, HTTPException, Query, Form
import subprocess
from pathlib import Path

router = APIRouter()
# Path to the folder containing images
TEMP_DIR =  Path("/temp") 
RAW_FOLDER =  Path("raw") 
PROCESSED_FOLDER =  Path("processed") 

@router.post("/")
def detect_objects(token: str = Form(...)):
    try:
        folder_path = TEMP_DIR / token / RAW_FOLDER
        results = []
        processed_path = TEMP_DIR / token / PROCESSED_FOLDER
        # Ensure the temp directory exists
        if not folder_path.exists():
            print("Temp directory not found.")
            return {"error": "Temp directory not found."}
        
        
        if not processed_path.exists():
            processed_path.mkdir(parents=True, exist_ok=True)
            print(f"Carpeta creada: {processed_path}")

        # Loop through images in the temp folder
        for image_path in folder_path.glob("*.jpg"):  # Adjust for other formats if needed
            print(f"Processing: {image_path}")

            # Command to run YOLO detection
            cmd_red = [
                "./darknet", "detect",
                "cfg/yolov3.cfg", "yolov3.weights",
                str(image_path)
            ]

            # Run the command
            result = subprocess.run(cmd_red, cwd= Path("ia_model/darknet"),capture_output=True, text=True)
            print(result.stdout)
            # Store results
            results.append({
                "filename": image_path.name,
                "stdout": result.stdout,
                "stderr": result.stderr
            })

            image_name_without_ext = image_path.name.removesuffix(".jpg")
            #print(image_name_without_ext)  
            image_processed_name = image_name_without_ext + "-processed.jpg"
            image_processed_path_name = str(processed_path) + "/" + image_processed_name 
            print(image_processed_path_name)
            cmd_move = [
                "mv", "predictions.jpg",
                str(image_processed_path_name)
            ]

            # # Run the command
            result_move = subprocess.run(cmd_move, cwd= Path("ia_model/darknet"),capture_output=True, text=True)
            print(result_move.stdout)

            results.append({
                "processed_filename": image_processed_name,
                "stdout": result_move.stdout,
                "stderr": result_move.stderr
            })
            # # Test case
            # ls = ["ls", "-al"]
            # result = subprocess.run(ls, cwd= Path("app/routes/darknet"),capture_output=True, text=True)
            # print(result.stdout)
            # results.append(result)

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar imagenes: {str(e)}")