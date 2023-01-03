import requests

def get_finds_pet_by_status(status="available"):

    headers = {'accept':'application/json'}
    res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers=headers)
    print(res.status_code)
    if 'application/json' in res.headers['Content-Type']:
        print(res.json())
    else:
        print(res.text)


def add_new_pet():

    data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "dog",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)
    print(res.status_code)
    if 'application/json' in res.headers['Content-Type']:
        print("Ответ на запрос по добавлению питомца: ", res.json())
    else:
        print("Ответ на запрос по добавлению питомца: ", res.text)


def delete_a_pet(pet_id):

    headers = {'accept': 'application/json'}
    url = (f'https://petstore.swagger.io/v2/pet/{pet_id}')
    res = requests.delete(url, headers=headers)
    print(res.status_code)
    if res.status_code != 404:
        if 'application/json' in res.headers['Content-Type']:
            print(res.json())
        else:
            print(res.text)
    else:
        print(res.content)



def update_existing_pet():

    data = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "dog",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)
    print(res.status_code)
    if 'application/json' in res.headers['Content-Type']:
        print("Ответ на запрос по обновлению питомца: ", res.json())
    else:
        print("Ответ на запрос по обновлению питомца: ", res.text)


get_finds_pet_by_status()
print('-' * 250)
add_new_pet()
print('-' * 250)
delete_a_pet('9223372036854307742')
print('-' * 250)
update_existing_pet()
print('-' * 250)