Django Site.
Вместо sqlite базы данных была взята postgres_psycopg2.

Проект представляет собой Блог

Регистрация реализована через стандарные средства Django.

Зарегистрированный пользователь может создать статью (если он создатель статьи,то он может ее удалить или редактировать)

Post(хранит в себе текст статьи её описание,имя написавшего,дату создания)

Comment(хранит в себе адрес на статью, имя написавшего, текст комментария,дату написания )
http://127.0.0.1:8000/
https://evilgeniy.pythonanywhere.com/
Использовал источники:
1)https://developer.mozilla.org/ru/docs/Learn/Server-side/Django
2)https://tutorial.djangogirls.org/ru/
3)https://www.w3schools.com/
4)https://djbook.ru/
5)https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/