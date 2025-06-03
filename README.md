# may-27-cli
Скрипт подсчёта зарплаты сотрудников

[Тестовое задание](https://docs.google.com/document/d/1Kyj6X7poy2e1lKUaZasNDIFnMYdAlyDdQ9FCBkBCe1s/edit?tab=t.0)

# Пример запуска скрипта

python main.py csvs/data1.csv csvs/data2.csv csvs/data3.csv --report payout

# Скриншот формирования отчета

![plot](Screenshot_2025-04-11.png)

# Добавление нового типа отчета

1. Создать модуль с функциями init, process, result
2. Добавить в reports.py импорт модуля нового отчета и строчку в кортеж REPORTS с указанием имени отчета и функций инициализации отчета, обработки строки лог-файла, формирования текста отчета

За основу можно взять файл report_template.py
