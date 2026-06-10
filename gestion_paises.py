"""
Trabajo Práctico Integrador — Programación 1
Gestión de Datos de Países en Python
"""

import csv
import os

ARCHIVO_CSV = "paises.csv"

# ─────────────────────────────────────────────
# LECTURA Y ESCRITURA DEL CSV
# ─────────────────────────────────────────────

def cargar_paises(ruta: str) -> list:
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    paises = []
    if not os.path.exists(ruta):
        print(f"[ERROR] No se encontró el archivo '{ruta}'.")
        return paises
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    })
                except (ValueError, KeyError) as e:
                    print(f"[ADVERTENCIA] Fila ignorada por error de formato: {fila} — {e}")
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")
    return paises


def guardar_paises(paises: list, ruta: str) -> None:
    """Guarda la lista de países en el CSV."""
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")


# ─────────────────────────────────────────────
# AGREGAR Y ACTUALIZAR
# ─────────────────────────────────────────────

def agregar_pais(paises: list) -> None:
    """Solicita datos al usuario y agrega un nuevo país."""
    print("\n── Agregar país ──")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    # Verificar duplicado
    if any(p["nombre"].lower() == nombre.lower() for p in paises):
        print(f"[ERROR] Ya existe un país llamado '{nombre}'.")
        return

    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie (km²): ")
    continente = input("Continente: ").strip()
    if not continente:
        print("[ERROR] El continente no puede estar vacío.")
        return

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises, ARCHIVO_CSV)
    print(f"[OK] '{nombre}' agregado correctamente.")


def actualizar_pais(paises: list) -> None:
    """Actualiza población y/o superficie de un país existente."""
    print("\n── Actualizar país ──")
    nombre = input("Nombre del país a actualizar: ").strip()
    pais = buscar_exacto(paises, nombre)
    if not pais:
        print(f"[ERROR] No se encontró '{nombre}'.")
        return

    print(f"Datos actuales → Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km²")
    nueva_pob = pedir_entero_opcional("Nueva población (Enter para mantener): ", pais["poblacion"])
    nueva_sup = pedir_entero_opcional("Nueva superficie (Enter para mantener): ", pais["superficie"])

    pais["poblacion"] = nueva_pob
    pais["superficie"] = nueva_sup
    guardar_paises(paises, ARCHIVO_CSV)
    print("[OK] Datos actualizados.")


# ─────────────────────────────────────────────
# BÚSQUEDA
# ─────────────────────────────────────────────

def buscar_pais(paises: list) -> None:
    """Busca países por nombre (coincidencia parcial o exacta)."""
    print("\n── Buscar país ──")
    termino = input("Nombre (parcial o exacto): ").strip().lower()
    if not termino:
        print("[ERROR] Ingresá un término de búsqueda.")
        return
    resultados = [p for p in paises if termino in p["nombre"].lower()]
    mostrar_lista(resultados, f"Resultados para '{termino}'")


def buscar_exacto(paises: list, nombre: str):
    """Devuelve el diccionario del país con ese nombre exacto (case-insensitive), o None."""
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


# ─────────────────────────────────────────────
# FILTROS
# ─────────────────────────────────────────────

def filtrar_paises(paises: list) -> None:
    """Submenú de filtros."""
    print("\n── Filtrar países ──")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        continente = input("Continente: ").strip()
        resultado = [p for p in paises if p["continente"].lower() == continente.lower()]
        mostrar_lista(resultado, f"Países en {continente}")

    elif opcion == "2":
        min_pob = pedir_entero("Población mínima: ")
        max_pob = pedir_entero("Población máxima: ")
        resultado = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
        mostrar_lista(resultado, f"Población entre {min_pob:,} y {max_pob:,}")

    elif opcion == "3":
        min_sup = pedir_entero("Superficie mínima (km²): ")
        max_sup = pedir_entero("Superficie máxima (km²): ")
        resultado = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
        mostrar_lista(resultado, f"Superficie entre {min_sup:,} y {max_sup:,} km²")

    else:
        print("[ERROR] Opción inválida.")


# ─────────────────────────────────────────────
# ORDENAMIENTOS
# ─────────────────────────────────────────────

def ordenar_paises(paises: list) -> None:
    """Submenú de ordenamiento."""
    print("\n── Ordenar países ──")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    criterio = input("Criterio: ").strip()

    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio not in claves:
        print("[ERROR] Opción inválida.")
        return

    clave = claves[criterio]
    orden = input("¿Ascendente (A) o Descendente (D)? ").strip().upper()
    if orden not in ("A", "D"):
        print("[ERROR] Ingresá A o D.")
        return

    descendente = orden == "D"
    ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)
    mostrar_lista(ordenados, f"Ordenados por {clave} ({'desc' if descendente else 'asc'})")


# ─────────────────────────────────────────────
# ESTADÍSTICAS
# ─────────────────────────────────────────────

def mostrar_estadisticas(paises: list) -> None:
    """Calcula y muestra estadísticas básicas del dataset."""
    if not paises:
        print("[ERROR] No hay datos para calcular estadísticas.")
        return

    print("\n── Estadísticas ──")

    # Población
    max_pob = max(paises, key=lambda p: p["poblacion"])
    min_pob = min(paises, key=lambda p: p["poblacion"])
    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)

    # Superficie
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    # Cantidad por continente
    continentes = {}
    for p in paises:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print(f"  Total de países: {len(paises)}")
    print(f"  Mayor población: {max_pob['nombre']} ({max_pob['poblacion']:,})")
    print(f"  Menor población: {min_pob['nombre']} ({min_pob['poblacion']:,})")
    print(f"  Promedio de población: {prom_pob:,.0f}")
    print(f"  Promedio de superficie: {prom_sup:,.0f} km²")
    print("\n  Países por continente:")
    for cont, cant in sorted(continentes.items()):
        print(f"    {cont}: {cant}")


# ─────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────

def mostrar_lista(paises: list, titulo: str = "Países") -> None:
    """Imprime una lista de países en formato tabla."""
    if not paises:
        print(f"[INFO] Sin resultados para: {titulo}.")
        return
    ancho = 26
    print(f"\n  {titulo} ({len(paises)} resultado/s)")
    print(f"  {'Nombre':<{ancho}} {'Población':>14} {'Superficie':>12} {'Continente'}")
    print("  " + "─" * 70)
    for p in paises:
        print(f"  {p['nombre']:<{ancho}} {p['poblacion']:>14,} {p['superficie']:>10,} km²  {p['continente']}")


def pedir_entero(mensaje: str) -> int:
    """Pide un entero positivo al usuario con validación."""
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("[ERROR] Ingresá un número entero positivo.")


def pedir_entero_opcional(mensaje: str, default: int) -> int:
    """Pide un entero o devuelve el valor por defecto si se presiona Enter."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            return default
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("[ERROR] Ingresá un número entero positivo o presioná Enter para mantener.")


# ─────────────────────────────────────────────
# MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu() -> None:
    """Loop principal del programa."""
    paises = cargar_paises(ARCHIVO_CSV)
    print(f"\n=== Gestión de Países === ({len(paises)} países cargados)\n")

    opciones = {
        "1": ("Agregar país", agregar_pais),
        "2": ("Actualizar población/superficie", actualizar_pais),
        "3": ("Buscar por nombre", buscar_pais),
        "4": ("Filtrar países", filtrar_paises),
        "5": ("Ordenar países", ordenar_paises),
        "6": ("Estadísticas", mostrar_estadisticas),
        "0": ("Salir", None),
    }

    while True:
        print("\n─── Menú ───────────────────────────")
        for clave, (desc, _) in opciones.items():
            print(f"  {clave}. {desc}")
        print("────────────────────────────────────")
        eleccion = input("Opción: ").strip()

        if eleccion == "0":
            print("Hasta luego.")
            break
        elif eleccion in opciones:
            _, funcion = opciones[eleccion]
            funcion(paises)
        else:
            print("[ERROR] Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    menu()
