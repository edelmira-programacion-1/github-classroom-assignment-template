# Tarea [Número]: [Nombre Descriptivo de la Tarea]

## 🎯 Objetivo
[Explica brevemente qué concepto o habilidad practicará el alumno.]


## 📝 Descripción del Problema
[Aquí va la descripción detallada de la tarea.]

### 📥 Entrada
[Describe el formato de entrada esperado.]

### 📤 Salida
[Describe el formato de salida esperado.]

### ⛔️ Restricciones
- [Enumera las restricciones aplicables al problema.]

> (Sugerencia) [Proporciona una sugerencia útil relacionada con el problema.]

### 🧾 Muestras
[Proporciona ejemplos de entrada y salida.]

| Entrada | Salida |
|---------|--------|
| [Ejemplo de entrada] | [Ejemplo de salida] |

El formato es estricto: respeta mayúsculas, minúsculas, espacios y saltos de línea.

---

## 📂 Estructura del Repositorio

```
.
├── README                 # Instrucciones de la tarea
├── main.py                # Archivo para ejecutar el programa
├── solucion.py            # Archivo donde debes implementar tu solución
├── .gitignore             # Archivo para ignorar archivos en Git
├── requirements.txt       # Archivo para dependencias
└── tests                  
    ├── conftest.py        # Configuración de pruebas
    └── test_solucion.py   # Pruebas unitarias para la solución
```

## 🚀 Cómo ejecutar el proyecto

1. Instala Python (3.9+) si no lo tienes instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Instala *pytest*:
   
   ```
   pip install pytest
   ```

3. Clona el repositorio en tu computadora:
   
   ```
   git clone [URL_DEL_REPOSITORIO]
   ```

4. Abre `solucion.py` y escribe tu solución.

5. Instala las dependencias necesarias (si las hay) con el siguiente comando:

   ```
   pip install -r requirements.txt
   ```

6. Para ejecutar el programa y poder introducir datos manualmente, abre tu terminal en la carpeta del proyecto e introduce el siguiente comando:

   ```
   python main.py
   ```

7. Para ejecutar las pruebas unitarias y verificar tu solución, usa el siguiente comando en la terminal:

    ```
    python -m pytest -q
    ```
