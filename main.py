# Инициализация пустого словаря
phonebook = {}

# Функция добавления контакта
def add_contact(name, phone):
    phonebook[name] = phone

# Функция изменения контакта
def update_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        print(f"Контакт {name} был обновлен")
    else:
        print(f"Контакт {name} не найден")

# Функция удаления контакта
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Контакт {name} был удален")
    else:
        print(f"Контакт {name} не найден")


# Функция поиска контакта
def find_contact(query):
    matches = []
    for name, phone in phonebook.items():
        if query.lower() in name.lower():
            matches.append((name, phone))
    return matches

# Добавление контакта
add_contact("Иван Иванов", "123-456-7890")

# Изменение контакта
update_contact("Иван Иванов", "111-222-3333")

# Удаление контакта
delete_contact("Иван Иванов")

# Поиск контакта
matches = find_contact("Иван")
print(matches)


