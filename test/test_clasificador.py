# tests/test_clasificador.py
import pytest
import sys
import os

# Permite importar desde src/ sin instalar el paquete
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.clasificador import clasificar_nota


# ──────────────────────────────────────────────
# Casos NORMALES (N) — valores típicos del centro
# ──────────────────────────────────────────────

def test_nota_normal_suspenso():
    """N: Una nota normal dentro de Suspenso."""
    # Arrange
    nota = 3
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == "Suspenso"


def test_nota_normal_notable():
    """N: Una nota normal dentro de Notable."""
    # Arrange
    nota = 8
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == "Notable"


# ──────────────────────────────────────────────
# Casos LÍMITE (L) — valores exactos en los bordes
# ──────────────────────────────────────────────

def test_nota_exactamente_cinco():
    """L: nota=5.0 debe devolver 'Aprobado' (límite inferior de Aprobado)."""
    assert clasificar_nota(5.0) == "Aprobado"


def test_nota_exactamente_siete():
    """L: nota=7.0 debe devolver 'Notable' (límite inferior de Notable)."""
    assert clasificar_nota(7.0) == "Notable"


def test_nota_diez():
    """L: nota=10 debe devolver 'Sobresaliente' (máximo permitido)."""
    assert clasificar_nota(10) == "Sobresaliente"


def test_nota_cero():
    """L: nota=0 debe devolver 'Suspenso' (mínimo permitido)."""
    assert clasificar_nota(0) == "Suspenso"


def test_nota_cuatro_noventa_y_nueve():
    """L: nota=4.99 debe devolver 'Suspenso' (justo antes del límite)."""
    assert clasificar_nota(4.99) == "Suspenso"


def test_nota_nueve():
    """L: nota=9.0 debe devolver 'Sobresaliente' (límite inferior)."""
    assert clasificar_nota(9.0) == "Sobresaliente"


# ──────────────────────────────────────────────
# Casos de ERROR (E) — entradas inválidas
# ──────────────────────────────────────────────

def test_nota_negativa():
    """E: nota=-1 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        clasificar_nota(-1)


def test_nota_mayor_diez():
    """E: nota=11 debe lanzar ValueError."""
    with pytest.raises(ValueError):
        clasificar_nota(11)


def test_tipo_incorrecto():
    """E: nota='ocho' (str) debe lanzar TypeError."""
    with pytest.raises(TypeError):
        clasificar_nota("ocho")


def test_nota_negativa_mensaje_descriptivo():
    """E: El ValueError debe incluir información sobre el valor inválido."""
    with pytest.raises(ValueError, match="0"):
        clasificar_nota(-5)