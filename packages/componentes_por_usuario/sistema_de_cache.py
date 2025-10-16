# archivo: cache_manager.py
from typing import Any, Optional
from datetime import datetime, timedelta
import threading
from collections import OrderedDict

class CacheItem:
    """Elemento individual del cache."""
    
    def __init__(self, value: Any, ttl_seconds: Optional[int] = None):
        self.value = value
        self.created_at = datetime.now()
        self.expires_at = None
        if ttl_seconds:
            self.expires_at = self.created_at + timedelta(seconds=ttl_seconds)
    
    def is_expired(self) -> bool:
        """Verifica si el elemento ha expirado."""
        if self.expires_at is None:
            return False
        return datetime.now() > self.expires_at

class CacheManager:
    """Gestor de cache thread-safe con TTL y límite de tamaño."""
    
    def __init__(self, max_size: int = 1000, default_ttl: Optional[int] = None):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._cache = OrderedDict()
        self._lock = threading.RLock()
        self._hits = 0
        self._misses = 0
    
    def get(self, key: str) -> Optional[Any]:
        """Obtiene un valor del cache."""
        with self._lock:
            if key not in self._cache:
                self._misses += 1
                return None
            
            item = self._cache[key]
            
            # Verificar expiración
            if item.is_expired():
                del self._cache[key]
                self._misses += 1
                return None
            
            # Mover al final (LRU)
            self._cache.move_to_end(key)
            self._hits += 1
            return item.value
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Establece un valor en el cache."""
        with self._lock:
            # Usar TTL específico o por defecto
            ttl_to_use = ttl if ttl is not None else self.default_ttl
            
            # Crear nuevo item
            item = CacheItem(value, ttl_to_use)
            
            # Si la clave ya existe, actualizarla
            if key in self._cache:
                self._cache[key] = item
                self._cache.move_to_end(key)
                return
            
            # Si el cache está lleno, remover el más antiguo
            if len(self._cache) >= self.max_size:
                self._cache.popitem(last=False)  # Remover el primero (más antiguo)
            
            self._cache[key] = item
    
    def delete(self, key: str) -> bool:
        """Elimina una clave del cache."""
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                return True
            return False
    
    def clear(self) -> None:
        """Limpia todo el cache."""
        with self._lock:
            self._cache.clear()
    
    def size(self) -> int:
        """Retorna el tamaño actual del cache."""
        with self._lock:
            return len(self._cache)
    
    def get_stats(self) -> dict:
        """Obtiene estadísticas del cache."""
        with self._lock:
            total_requests = self._hits + self._misses
            hit_rate = (self._hits / total_requests * 100) if total_requests > 0 else 0
            
            return {
                'hits': self._hits,
                'misses': self._misses,
                'total_requests': total_requests,
                'hit_rate_percent': round(hit_rate, 2),
                'current_size': len(self._cache),
                'max_size': self.max_size
            }
    
    def cleanup_expired(self) -> int:
        """Limpia elementos expirados y retorna la cantidad eliminada."""
        with self._lock:
            expired_keys = []
            for key, item in self._cache.items():
                if item.is_expired():
                    expired_keys.append(key)
            
            for key in expired_keys:
                del self._cache[key]
            
            return len(expired_keys)