from module4_dz1 import total_salary
from pathlib import Path

def main():
    filename = Path('salery_workers.txt')
    if filename.exists():
        total, average = total_salary(filename)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
