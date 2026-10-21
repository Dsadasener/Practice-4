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
    # ДОДАНО: 1. Відкриваємо file_in для читання
    f_in = safe_open(file_in, 'r')
    if not f_in:
        return

    # ДОДАНО: Читаємо весь текст з файлу
    text = f_in.read()
    f_in.close()  # ДОДАНО: 4. Закриваємо файл після читання

    # ДОДАНО: 2. Знаходимо потрібні цифри (використовуючи split() та isnumeric())
    words = text.split()  # Розбиваємо текст на окремі слова по пробілах
    target_numbers = []
    for word in words:
        # Перевіряємо, чи складається слово тільки з цифр і чи його довжина більша за 2
        if word.isnumeric() and len(word) > 2:
            target_numbers.append(word)

    # ДОДАНО: Відкриваємо file_out для запису
    f_out = safe_open(file_out, 'w')
    if not f_out:
        return

    # ДОДАНО: 3. Записуємо знайдені числа у file_out в один рядок через пробіл
    f_out.write(" ".join(target_numbers))
    f_out.close()  # ДОДАНО: 4. Закриваємо файл після запису

    # ДОДАНО: 5. Відкриваємо file_out для читання і виводимо результат на екран
    f_out_read = safe_open(file_out, 'r')
    if f_out_read:
        result = f_out_read.read()
        print(f"\n--- Вміст файлу {file_out} ---")
        print(result)
        print("---------------------------------\n")
        f_out_read.close()  # ДОДАНО: Закриваємо файл після виведення


def main():
    file1_name = "TF2_1.txt"
    file2_name = "TF2_2.txt"

    print("Робота тімліда створення файлу")
    part_a_create_file(file1_name)

    print("Робота напарника обробка та виведення")
    participant_task_process_and_print(file1_name, file2_name)


if __name__ == "__main__":
    main()