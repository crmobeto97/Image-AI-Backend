from pathlib import Path
import subprocess
from typing import Dict
from ia_model.base_detector import BaseDetector

class DarknetDetector(BaseDetector):
    def detect(self, image_path: Path) -> Dict:
        cmd = [
            "./darknet", "detect",
            "cfg/yolov3.cfg", "yolov3.weights",
            str(image_path)
        ]

        result = subprocess.run(
            cmd,
            cwd=Path("ia_model/darknet"),
            capture_output=True,
            text=True
        )

        return {
            "filename": image_path.name,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

