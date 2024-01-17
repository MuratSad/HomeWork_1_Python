Консольная программа работает
с заданными дополнительными ключами при запуске.
например: 
варианты команд:
add, python main.py --add --title "Имя заметки" --message "Тело заметки"
list,python main.py list --date "2024-01-17"
delete,python main.py delete --id 2
edit python main.py edit --id 1 --title "Заметка_1" --message "Тут заметка"

Заметки хранятся в формате json.