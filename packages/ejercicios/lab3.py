import json
import os
from typing import Any, Dict

class ConfigManager:
    def __init__(self, archivo_config: str = "config.json"):
        self.archivo_config = archivo_config
        if os.path.exists(self.archivo_config):
            with open(self.archivo_config, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def get(self, clave: str, default: Any = None) -> Any:
        partes = clave.split(".")
        valor = self.config
        for parte in partes:
            if isinstance(valor, dict) and parte in valor:
                valor = valor[parte]
            else:
                return default
        return valor

    def set(self, clave: str, valor: Any) -> None:
        partes = clave.split(".")
        ref = self.config
        for parte in partes[:-1]:
            if parte not in ref or not isinstance(ref[parte], dict):
                ref[parte] = {}
            ref = ref[parte]
        ref[partes[-1]] = valor

    def save(self) -> None:
        with open(self.archivo_config, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def load_from_env(self, mapeo: Dict[str, str]) -> None:
        for env_var, clave_config in mapeo.items():
            valor = os.getenv(env_var)
            if valor is not None:
                self.set(clave_config, valor)
