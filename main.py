# 1. Відкрити file_in для читання, а file_out для запису.
    # 2. Знайти потрібні цифри (використовуючи split() та isnumeric(), як у прикладі).
    # 3. Записати їх у file_out.
    # 4. Закрити файли.
    # 5. Відкрити file_out для читання і вивести результат на екран (print).
    # Використовуй функцію safe_open() для всіх операцій з файлами!

def safe_open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
        print(f"Файл {file_name} відкрито")
        return file
    except Exception as e:
        print(f"Помилка: Файл {file_name} не вдалося відкрити.({e})")
        return None

def part_a_create_file(filename):
    """
    Створення текстового файлу TF2_1 із символьних рядків різної довжини.
    """
    file = safe_open(filename, 'w')
    if file:  # Якщо файл успішно відкрито, робимо все, що нижче:
        lines = [
            "The flight number 1717 is postponed for 40 minute",
            "Boarding will start at 5 a.m.",
            "Passenger count is 1024 people in terminal 2",
            "Short line",
            "A very long line with numbers like 987654 and 12"
        ]
        for line in lines:
            file.write(line + "\n")
        file.close()
        print(f"Дані записано у файл {filename}\n")

def participant_task_process_and_print(file_in, file_out):
    """
    Завдання для Напарника
    1. Читає вміст TF2_1, знаходить послідовності цифр довжиною більше двох
       і записує їх у TF2_2 в один рядок через пробіл (Частина Б).
    2. Читає вміст TF2_2 і виводить його на екран (Частина В).
    """
    print("Повернемося через 5хв, повернітся пізніше")

def main():
    file1_name = "TF2_1.txt"
    file2_name = "TF2_2.txt"

    print("Робота тімліда створення файлу")
    part_a_create_file(file1_name)

    print("Робота напарника обробка та виведення")
    participant_task_process_and_print(file1_name, file2_name)


if __name__ == "__main__":
    main()