import pandas as pd
from cryptography.fernet import Fernet
from typing import Union

class Codex:
    def __init__(self, key_path: str = 'key.key') -> None:
        self.key_path = key_path
        self.key = None

    def generar_clave(self) -> None:
        """
        Genera una clave y la guarda en un archivo
        """
        self.key = Fernet.generate_key()
        with open(self.key_path, "wb") as key_file:
            key_file.write(self.key)

    def cargar_clave(self) -> None:
        """
        Carga la clave desde el archivo
        """
        self.key = open(self.key_path, "rb").read()

    def guardar_df(self, df: pd.DataFrame, filename: str, formato: str = 'parquet') -> None:
        """
        Guarda el dataframe en varios formatos y lo cifra
        """
        formato = 'excel' if formato == 'xlsx' else formato
        try:
            getattr(df, f'to_{formato}')(filename)
            self.cifrar(filename)
        except AttributeError:
            raise ValueError(f'Formato no soportado: {formato}')

    def cargar_df(self, filename: str, formato: str = 'parquet') -> pd.DataFrame:
        """
        Descifra y carga el dataframe desde un archivo
        """
        self.descifrar(filename)
        formato = 'excel' if formato == 'xlsx' else formato
        try:
            return getattr(pd, f'read_{formato}')(filename)
        except AttributeError:
            raise ValueError(f'Formato no soportado: {formato}')

    def cifrar(self, filename: str) -> None:
        """
        Dado un nombre de archivo (str) y una clave (bytes), cifra el archivo y escribe
        los bytes cifrados de nuevo en el archivo.
        """
        f = Fernet(self.key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def descifrar(self, filename: str) -> None:
        """
        Dado el nombre del archivo (con datos cifrados) y la clave, descifra el contenido
        del archivo y escribe los datos originales de nuevo en el archivo.
        """
        f = Fernet(self.key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
