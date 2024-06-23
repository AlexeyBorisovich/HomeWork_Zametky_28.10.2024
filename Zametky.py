import os

NOTES_DIR = 'notes'

def init_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def create_note(title, content):
    note_path = os.path.join(NOTES_DIR, f"{title}.txt")
    with open(note_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Заметка '{title}' создана.")

def list_notes():
    notes = os.listdir(NOTES_DIR)
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"- {note}")
    else:
        print("Заметки отсутствуют.")

def read_note(title):
    note_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(note_path):
        with open(note_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"Содержимое заметки '{title}':\n{content}")
    else:
        print(f"Заметка '{title}' не найдена.")

def edit_note(title, new_content):
    note_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(note_path):
        with open(note_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Заметка '{title}' обновлена.")
    else:
        print(f"Заметка '{title}' не найдена.")

def delete_note(title):
    note_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(note_path):
        os.remove(note_path)
        print(f"Заметка '{title}' удалена.")
    else:
        print(f"Заметка '{title}' не найдена.")

if __name__ == "__main__":
    init_notes_dir()
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            create_note(title, content)
        elif choice == '2':
            list_notes()
        elif choice == '3':
            title = input("Введите заголовок заметки: ")
            read_note(title)
        elif choice == '4':
            title = input("Введите заголовок заметки: ")
            new_content = input("Введите новое содержимое заметки: ")
            edit_note(title, new_content)
        elif choice == '5':
            title = input("Введите заголовок заметки: ")
            delete_note(title)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            