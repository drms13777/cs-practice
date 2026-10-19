import sys
from tablestats import read_rows, count_types, total_minutes, to_csv
def main():
    try:
        filename = input("Введите имя файла: ").strip()
    except (EOFError, KeyboardInterrupt):
        return

    if not filename:
        print("Ошибка: Пустой ввод")
        return

    try:
        with open(filename, encoding="utf-8") as table:
            rows = read_rows(table)
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден в текущей папке")
        return
    counts = count_types(rows)
    unique_types_count = len(counts)
    error_minutes = total_minutes(rows, "ошибка")
    print(len(rows))
    print(unique_types_count)
    print(error_minutes)
    csv_summary = to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(csv_summary)

if __name__ == "__main__":
    main()
