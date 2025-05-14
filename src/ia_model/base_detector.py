from pathlib import Path
from abc import ABC, abstractmethod
from typing import Dict

class BaseDetector(ABC):
    @abstractmethod
    def detect(self, image_path: Path) -> Dict:
        """
        Ejecuta la detección en la imagen especificada.
        Debe devolver un diccionario con resultados (puede incluir logs, nombre, etc.).
        """
        pass