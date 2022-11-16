list_date = []
with open('list_date_all.txt', encoding='utf-8') as file_date_all:
    for line in file_date_all:
        current_line = line.replace(' ', '')
        current_line = current_line.replace('\n', '')
        list_date.append(current_line)

with open('SOG_EW.sog', 'r', encoding='utf-8') as file_sog3:
    text_sog = file_sog3.read()
    for date in list_date:
        if date in text_sog:
            pass
        else:
            print(date)
