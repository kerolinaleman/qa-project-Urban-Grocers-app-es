import configuration
import requests
import data

def create_new_user():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json = data.user_body,
        headers = data.headers
    )
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error al crear usuario: {err}")
        print(f"Respuesta completa: {response.text}")
        return None
    except ValueError:
        print("Error: la respuesta no es un JSON válido. Contenido recibido:")
        print(response.text)
        return None

def get_new_user_token():
    user = create_new_user()
    if not user or "authToken" not in user:
        raise Exception("No se pudo crear el usuario o no se obtuvo el token.")
    auth_token = user["authToken"]
    print(f" authToken generado: {auth_token}")
    return {"Authorization": f"Bearer {auth_token}"}

def create_kit(kit_body, token):
    full_headers = data.headers.copy()
    full_headers.update(token)
    return requests.post(
        url = configuration.URL_SERVICE + "/api/v1/kits",
        json = kit_body,
        headers = full_headers
    )

def add_products_to_kit(kit_id, products, token):
    url = configuration.URL_SERVICE + f"/api/v1/kits/{kit_id}/products"
    headers = data.headers.copy()
    headers.update(token)
    return requests.post(
        url = url,
        json = {"productsList": products},
        headers = headers
    )

if __name__ == "__main__":
    from data import kit_body
    token = get_new_user_token()
    response = create_kit(kit_body, token)
    print("Código de estado:", response.status_code)
    print("Respuesta del servidor:", response.json())