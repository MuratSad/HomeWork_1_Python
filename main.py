import json
import argparse
import sys
from datetime import datetime

# Файл для хранения данных о заметках
NOTES_FILE = 'notes.json'

# Загрузка заметок из файла
def load_notes():
    try:
        with open(NOTES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Сохранение заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

# Добавление новой заметки
def add_note(title, message):
    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'message': message,
        'date': datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    return note

# Просмотр списка заметок
def list_notes(filter_date=None):
    notes = load_notes()
    if filter_date:
        notes = [note for note in notes if note['date'][:10] == filter_date]
    return notes

# Редактирование заметки
def edit_note(note_id, title=None, message=None):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            if title:
                note['title'] = title
            if message:
                note['message'] = message
            note['date'] = datetime.now().isoformat()  # Обновляем дату
            save_notes(notes)
            return note
    return None

# Удаление заметки
def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)

# Обработка аргументов командной строки
parser = argparse.ArgumentParser(description="Notes management system")
parser.add_argument('command', help='Command to execute (add, list, edit, delete)')
parser.add_argument('--id', type=int, help='ID of the note')
parser.add_argument('--title', help='Title of the note')
parser.add_argument('--message', help='Content of the note')
parser.add_argument('--date', help='Filter notes by date (YYYY-MM-DD)')

args = parser.parse_args()

if args.command == 'add':
    if args.title and args.message:
        note = add_note(args.title, args.message)
        print(f'Заметка добавлена: {note}')
    else:
        print('Для добавления заметки необходимо задать заголовок и текст заметки.Например: main.py add --title "имя заметки" --Message "Текст заметки"')
elif args.command == 'list':
    notes = list_notes(filter_date=args.date)
    for note in notes:
        print(note)
elif args.command == 'edit':
    if args.id and (args.title or args.message):
        note = edit_note(args.id, args.title, args.message)
        if note:
            print(f'Заметка обновлена: {note}')
        else:
            print(f'Заметка с ID {args.id} не найдена.')
    else:
        print('Для редактирования заметки необходимо задать ID Номер заметки и --message "новый текст" или --title "заголовок".')
elif args.command == 'delete':
    if args.id:
        delete_note(args.id)
        print(f'Заметка с ID {args.id} удалена.')
    else:
        print('Для удаления заметки необходимо задать её ID.')
else:
    print('Неизвестная команда. Используйте "add", "list", "edit" или "delete".')