def number_str(number):
    '''
    Функция принимает число и возвращает строку
        :param number : int Число
        :return : str Строка
    '''

    # Строка формируется в зависимости от количества цифр в числе
    match len(str(number)):
        case 1:
            number = f'000{number}'
        case 2:
            number = f'00{number}'
        case 3:
            number = f'0{number}'
    return number


def list_duplicate(list):
    visited = set()
    duplicate_list = [x for x in list if x in visited or (
        visited.add(x) or False)]
    return duplicate_list


def create_file_list_sermon():
    number_sermon = 1

    with open('SOG_3_fix.sog', encoding='utf-8') as file_sog3, open('a_/list_sermon_sog3.txt', 'a', encoding='utf-8') as file_list_sermon:
        for line in file_sog3:

            number_sermon_str = number_str(number_sermon)

            if f'{number_sermon_str}' in line:

                file_list_sermon.write(next(file_sog3))

                number_sermon += 1


def create_list_date_and_date_duplicate():
    all_date = []

    with open('a_/list_sermon_sog3.txt', encoding='utf-8') as file_list_sermon:
        for line in file_list_sermon:
            if '-' in line:
                index_tire = line.find('-')
                str_year = line[index_tire-2:index_tire]
                str_date = line[index_tire+1:index_tire+6]

                if str_year.isdigit():
                    all_date.append(f'{str_year}-{str_date}')
                else:
                    index_tire_next = line.find('-', index_tire + 1)
                    str_year = line[index_tire_next-2:index_tire_next]
                    str_date = line[index_tire_next+1:index_tire_next+6]

                    all_date.append(f'{str_year}-{str_date}')

    with open('a_/list_date_all.txt', 'a', encoding='utf-8') as file_list_all_date:
        for date in all_date:
            file_list_all_date.write(f'{date}\n')

    with open('a_/list_date_duplicate.txt', 'a', encoding='utf-8') as file_date_duplicate:
        for sermon_duplicate in list_duplicate(all_date):
            file_date_duplicate.write(f'{sermon_duplicate}\n')


def go():
    create_file_list_sermon()
    create_list_date_and_date_duplicate()


go()
