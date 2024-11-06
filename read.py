file = open('habr.html', encoding='utf-8')
text = file.read()


def clear_tags(st: str) -> str:
    while True:
        tag_start = st.find("<")
        if tag_start == -1:
            break
        tag_end = st.find(">")
        st = st[:tag_start] + st[tag_end + 1:]
    return st

def find_time_watch(st: str, tag_class: str) -> str:
    # поиск класса, переданного выше
    index = st.find(tag_class)
    # поиск закрывающего тега html (контейнер) с указанного индекса
    index_end = st.find("</span>", index)
    # возврат строки между тегами контейнера
    return st[index + len(tag_class) + 2:index_end]

# открытие файла и сохранение его дескриптора
file = open("habr.html", encoding="utf-8")
# чтение содержимого файла полностью в переменную
text = file.read()

index = 0 # начальный индекс
while True: # бесконечный цикл, пока не закончатся теги для поиска
    # поиск начала статьи
    index = text. find("<article", index)
    # прерывание цикла, если тег заголовка не найден
    if index == -1:
        break
    # поиск открывающего тега html (заголовок уровня 2)
    index = text.find("<h2", index)
    # поиск открывающего тега html (контейнер) с указанного индекса
    index = text. find("<span>", index)
    # поиск закрывающего тега html (контейнер) с указанного индекса
    index_end = text.find("</span>", index)
    # вырезание строки между найденными индексами
    title = text[index + len("<span>"):index_end]
    # вызов функции для вырезания лишних тегов из строки
    new_title = clear_tags(title)
    # css класс времени на прочтение для контейнера
    time_class = "tm-article-reading-time __ label"
    # вызов функции поиска и выделения времени (передаётся остальной текст)
    time = find_time_watch(text[index_end:], time_class)

    # css класс количества просмотров для контейнера
    watch_class = "tm-icon-counter __ value"
    # вызов функции поиска и выделения просмотров (передаётся остальной текст)
    watch = find_time_watch(text[index_end:], watch_class)
    # вывод заголовка
    print(new_title)
    # вывод времени и просмотров
    print(time, "|", watch)
    # вывод пустой строки для разделения постов
    print()

index = text.find('<h2')
index = text.find("<span>", index)
index_end = text.find("</span>", index)
title = text[index + len("<span>"):index_end]

tag_start = text.find("<")
tag_end = text.find(">")
clear_title = title[:tag_start] + title[tag_end + 1:]

new_title = clear_tags(title)
print(new_title)

