# 📝 Pipeline-Notas

Proyecto de clasificación de notas con pipeline CI/CD automatizado mediante GitHub Actions.

---

# 📁 Estructura del Proyecto

```
pipeline-notas/
├── .github/
│   └── workflows/
│       └── pipeline.yml        # Pipeline CI/CD
├── src/
│   └── clasificador.py         # Lógica principal de clasificación
├── test/
│   └── test_clasificador.py    # Tests unitarios
├── conftest.py                 # Configuración de pytest
├── requirements.txt            # Dependencias del proyecto
└── README.md
```

---

# 🚀 Descripción

**Pipeline-Notas** es una aplicación Python que clasifica notas de texto de forma automática. El proyecto incluye un pipeline CI/CD configurado con GitHub Actions que ejecuta los tests automáticamente en cada push o pull request.

---

# ⚙️ Requisitos Previos

- Python 3.8+
- pip

---

# 🔧 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/pipeline-notas.git
cd pipeline-notas
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv

# En Linux/macOS
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecución de Tests

Los tests están escritos con `pytest`. Para ejecutarlos:

```bash
pytest
```

O con más detalle:

```bash
pytest -v
```

---

# 📦 Módulos Principales

## `src/clasificador.py`

Contiene la lógica principal de clasificación de notas. Se encarga de procesar y categorizar el contenido de las notas de texto.

## `test/test_clasificador.py`

Tests unitarios que validan el comportamiento del clasificador.

## `conftest.py`

Fixtures y configuración compartida para los tests de pytest.

---

# 🔄 Pipeline CI/CD

El pipeline está definido en `.github/workflows/pipeline.yml` y se ejecuta automáticamente al hacer push o abrir un pull request a la rama `main`.

**Pasos del pipeline:**

1. Checkout del código
2. Configuración de Python
3. Instalación de dependencias
4. Ejecución de tests con `pytest`

---

# 📋 Dependencias

Las dependencias del proyecto se encuentran en `requirements.txt`. Instálalas con:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contribuciones

1. Haz un fork del repositorio
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m "Añade nueva funcionalidad"`
4. Sube los cambios: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

# 📄 Licencia

Este proyecto está bajo la licencia incluida en el archivo [LICENSE](LICENSE).