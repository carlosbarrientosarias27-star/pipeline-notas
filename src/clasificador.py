# src/clasificador.py

def clasificar_nota(nota):
    """Clasifica una nota numérica en su categoría.

    Reglas:
    - nota < 0 o nota > 10  → lanzar ValueError con mensaje descriptivo
    - 0  <= nota < 5        → devolver "Suspenso"
    - 5  <= nota < 7        → devolver "Aprobado"
    - 7  <= nota < 9        → devolver "Notable"
    - 9  <= nota <= 10      → devolver "Sobresaliente"

    Args:
        nota (float): Valor numérico entre 0 y 10.

    Returns:
        str: Categoría de la nota.

    Raises:
        ValueError: Si la nota está fuera del rango [0, 10].
        TypeError:  Si la nota no es un número.
    """
    # Validar que sea un número (int o float)
    if not isinstance(nota, (int, float)):
        raise TypeError(f"La nota debe ser un número, se recibió: {type(nota).__name__}")

    # Validar rango
    if nota < 0 or nota > 10:
        raise ValueError(f"La nota {nota} está fuera del rango válido [0, 10]")

    # Clasificar
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"