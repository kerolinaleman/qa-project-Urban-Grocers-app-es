import data
import sender_stand_request

def get_kit_body (kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_authorized_header():
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    token = user_account.json() ["authToken"]
    header = data.header_kit.copy()
    header ["Authorization"] =  f'Bearer {token}'
    return header

def positive_assert(name):
    user_body = get_kit_body(name)
    current_header = get_authorized_header()
    user_account= sender_stand_request.post_new_user()
    assert user_account == 201
    kit_response= sender_stand_request.post_new_kit(current_header, user_body)

    assert kit_response.status_code == 201
    assert kit_response.json() ["name"] == name
    assert None == kit_response.json()["productsList"]
    assert kit_response.json()["id"] != ""
    assert kit_response.json()["productsCount"] == 0


def negative_assert(name):
    user_body = get_kit_body(name)
    current_header = get_authorized_header()
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    kit_response = sender_stand_request.post_new_kit(current_header, user_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] != ""

def test_crear_1_kit_con_nombre_de_6_letras():
    new_kit_body = get_kit_body("Krfewa")
    positive_assert(new_kit_body)
def test_1_one_character():
    positive_assert("a")
def test_2_511_characters():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
def test_3_none_character():
    negative_assert("")
def test_4_512_characters():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
def test_5_special_characters():
    positive_assert('"№%@",')
def test_6_has_spaces():
    positive_assert( " A Aaa ")
def test_7_has_numbers():
    positive_assert("123")
def test_8_no_params():
    kit_body = data.kit_body.copy()
    current_header = get_authorized_header()
    kit_body.pop("name")
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    kit_response = sender_stand_request.post_new_kit(current_header, kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
def test_9_invalid_type_integer():
    kit_body = get_kit_body(123)
    current_header = get_authorized_header()
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    kit_response = sender_stand_request.post_new_kit(current_header, kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"