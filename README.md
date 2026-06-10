# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
Tecnicatura Universitaria en Programación — UTN

---

## Descripción

Aplicación de consola en Python que permite gestionar información sobre países del mundo. Lee y escribe datos desde un archivo CSV, y ofrece un menú interactivo con funciones de búsqueda, filtrado, ordenamiento y estadísticas.

## Integrantes

| Nombre | Responsabilidad principal |
|--------|--------------------------|
| [Nombre 1] | Lectura CSV, agregar/actualizar, búsqueda, estadísticas |
| [Nombre 2] | Filtros, ordenamientos, menú principal, validaciones |

## Estructura del proyecto

```
tpi-paises/
├── gestion_paises.py   # Código fuente principal
├── paises.csv          # Dataset base (22 países)
└── README.md           # Este archivo
```

## Requisitos

- Python 3.x
- Sin dependencias externas (solo módulos `csv` y `os` de la librería estándar)

## Cómo ejecutar

```bash
python gestion_paises.py
```

## Opciones del menú

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar un nuevo país (sin campos vacíos) |
| 2 | Actualizar población y/o superficie |
| 3 | Buscar por nombre (parcial o exacto) |
| 4 | Filtrar por continente, rango de población o superficie |
| 5 | Ordenar por nombre, población o superficie (asc/desc) |
| 6 | Ver estadísticas del dataset |
| 0 | Salir |

## Ejemplos de uso

### Agregar un país
```
Opción: 1
Nombre: Uruguay
Población: 3473730
Superficie (km²): 176215
Continente: América
[OK] 'Uruguay' agregado correctamente.
```

### Buscar por nombre parcial
```
Opción: 3
Nombre (parcial o exacto): bras
  Resultados para 'bras' (1 resultado/s)
  Nombre                      Población    Superficie  Continente
  ──────────────────────────────────────────────────────────────────────
  Brasil               213.993.437    8.515.767 km²  América
```

### Filtrar por continente
```
Opción: 4 → 1
Continente: Europa
  Países en Europa (5 resultado/s)
  ...
```

### Estadísticas
```
Opción: 6
  Total de países: 22
  Mayor población: China (1.412.600.000)
  Menor población: Nueva Zelanda (5.084.300)
  Promedio de población: 173.237.638
  Promedio de superficie: 1.803.578 km²

  Países por continente:
    África: 5
    América: 5
    Asia: 5
    Europa: 5
    Oceanía: 2
```

## Links

- 🎥 Video demostrativo: [insertar link]
- 📄 Documentación PDF: [insertar link o archivo en raíz del repo]
