# Sprint_6

Автотесты для сервиса https://qa-scooter.praktikum-services.ru/

### Проект содержит:

Папка locators - папка с локатарми для всех страниц.
Папка pages - папка с методами для всех страниц.
Папка tests - папка с тестами для всех страниц.
Файл conftest.py - фикстуры, необходимые для запуска тестов.
Файл data.py - тестовые данные для запуска тестов.
Файд README.md - полное описание проекта.

### Описание тестов из папки tests:

**Главная страница** - test_main_page.py:
<p>Тестовый сценарий: Выпадающий список в разделе «Вопросы о важном». Тебе нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст. Важно написать отдельный тест на каждый вопрос.

**Страница Заказа** - test_order_page.py:
<p>Тестовый сценарий: Совершить два заказа с разными данными через разные кнопки. Проверить переход по лого Самоката. Проверить переход по лого Яндекса.

# Команда для терминала, запускающая все тесты: `pytest -v`
