Решение данного проекта не является постоянной задачей.
Проект предназначен для разового выявления переводов, отличных от переводов, которые имеются на ресурсе https://reader.eternalwords.net/
В процессе также были выявлены проповеди, которые вообще не были включены на ресурсе https://reader.eternalwords.net/
Из-за разовости использования, комментирование кода не выполнено.
Основная логика скрипта:
- построить список дубликатов проповедей, найденных в старом файле SOG
- для каждой проповеди создать текстовый файл
- привести текст каждой проповеди в нужный формат и сохранить в файле исключения (*.excl)
- * построить список проповедей отсутствующих на ресурсе https://reader.eternalwords.net/

Дальнейшее выявление нужного перевода производилось в ручном режиме, открывая файлы исключений
и сравнивая тексты с имеющимися на ресурсе https://reader.eternalwords.net/

* Файлы исключений проповедей, отсутствующих на ресурсе https://reader.eternalwords.net/, были созданы с помощью скрипта "!c_fix_temp.py":
- вставить текст проповеди в файл "c_/temp.txt"
- выполнить скрипт "!c_fix_temp.py"
- вырезать готовый отформатированный текст из файла "c_/temp_finish.txt"
- вставить вырезанный текст в новый файл и сохранить в файле исключения (*.excl)
