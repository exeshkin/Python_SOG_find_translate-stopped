import math


def splitting_line(line):
    '''
    Функция разбивает полученную строку на дополнительые строки,
    если длина исходной строки превышает 300 символов
        :param line : str Параграф в виде строки
        :return : str Параграф со строками длиной менее 300 символов
    '''
    # Заменить кавычки на обычные
    line = line.replace('“', '"')
    line = line.replace('”', '"')

    # Начало формирования параграфа
    final_line = ''
    # Определить длину параграфа
    length_line = len(line)

    # Проверить является ли длина параграфа больше 300 символов
    if length_line > 300:
        # Определить количество разделений параграфа
        count_broken_line = math.ceil(length_line / 300)
        # Определить длину строк разделений параграфа
        number_symb_broken_line = math.ceil(
            length_line / count_broken_line)

        # Начальный индекс разделителя
        index_witespace = 0
        for count in range(count_broken_line):
            count += 1
            if count == 1:
                # Определить индекс разделителя до первого пробела
                index_witespace = line.find(' ', number_symb_broken_line)
                # Обрезать параграф до индекса разделителя
                broken_line = line[:index_witespace + 1]
                # Добавить данные в параграф
                final_line += f'{broken_line}\n'
            else:
                # Определить предыдущий индекс разделителя
                prev_index_witespace = index_witespace + 1
                # Определить следующий индекс разделителя до первого пробела
                next_intermediate_index = index_witespace + number_symb_broken_line
                # Проверить является ли следующий индекс разделителя
                # больше длины параграфа
                if next_intermediate_index < length_line:
                    # Определить индекс разделителя до первого пробела
                    index_witespace = line.find(
                        ' ', next_intermediate_index)
                else:
                    # Определить индекс разделителя до конца параграфа
                    index_witespace = length_line
                # Обрезать параграф по индексам разделителя
                broken_line = line[prev_index_witespace:index_witespace + 1]
                # Добавить данные в параграф
                final_line += f'{broken_line}\n'
    else:
        # Добавить данные в параграф
        final_line = f'{line}\n'

    # Вернуть готовый параграф
    return final_line


def temp_sermon_to_fix_sermon():
    with open('c_/temp.txt', encoding='utf-8') as file_temp, open('c_/temp_fix.txt', 'w', encoding='utf-8') as file_temp_fix:
        sermon_one_str = ''
        for line in file_temp:
            if line[0:1].isdigit():
                current_line = line.replace(' ', '. ', 1)
                current_line = current_line.replace('\n', ' ')
                sermon_one_str += f'\n{current_line}'
            else:
                sermon_one_str += line.replace('\n', ' ')

        file_temp_fix.write(sermon_one_str)


def temp_fix_to_temp_finish():
    with open('c_/temp_fix.txt', encoding='utf-8') as file_temp_fix, open('c_/temp_finish.txt', 'a', encoding='utf-8') as file_temp_finish:
        text = ''
        for line in file_temp_fix:
            text += splitting_line(line)

        file_temp_finish.write(text.replace('\n\n', '\n'))

    with open('c_/temp_fix.txt', 'w', encoding='utf-8') as file_temp_fix:
        file_temp_fix.write('')


def go():
    temp_sermon_to_fix_sermon()
    temp_fix_to_temp_finish()


go()
