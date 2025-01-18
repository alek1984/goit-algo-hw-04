def create_salary_file(file_path):
    """Створює файл із даними про зарплати."""
    data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)

def total_salary(path):
    """Аналізує файл і повертає загальну та середню зарплату."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        total = 0
        count = 0
        
        for line in lines:
            name, salary = line.strip().split(",")  # Розділяємо ім'я і зарплату
            total += int(salary)  # Додаємо зарплату до загальної суми
            count += 1  # Підраховуємо кількість співробітників
        
        average = total / count if count > 0 else 0  # Обчислюємо середню зарплату
        
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0
    except ValueError:
        print("Файл містить неправильні дані. Перевірте формат.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Шлях до файлу
file_path = "salaries.txt"

# Створення файлу з даними
create_salary_file(file_path)

# Виклик функції для аналізу зарплат
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
