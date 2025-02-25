from fastapi import APIRouter, File, UploadFile, HTTPException, Query, Form
import subprocess
from pathlib import Path

router = APIRouter()
# Path to the folder containing images
TEMP_DIR =  Path("/temp") 

@router.post("/")
def detect_objects(token: str = Form(...)):
    try:
        folder_path = TEMP_DIR / token  
        results = []

        # Ensure the temp directory exists
        if not folder_path.exists():
            print("Temp directory not found.")
            return {"error": "Temp directory not found."}

        # Loop through images in the temp folder
        for image_path in folder_path.glob("*.jpg"):  # Adjust for other formats if needed
            print(f"Processing: {image_path}")

            # Command to run YOLO detection
            cmd = [
                "./darknet", "detect",
                "cfg/yolov3.cfg", "yolov3.weights",
                str(image_path)
            ]

            # Run the command
            result = subprocess.run(cmd, cwd= Path("ia_model/darknet"),capture_output=True, text=True)
            print(result.stdout)
            # Store results
            results.append({
                "filename": image_path.name,
                "stdout": result.stdout,
                "stderr": result.stderr
            })

            
            # # Test case
            # ls = ["ls", "-al"]
            # result = subprocess.run(ls, cwd= Path("app/routes/darknet"),capture_output=True, text=True)
            # print(result.stdout)
            # results.append(result)

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar imagenes: {str(e)}")