import sender_stand_request
from data import (
    valid_name_1_letter,
    valid_name_511_chars,
    empty_name,
    long_name_512_plus,
    special_chars_name,
    spaces_name,
    numeric_string_name,
    no_name_param,
    numeric_type_name
)

# Función para construir el cuerpo del kit si tiene campo name
def get_kit_body(name):
    return { "name": name }

# Función común para crear kit con nombre y validar respuesta esperada
def positive_assert(name_value):
    body = get_kit_body(name_value)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.create_kit(body, token)
    assert response.status_code == 201
    assert response.json()["name"] == name_value

# Función común para verificar códigos 400 en casos inválidos
def negative_assert(name_value):
    body = get_kit_body(name_value)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.create_kit(body, token)
    assert response.status_code == 400

# 1. Nombre de 1 caracter permitido
def test_name_1_char():
    positive_assert(valid_name_1_letter)

# 2. Nombre de 511 caracteres permitido
def test_name_511_chars():
    positive_assert(valid_name_511_chars)

# 3. Nombre vacío (0 caracteres)
def test_name_empty():
    negative_assert(empty_name)

# 4. Nombre de más de 512 caracteres
def test_name_too_long():
    negative_assert(long_name_512_plus)

# 5. Caracteres especiales permitidos
def test_name_special_chars():
    positive_assert(special_chars_name)

# 6. Nombre con espacios
def test_name_with_spaces():
    positive_assert(spaces_name)

# 7. Nombre con números como string
def test_name_numeric_string():
    positive_assert(numeric_string_name)

# 8. No se pasa el campo "name"
def test_name_missing_param():
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.create_kit(no_name_param, token)
    assert response.status_code == 400

# 9. Se pasa tipo incorrecto (número)
def test_name_wrong_type():
    body = get_kit_body(numeric_type_name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.create_kit(body, token)
    assert response.status_code == 400