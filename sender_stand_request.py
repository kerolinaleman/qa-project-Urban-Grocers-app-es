import requests
import configuration
import data


def post_new_user ():
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json=data.user_body,
			             headers=data.header_user)

def post_new_client_kit(kit_body, auth_token):
	new_headers = data.header_user.copy()
	new_headers["Authorization"] = "Bearer " + auth_token
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
	                     json=kit_body,
			             headers=new_headers)
#
def post_new_kit (current_header, body):
	return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
						 json= body,
						 headers= current_header)

# Def. el authToken