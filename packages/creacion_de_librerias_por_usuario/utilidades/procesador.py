"""Módulo para procesamiento de datos."""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Union
import json

class ProcesadorDatos:
    """Clase para procesamiento avanzado de datos."""
    
    def __init__(self):
        self.historial_operaciones = []
    
    def cargar_csv(self, archivo: str, **kwargs) -> pd.DataFrame:
        """
        Carga datos desde un archivo CSV.
        
        Args:
            archivo: Ruta del archivo CSV
            **kwargs: Argumentos adicionales para pandas.read_csv
            
        Returns:
            DataFrame con los datos
        """
        try:
            df = pd.read_csv(archivo, **kwargs)
            self.historial_operaciones.append(f"Cargado CSV: {archivo}")
            return df
        except Exception as e:
            raise ValueError(f"Error al cargar CSV: {str(e)}")
    
    def limpiar_datos(self, df: pd.DataFrame, 
                     eliminar_duplicados: bool = True,
                     llenar_nulos: Union[str, Dict] = 'mean') -> pd.DataFrame:
        """
        Limpia un DataFrame eliminando duplicados y tratando valores nulos.
        
        Args:
            df: DataFrame a limpiar
            eliminar_duplicados: Si eliminar filas duplicadas
            llenar_nulos: Estrategia para llenar nulos ('mean', 'median', 'mode', 0, dict)
            
        Returns:
            DataFrame limpio
        """
        df_limpio = df.copy()
        
        # Eliminar duplicados
        if eliminar_duplicados:
            antes = len(df_limpio)
            df_limpio = df_limpio.drop_duplicates()
            despues = len(df_limpio)
            self.historial_operaciones.append(f"Eliminados {antes - despues} duplicados")
        
        # Tratar valores nulos
        if llenar_nulos is not None:
            if isinstance(llenar_nulos, str):
                if llenar_nulos == 'mean':
                    # Llenar con la media (solo columnas numéricas)
                    numericas = df_limpio.select_dtypes(include=[np.number]).columns
                    df_limpio[numericas] = df_limpio[numericas].fillna(df_limpio[numericas].mean())
                elif llenar_nulos == 'median':
                    numericas = df_limpio.select_dtypes(include=[np.number]).columns
                    df_limpio[numericas] = df_limpio[numericas].fillna(df_limpio[numericas].median())
                elif llenar_nulos == 'mode':
                    for col in df_limpio.columns:
                        if df_limpio[col].isnull().any():
                            moda = df_limpio[col].mode()
                            if not moda.empty:
                                df_limpio[col].fillna(moda[0], inplace=True)
            elif isinstance(llenar_nulos, dict):
                df_limpio = df_limpio.fillna(llenar_nulos)
            else:
                df_limpio = df_limpio.fillna(llenar_nulos)
            
            self.historial_operaciones.append(f"Valores nulos tratados con: {llenar_nulos}")
        
        return df_limpio
    
    def detectar_outliers(self, df: pd.DataFrame, columna: str, 
                         metodo: str = 'iqr') -> List[int]:
        """
        Detecta outliers en una columna específica.
        
        Args:
            df: DataFrame
            columna: Nombre de la columna
            metodo: Método de detección ('iqr', 'zscore')
            
        Returns:
            Lista de índices de outliers
        """
        if columna not in df.columns:
            raise ValueError(f"Columna '{columna}' no encontrada")
        
        datos = df[columna].dropna()
        outliers = []
        
        if metodo == 'iqr':
            Q1 = datos.quantile(0.25)
            Q3 = datos.quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR
            outliers = df[(df[columna] < limite_inferior) | 
                         (df[columna] > limite_superior)].index.tolist()
        
        elif metodo == 'zscore':
            from scipy import stats
            z_scores = np.abs(stats.zscore(datos))
            threshold = 3
            outliers = df[np.abs(stats.zscore(df[columna].fillna(datos.mean()))) > threshold].index.tolist()
        
        self.historial_operaciones.append(f"Detectados {len(outliers)} outliers en '{columna}' usando {metodo}")
        return outliers
    
    def agrupar_datos(self, df: pd.DataFrame, por: Union[str, List[str]], 
                     agregaciones: Dict[str, Union[str, List[str]]]) -> pd.DataFrame:
        """
        Agrupa datos y aplica funciones de agregación.
        
        Args:
            df: DataFrame
            por: Columna(s) para agrupar
            agregaciones: Diccionario de columna -> función(es) de agregación
            
        Returns:
            DataFrame agrupado
        """
        try:
            resultado = df.groupby(por).agg(agregaciones)
            self.historial_operaciones.append(f"Agrupado por {por} con agregaciones {agregaciones}")
            return resultado
        except Exception as e:
            raise ValueError(f"Error en agrupación: {str(e)}")
    
    def normalizar_datos(self, df: pd.DataFrame, columnas: Optional[List[str]] = None,
                        metodo: str = 'minmax') -> pd.DataFrame:
        """
        Normaliza datos numéricos.
        
        Args:
            df: DataFrame
            columnas: Columnas a normalizar (None para todas las numéricas)
            metodo: Método de normalización ('minmax', 'zscore')
            
        Returns:
            DataFrame normalizado
        """
        df_norm = df.copy()
        
        if columnas is None:
            columnas = df_norm.select_dtypes(include=[np.number]).columns.tolist()
        
        from sklearn.preprocessing import MinMaxScaler, StandardScaler
        
        if metodo == 'minmax':
            scaler = MinMaxScaler()
        elif metodo == 'zscore':
            scaler = StandardScaler()
        else:
            raise ValueError("Método debe ser 'minmax' o 'zscore'")
        
        df_norm[columnas] = scaler.fit_transform(df_norm[columnas])
        self.historial_operaciones.append(f"Normalizado columnas {columnas} con {metodo}")
        
        return df_norm
    
    def obtener_resumen(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Obtiene un resumen completo del DataFrame.
        
        Args:
            df: DataFrame a resumir
            
        Returns:
            Diccionario con información del resumen
        """
        resumen = {
            'forma': df.shape,
            'columnas': df.columns.tolist(),
            'tipos_datos': df.dtypes.to_dict(),
            'valores_nulos': df.isnull().sum().to_dict(),
            'memoria_mb': round(df.memory_usage(deep=True).sum() / 1024**2, 2),
            'estadisticas_numericas': df.describe().to_dict() if not df.select_dtypes(include=[np.number]).empty else {},
            'valores_unicos': {col: df[col].nunique() for col in df.columns}
        }
        
        return resumen
    
    def exportar_datos(self, df: pd.DataFrame, archivo: str, formato: str = 'csv'):
        """
        Exporta DataFrame a diferentes formatos.
        
        Args:
            df: DataFrame a exportar
            archivo: Nombre del archivo
            formato: Formato de exportación ('csv', 'excel', 'json')
        """
        try:
            if formato == 'csv':
                df.to_csv(archivo, index=False)
            elif formato == 'excel':
                df.to_excel(archivo, index=False)
            elif formato == 'json':
                df.to_json(archivo, orient='records', indent=2)
            else:
                raise ValueError("Formato debe ser 'csv', 'excel' o 'json'")
            
            self.historial_operaciones.append(f"Exportado a {archivo} en formato {formato}")
        except Exception as e:
            raise ValueError(f"Error al exportar: {str(e)}")
    
    def obtener_historial(self) -> List[str]:
        """Retorna el historial de operaciones realizadas."""
        return self.historial_operaciones.copy()
    
    def limpiar_historial(self):
        """Limpia el historial de operaciones."""
        self.historial_operaciones.clear()