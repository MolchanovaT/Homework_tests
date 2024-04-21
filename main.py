def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def solution(a, b, c):
    d = discriminant(a, b, c)

    if d > 0:
        x1 = round((-1 * b + d ** 0.5) / 2 * a, 1)
        x2 = round((-1 * b - d ** 0.5) / 2 * a, 1)
        print(x1, x2)
        return [x1, x2]
    elif d == 0:
        x = round(-1 * b / (2 * a), 1)
        print(x)
        return x
    else:
        print("корней нет")
        return "корней нет"


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['311 020203']
}


def get_name(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            res = doc['name']
            break
        else:
            res = "Документ не найден"
    return res


def get_directory(doc_number):
    res = "Полки с таким документом не найдено"
    for shelf_key in directories.keys():
        list_numbers = directories.get(shelf_key)
        for num in list_numbers:
            if num == doc_number:
                res = shelf_key
                return res
    return res


def add(document_type, number, name, shelf_number):
    doc_dict = {"type": document_type, "number": number, "name": name}
    documents.append(doc_dict)

    for shelf_key in directories.keys():
        if shelf_key == str(shelf_number):
            directories.get(str(shelf_number)).append(number)
            return True


if __name__ == '__main__':
    # solution(1, 8, 15)
    # solution(1, -13, 12)
    # solution(-4, 28, -49)
    # solution(1, 1, 1)

    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
