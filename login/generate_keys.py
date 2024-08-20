import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ['Alice', 'Bob', 'Charlie']
usernames = ['alice', 'bob', 'charlie']
passwords = ['password', 'adc123', 'def456']

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "./keys.pkl"
file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print(f"Archivo creado en: {file_path.absolute()}")
print(f"Contenido: {hashed_passwords}")

# Verificar que se puede leer
with file_path.open("rb") as file:
    loaded_passwords = pickle.load(file)
print(f"Contenido leído: {loaded_passwords}")