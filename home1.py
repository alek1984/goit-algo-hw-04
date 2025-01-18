def get_cats_info(path):
    """Читає файл із даними про котів і повертає список словників."""
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  # Видаляємо зайві пробіли та символи переносу рядка
                if line:  # Перевіряємо, що рядок не порожній
                    cat_id, name, age = line.split(",")  # Розділяємо дані
                    cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return cats_info

# Демонстрація роботи функції
file_path = "cats.txt"

# Створення файлу з даними про котів
data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""

with open(file_path, "w", encoding="utf-8") as file:
    file.write(data)

# Виклик функції
cats_info = get_cats_info(file_path)
print(cats_info)
