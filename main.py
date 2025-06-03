import argparse

from csv_engine import CSVEngine
from reports import REPORTS


def main():
    parser = argparse.ArgumentParser(description='Скрипт подсчёта зарплаты сотрудников')
    parser.add_argument('csv_files', type=str, nargs='+',
                        help='пути к данным, файлов может быть несколько')
    parser.add_argument('--report', type=str, required=True,
                        choices=[el[0] for el in REPORTS],
                        help='название отчета который нужно сформировать')
    args = parser.parse_args()

    # find report
    for report_name, report_init, report_process, report_result in REPORTS:
        if args.report == report_name:
            break
    else:
        print('Неизвестный отчет', args.report)
        return

    # process
    data = report_init()
    for csv_file in args.csv_files:
        with open(csv_file) as in_file:
            csv_engine = CSVEngine(in_file.readline())
            while in_str:=in_file.readline():
                csv_engine.csv_data(in_str)
                report_process(data, csv_engine)

    # result
    result = report_result(data)
    print(result)


if __name__ == '__main__':
    main()
