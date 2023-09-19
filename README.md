Описание:
Написать сервис, сокращающий ссылки (простой аналог https://www.shorturl.at),
и обернуть в Docker compose. Предполагается, что сервис будет нагруженным, поэтому надо добавить кэширование.

Эндпоинты:
 - POST: generate_short_url/
   переменная long_url = {длинный URL}: сохраняет длинную ссылку в базу, генерирует и возвращает короткую ссылку
 - GET: get_long_url/{короткая ссылка}: возвращает длинную ссылку
 - GET: {короткая ссылка}: редирект на длинную ссылку, соответствующую короткой ссылке
 - GET: count/{короткая ссылка}: возвращает, сколько раз уже переходили по этой ссылке (предыдущий эндпоинт)

Короткая ссылка пусть будет из 5-ти символов: цифры, большие и маленькие латинские буквы (к примеру, fiY25)

Стек:
- фреймворк: FastAPI
- БД: MongoDB
- Кэш: Redis
