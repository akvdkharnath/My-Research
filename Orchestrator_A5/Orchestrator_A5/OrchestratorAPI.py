import requests, json
import json


def get_authentication_key_local(source_url,tenancy_name,user_name,password):
    url = source_url+"/api/Account/Authenticate"
    data = {
        "tenancyName": tenancy_name,
        "usernameOrEmailAddress": user_name,
        "password": password
        }
    responce = requests.post(url,data)
    if(responce.status_code == 200):
        responce_json = responce.json()
        return responce_json
    else:
        return responce.status_code

def get_api_call(url,key,file_case = False):
    head = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + key
    }
    responce = requests.get(url,headers=head)
    
    if(responce.status_code == 200):
        if file_case == False:
            return responce.json()
        elif file_case == True:
            return responce
    else:
        return responce.status_code

def post_api_call(url,key,data = None):
    head = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + key
    }
    responce = requests.post(url,headers=head,data=json.dumps(data))
    
    if(responce.status_code == 200):
        return responce.json()
    else:
        return responce.status_code

def process_schedule(source_url,key):
    url  = source_url+"/odata/ProcessSchedules"
    data = get_api_call(url,key)
    print("Process Information: ")
    print(data)
    return data

