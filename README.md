# Веб приложение используя Django + REST API

- Реализована модель User с регистрацией.
- При регистрации у пользователя должен запрашиваться username и пароль. А так же - краткая биография, и дата рождения.
- Реализована модель Post, любой пользователь может создать пост с темой поста, описанием и прикрепленной фотографией к нему.
- На главной странице сайта отображены все созданные посты пользователей.
- Добавлена возможность комментирования постов (могут комментировать любой авторизованный пользователь) на главной странице + счетчик комментариев.
- Суперпользователь имеет право удалять любой пост и комментарий в Админке.

Представления, основаны на классах (CBV).

Так же добавлены API end-points:
api/posts
api/users
api/users/<id>
