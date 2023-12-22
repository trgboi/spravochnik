filePath = ('phonebook.txt')

def show_menu():
    print('1. Распечатать справочник \n'
          '2. Найти телефон по фамилии \n'
          '3. Изменить номер телефона \n'
          '4. Удалить запись \n'
          '5. Найти абонента по номеру телефона \n'
          '6. Добавить абонента в справочник \n'
          '7. Добавить абонента из другого справочника\n'
          '8. Закончить работу', sep='\n')
    
    choice=int(input('Циферку *ТЫК* : '))
    return choice

def read_txt(filePath):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filePath, 'r', encoding='utf-8') as file:
        phone_book = [
            dict(zip(fields, line.strip().split(',')))
            for line in file
            if len(line.strip().split(',')) == len(fields)
        ]

    return phone_book

def write_txt(filePath, phone_book):
    with open(filePath, 'w', encoding='utf-8') as pb_out:
        for entry in phone_book:
            line = ','.join(entry.values())
            pb_out.write(line + '\n')

def find_by_lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            return item['Телефон']
    return 'Абонент не найден'
    
def find_by_number(phone_book, number):
    for item in phone_book:
        if number == item['Телефон']:
            return item['Фамилия'] + ' ' + item['Имя'] + ' ' + item['Телефон']
    return 'Абонент не найден'
    
def add_user(phone_book, user_data):
    phone_book.append(user_data)
    write_txt(filePath, phone_book)
    return "Абонент добавлен"

def change_number(phone_book, last_name, new_number):
    if not phone_book or last_name is None:
        return 'Адресная книга пуста или не передана фамилия.'

    for item in phone_book:
        if item.get('Фамилия') == last_name:
            item['Телефон'] = new_number
            write_txt(filePath, phone_book)  
            return f"Номер телефона абонента {item['Имя']} {last_name} изменен на {new_number}"
    return 'Абонент не найден'

def delete_by_lastname(phone_book, last_name):
    if not phone_book or last_name is None:
        return 'Адресная книга пуста или не передана фамилия.'

    to_delete = [item for item in phone_book if item.get('Фамилия') == last_name]
    for item in to_delete:
        phone_book.remove(item)

    if to_delete:
        write_txt(filePath, phone_book)
        names_deleted = ', '.join([f"{item['Имя']} {item['Фамилия']}" for item in to_delete])
        return f'Абонента(ов) {names_deleted} удален(ы)'
    else:
        return 'Абонент не найден'

def work_with_phonebook():
	

    choice=show_menu()

    phone_book = read_txt(filePath)

    while (choice!=8):

        if choice==1:
            print(read_txt(filePath))
		
        elif choice==2:
            last_name=input('Введите фамилию ')
            print(find_by_lastname(phone_book,last_name))
		
        elif choice==3:
            last_name=input('Введите фамилию ')
            new_number=input('Введите номер телефона ')
            print(change_number(phone_book, last_name, new_number))
        elif choice==4:
            lastname=input('Введите фамилию ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice==5:
            number=input('Введите номер телефона ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
            user_data = {}
            for item in fields: 
                    user_input = input('Введите ' + item + ': ').strip()
                    user_data[item] = user_input
            print(add_user(phone_book, user_data))
        elif choice==7:
            fileName = input('Введите наименование файла: ')
            if len(fileName) > 0:
                phoneList = read_txt(filePath)
                for index in range(0, len(phoneList)):
                    print(f'{(index + 1)}. {phoneList[index]["Фамилия"]} {phoneList[index]["Имя"]} - {phoneList[index]["Телефон"]}')
                numberItem = (int(input('Введите номер строки нужного абонента: ')) - 1)
                phone_book.append(phoneList[numberItem])
                write_txt(filePath, phone_book)
        choice = show_menu()


work_with_phonebook()





