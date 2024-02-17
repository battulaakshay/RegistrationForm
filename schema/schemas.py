def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "fullname": (todo["fullname"]),
        "email": (todo["email"]),
        "password": (todo["password"]),
        "gender": (todo["gender"]),
        "phonenumber": (todo["phonenumber"]),
    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]
