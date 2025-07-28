# Proyecto Urban Grocers 

# QA Project - Urban Grocers App 🛒

Este repositorio contiene un conjunto de pruebas automatizadas para validar el comportamiento del endpoint que gestiona la creación de kits (con campo `name`) dentro de la aplicación **Urban Grocers**.

---

## ✅ Lista de Verificación de Pruebas

| №  | Descripción                                                             | Resultado Esperado (ER)                                                         |
|----|-------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| 1  | El número permitido de caracteres (1): `kit_body = { "name": "a" }`     | `201` – El campo `"name"` en la respuesta coincide con el del request          |
| 2  | Nombre con 511 caracteres                                               | `201` – El campo `"name"` en la respuesta coincide                              |
| 3  | Nombre vacío (0 caracteres)                                             | `400`                                                                           |
| 4  | Nombre con 512 caracteres                                               | `400`                                                                           |
| 5  | Caracteres especiales permitidos: `kit_body = { "name": "№%@" }`        | `201` – El campo `"name"` en la respuesta coincide                              |
| 6  | Nombre con espacios: `kit_body = { "name": " A Aaa " }`                 | `201` – El campo `"name"` en la respuesta coincide                              |
| 7  | Nombre numérico: `kit_body = { "name": "123" }`                         | `201` – El campo `"name"` en la respuesta coincide                              |
| 8  | El parámetro `"name"` no se pasa                                        | `400`                                                                           |
| 9  | Tipo incorrecto para `"name"` (número): `kit_body = { "name": 123 }`   | `400`                                                                           |

---

## 🧪 Herramientas utilizadas

- **PyCharm** – Editor de código y entorno de desarrollo para ejecutar y depurar las pruebas.
- **GitHub Desktop** – Cliente visual para gestionar los commits y sincronizar los cambios con el repositorio remoto.

---

## 🚀 Cómo ejecutar las pruebas

1. Clona este repositorio:
   git clone https://github.com/tu-usuario/qa-project-Urban-Grocers-app.git
   cd qa-project-Urban-Grocers-app

2. Instala las dependencias necesarias:
   pytest
   requests
   
3. Ejecuta las pruebas desde PyCharm o usando pytest

## 📁 Estructura del Proyecto
   
qa-project-Urban-Grocers-app/
├── tests/
│   └── test_create_kit.py
├── data/
│   └── test_payloads.json
├── requirements.txt
└── README.md

## ✍️ Autor
Kerolin Alemán Rivera
