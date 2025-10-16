# archivo: usuario_manager.py
from datetime import datetime
from typing import List, Optional
import json

class Usuario:
    """Componente que representa un usuario del sistema."""
    
    def __init__(self, id_usuario: int, nombre: str, email: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.fecha_creacion = datetime.now()
        self.activo = True
        self.ultimo_acceso = None
    
    def activar(self):
        """Activa el usuario."""
        self.activo = True
    
    def desactivar(self):
        """Desactiva el usuario."""
        self.activo = False
    
    def registrar_acceso(self):
        """Registra el último acceso del usuario."""
        self.ultimo_acceso = datetime.now()
    
    def to_dict(self) -> dict:
        """Convierte el usuario a diccionario para serialización."""
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'email': self.email,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'activo': self.activo,
            'ultimo_acceso': self.ultimo_acceso.isoformat() if self.ultimo_acceso else None
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crea un usuario desde un diccionario."""
        usuario = cls(data['id_usuario'], data['nombre'], data['email'])
        usuario.fecha_creacion = datetime.fromisoformat(data['fecha_creacion'])
        usuario.activo = data['activo']
        if data['ultimo_acceso']:
            usuario.ultimo_acceso = datetime.fromisoformat(data['ultimo_acceso'])
        return usuario
    
    def __str__(self):
        return f"Usuario({self.id_usuario}, {self.nombre}, {self.email})"

class GestorUsuarios:
    """Componente para gestionar múltiples usuarios."""
    
    def __init__(self):
        self.usuarios: dict[int, Usuario] = {}
        self.proximo_id = 1
    
    def crear_usuario(self, nombre: str, email: str) -> Usuario:
        """Crea un nuevo usuario."""
        if self.buscar_por_email(email):
            raise ValueError(f"Ya existe un usuario con el email {email}")
        
        usuario = Usuario(self.proximo_id, nombre, email)
        self.usuarios[self.proximo_id] = usuario
        self.proximo_id += 1
        return usuario
    
    def obtener_usuario(self, id_usuario: int) -> Optional[Usuario]:
        """Obtiene un usuario por su ID."""
        return self.usuarios.get(id_usuario)
    
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """Busca un usuario por su email."""
        for usuario in self.usuarios.values():
            if usuario.email == email:
                return usuario
        return None
    
    def listar_usuarios_activos(self) -> List[Usuario]:
        """Lista todos los usuarios activos."""
        return [u for u in self.usuarios.values() if u.activo]
    
    def eliminar_usuario(self, id_usuario: int) -> bool:
        """Elimina un usuario del sistema."""
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            return True
        return False
    
    def guardar_en_archivo(self, nombre_archivo: str):
        """Guarda todos los usuarios en un archivo JSON."""
        datos = {
            'usuarios': [u.to_dict() for u in self.usuarios.values()],
            'proximo_id': self.proximo_id
        }
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
    
    def cargar_desde_archivo(self, nombre_archivo: str):
        """Carga usuarios desde un archivo JSON."""
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                
            self.usuarios.clear()
            for usuario_data in datos['usuarios']:
                usuario = Usuario.from_dict(usuario_data)
                self.usuarios[usuario.id_usuario] = usuario
            
            self.proximo_id = datos['proximo_id']
        except FileNotFoundError:
            print(f"Archivo {nombre_archivo} no encontrado. Iniciando con lista vacía.")