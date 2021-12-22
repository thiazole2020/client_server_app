# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
# определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
# «отчетный» файл в формате CSV.

import csv

def get_data(file_list):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    prod_name_header = 'Изготовитель системы'
    os_name_header = 'Название ОС'
    prod_code_name_header = 'Код продукта'
    prod_type_name_header = 'Тип системы'
    headers = [prod_name_header, os_name_header, prod_code_name_header, prod_type_name_header]
    
    for file in file_list:
        with open(file, 'r') as f:
            for line in f:
                line_in_list = line.split(':')
                if line_in_list[0] == prod_name_header:
                    os_prod_list.append(line_in_list[1].strip())
                elif line_in_list[0] == os_name_header:
                    os_name_list.append(line_in_list[1].strip())
                elif line_in_list[0] == prod_code_name_header:
                    os_code_list.append(line_in_list[1].strip())
                elif line_in_list[0] == prod_type_name_header:
                    os_type_list.append(line_in_list[1].strip())

    i = 0
    main_data_file_list = []
    for file in file_list:
        main_data_filename = f'main_data_{i+1}.csv'
        main_data_file_list.append(main_data_filename)
        with open(main_data_filename, 'w') as f:
            f.write(f'{headers[0]},{headers[1]},{headers[2]},{headers[3]}\n')
            f.write(f'{os_prod_list[i]},{os_name_list[i]},{os_code_list[i]},{os_type_list[i]}\n')
        i += 1

    return main_data_file_list

def write_to_csv(csv_file_name, source_files):
    main_data_files = get_data(source_files)
    data_list = []
    first = True
    for file in main_data_files:
        with open(file, 'r') as f:
            f_reader = csv.reader(f)
            if not first:
                next(f_reader)
            for row in f_reader:
                data_list.append(row)
        first = False

    with open(csv_file_name, 'w') as f:
        csv_writer = csv.writer(f)
        for row in data_list:
            csv_writer.writerow(row)


file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
csv_file_name = 'data.csv'

write_to_csv(csv_file_name, file_list)
