# data.py

# Headers comunes
headers = {
    "Content-Type": "application/json"
}

# Usuario válido
user_body = {
    "firstName": "Allan",
    "phone": "+79998887766",
    "address": "Calle Ficticia 123"
}

# Casos de prueba para el campo "name" en kits

# 1. Nombre de 1 caracter permitido
valid_name_1_letter = "a"

# 2. Nombre de 511 caracteres
valid_name_511_chars = (
    "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
)

# 3. Nombre vacío (0 caracteres)
empty_name = ""

# 4. Nombre de más de 512 caracteres
long_name_512_plus = (
    "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
)

# 5. Caracteres especiales
special_chars_name = "!@#№%"

# 6. Espacios
spaces_name = " A Aaa "

# 7. Números como string
numeric_string_name = "123"

# 8. Falta el parámetro "name"
no_name_param = {}  # kit_body sin el campo "name"

# 9. Tipo incorrecto: número en lugar de string
numeric_type_name = 123  # sin comillas