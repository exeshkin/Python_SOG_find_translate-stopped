import os

list_date = []


def cut_sermon(text=str, index=int):
    index_end_sermon = text.find('\n\n', index)
    if index_end_sermon == -1:
        return '---'
    else:
        index_start_sermon = text.find('\n\n', index-1000)
        if index_start_sermon == -1:
            return '---'
        else:
            return text[index_start_sermon+7:index_end_sermon]


def list_date_duplicate():
    with open('a_/list_date_duplicate.txt', encoding='utf-8') as file_date_all:
        for line in file_date_all:
            current_line = line.replace(' ', '')
            current_line = current_line.replace('\n', '')
            list_date.append(current_line)


def create_files_duplicate():
    with open('SOG_3_fix.sog', 'r', encoding='utf-8') as file_sog3:
        text_sog = file_sog3.read()
        for date in list_date:
            print(f'{date} - {text_sog.count(date)}')
            # ----------------
            index_date_first = text_sog.find(date)
            print(
                f'{index_date_first} - {text_sog[index_date_first:index_date_first+8]}')
            with open(f'b_duplicate_files/{date}_1.txt', 'w', encoding='utf-8') as file:
                file.write(cut_sermon(text_sog, index_date_first))
            # ----------------
            index_current_date_next = index_date_first
            for n in range(text_sog.count(date)-1):
                index_current_date_next = text_sog.find(
                    date, index_current_date_next+3)
                print(
                    f'{index_current_date_next} - {text_sog[index_current_date_next:index_current_date_next+8]}')
                with open(f'b_duplicate_files/{date}_{n+2}.txt', 'w', encoding='utf-8') as file:
                    file.write(cut_sermon(text_sog, index_current_date_next))


def remove_unwanted_files():
    list_duplicate_files = os.listdir('b_duplicate_files')

    for file in list_duplicate_files:
        file_size = os.stat(f'b_duplicate_files/{file}')

        if file_size.st_size < 2000:
            os.remove(f'b_duplicate_files/{file}')


def go():
    list_date_duplicate()
    create_files_duplicate()
    remove_unwanted_files()


go()
