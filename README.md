# 🌍 Gestión de Datos de Países en Python

> Trabajo Práctico Integrador — Programación 1  
> Tecnicatura Universitaria en Programación a Distancia — UTN

---

## 📋 Descripción

Aplicación de consola desarrollada en **Python 3** que permite gestionar información sobre países del mundo. El sistema lee y persiste datos en un archivo CSV y ofrece un menú interactivo con las siguientes funcionalidades:

- Agregar y actualizar países
- Buscar por nombre (coincidencia parcial o exacta)
- Filtrar por continente, rango de población o rango de superficie
- Ordenar por nombre, población o superficie (ascendente o descendente)
- Ver estadísticas del dataset (máximos, mínimos, promedios, frecuencias)

---

## 👥 Integrantes

| Nombre | Responsabilidad principal |
|--------|--------------------------|
| [Nombre Apellido 1] | Lectura/escritura CSV, agregar, actualizar, buscar, estadísticas, marco teórico |
| [Nombre Apellido 2] | Filtros, ordenamientos, menú principal, validaciones, README y capturas |

---

## 📁 Estructura del proyecto

```
tpi-paises/
├── gestion_paises.py   # Código fuente principal
├── paises.csv          # Dataset base (22 países, 5 continentes)
├── informe_TPI.pdf     # Documentación académica completa
└── README.md           # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.x
- Sin dependencias externas — solo módulos de la librería estándar (`csv`, `os`)

---

## ▶️ Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/[usuario]/[nombre-repo].git
cd [nombre-repo]

# Ejecutar el programa
python gestion_paises.py
```

> **Nota:** asegurate de que `paises.csv` esté en la misma carpeta que `gestion_paises.py`.

---

## 🗂️ Opciones del menú

```
=== Gestión de Países === (22 países cargados)

─── Menú ───────────────────────────
  1. Agregar país
  2. Actualizar población/superficie
  3. Buscar por nombre
  4. Filtrar países
  5. Ordenar países
  6. Estadísticas
  0. Salir
────────────────────────────────────
```

---

## 💡 Ejemplos de uso

### 1️⃣ Agregar un país

```
Opción: 1

── Agregar país ──
Nombre: Uruguay
Población: 3473730
Superficie (km²): 176215
Continente: América
[OK] 'Uruguay' agregado correctamente.
```

**Validación — campo vacío:**
```
Nombre:
[ERROR] El nombre no puede estar vacío.
```

**Validación — país duplicado:**
```
Nombre: Argentina
[ERROR] Ya existe un país llamado 'Argentina'.
```

---

### 2️⃣ Actualizar datos

```
Opción: 2

── Actualizar país ──
Nombre del país a actualizar: Argentina
Datos actuales → Población: 45,376,763 | Superficie: 2,780,400 km²
Nueva población (Enter para mantener): 46000000
Nueva superficie (Enter para mantener):
[OK] Datos actualizados.
```

---

### 3️⃣ Buscar por nombre

**Búsqueda parcial:**
```
Opción: 3

── Buscar país ──
Nombre (parcial o exacto): bras

  Resultados para 'bras' (1 resultado/s)
  Nombre                      Población    Superficie  Continente
  ──────────────────────────────────────────────────────────────────────
  Brasil               213,993,437    8,515,767 km²  América
```

**Sin resultados:**
```
Nombre (parcial o exacto): xyz
[INFO] Sin resultados para: 'xyz'.
```

---

### 4️⃣ Filtrar países

**Por continente:**
```
Opción: 4 → 1
Continente: Europa

  Países en Europa (5 resultado/s)
  Nombre                      Población    Superficie  Continente
  ──────────────────────────────────────────────────────────────────────
  Alemania                83,149,300      357,022 km²  Europa
  España                  47,351,567      505,990 km²  Europa
  Francia                 67,391,582      551,695 km²  Europa
  Italia                  60,317,000      301,340 km²  Europa
  Polonia                 38,036,118      312,685 km²  Europa
```

**Por rango de población:**
```
Opción: 4 → 2
Población mínima: 50000000
Población máxima: 100000000

  Población entre 50,000,000 y 100,000,000 (4 resultado/s)
  ...
```

---

### 5️⃣ Ordenar países

```
Opción: 5

── Ordenar países ──
1. Por nombre
2. Por población
3. Por superficie
Criterio: 2
¿Ascendente (A) o Descendente (D)? D

  Ordenados por poblacion (desc) (22 resultado/s)
  Nombre                      Población    Superficie  Continente
  ──────────────────────────────────────────────────────────────────────
  China              1,412,600,000    9,596,960 km²  Asia
  India              1,380,004,385    3,287,263 km²  Asia
  Indonesia            273,523,615    1,904,569 km²  Asia
  ...
```

---

### 6️⃣ Estadísticas

```
Opción: 6

── Estadísticas ──
  Total de países: 22
  Mayor población: China (1,412,600,000)
  Menor población: Nueva Zelanda (5,084,300)
  Promedio de población: 173,237,638
  Promedio de superficie: 1,803,578 km²

  Países por continente:
    África: 5
    América: 5
    Asia: 5
    Europa: 5
    Oceanía: 2
```

---

## 🗃️ Formato del CSV

El archivo `paises.csv` debe tener el siguiente formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

**Reglas del CSV:**
- Encabezado obligatorio en la primera línea
- Sin campos vacíos
- `poblacion` y `superficie` deben ser enteros positivos (sin puntos ni comas)
- Encoding: UTF-8

---

## 🏗️ Arquitectura del código

El módulo `gestion_paises.py` aplica el principio **una función = una responsabilidad**:

| Función | Responsabilidad |
|---------|----------------|
| `cargar_paises(ruta)` | Lee el CSV y retorna lista de diccionarios |
| `guardar_paises(paises, ruta)` | Persiste la lista en el CSV |
| `agregar_pais(paises)` | Solicita datos, valida y agrega un nuevo país |
| `actualizar_pais(paises)` | Modifica población y/o superficie |
| `buscar_pais(paises)` | Filtro por coincidencia parcial o exacta |
| `buscar_exacto(paises, nombre)` | Búsqueda auxiliar, retorna dict o None |
| `filtrar_paises(paises)` | Submenú: filtra por 3 criterios |
| `ordenar_paises(paises)` | Submenú: ordena por 3 criterios × 2 direcciones |
| `mostrar_estadisticas(paises)` | Calcula y muestra indicadores del dataset |
| `mostrar_lista(paises, titulo)` | Imprime tabla formateada en consola |
| `pedir_entero(msg)` | Valida entrada numérica entera positiva |
| `pedir_entero_opcional(msg, default)` | Igual, pero acepta Enter para mantener valor |
| `menu()` | Loop principal — carga datos y despacha opciones |

**Estructura de datos principal:**

```python
# Lista de diccionarios — un dict por país
paises = [
    {
        "nombre":     "Argentina",   # str
        "poblacion":  45376763,      # int
        "superficie": 2780400,       # int
        "continente": "América"      # str
    },
    ...
]
```

---

## ✅ Validaciones implementadas

- Campos vacíos en nombre y continente → mensaje `[ERROR]` y retorno al menú
- País duplicado al agregar → mensaje `[ERROR]`
- Entrada no numérica donde se espera entero → bucle hasta valor válido
- Búsqueda sin resultados → mensaje `[INFO]`
- Opción de menú inexistente → mensaje `[ERROR]` sin romper el programa
- Archivo CSV inexistente → mensaje `[ERROR]` con lista vacía
- Filas del CSV con formato incorrecto → `[ADVERTENCIA]` y fila ignorada

---

## 🎥 Video demostrativo

▶️ **[Ver video en YouTube / Drive](https://[insertar-link-aqui])**

> El video muestra el funcionamiento completo del sistema: estructura de datos, demostración de todas las opciones del menú, validaciones y manejo de errores. Duración: ~14 minutos.

---

## 📄 Documentación

📎 **[Ver informe académico en PDF](./informe_TPI.pdf)**

El informe incluye:
- Marco teórico (listas, diccionarios, funciones, condicionales, ordenamientos, estadísticas, CSV)
- Diagrama de flujo del sistema
- Capturas de pantalla de la ejecución
- Dificultades encontradas y conclusiones
- Bibliografía y webgrafía

---

## 📚 Bibliografía

- Python Software Foundation. *Módulo csv*. https://docs.python.org/3/library/csv.html
- Python Software Foundation. *Built-in functions: sorted, min, max, sum*. https://docs.python.org/3/library/functions.html
- Real Python. *Reading and Writing CSV Files in Python*. https://realpython.com/python-csv/
- Real Python. *How to Use sorted() and sort() in Python*. https://realpython.com/python-sort/
- W3Schools. *Python Dictionaries*. https://www.w3schools.com/python/python_dictionaries.asp

---

*Programación 1 — UTN | Junio 2026*
