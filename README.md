# Password Checker Project

Учебный проект, дз по ci/cd: **проверка надежности пароля**.

Проект демонстрирует:
- Flask-приложение
- Юнит-тесты с `unittest`
- Настроенный CI (GitHub Actions / GitLab CI)


---

##  Функционал

### Эндпоинты

1. **GET /**  
   Возвращает строку `"Password Checker API"`.  
   Используется для проверки, что сервер работает.

2. **POST /check**  
   Проверяет пароль на надежность.  
   JSON-запрос:
   ```json
   {
     "password": "string"
   }
   ```
   Условия надежного пароля:
   - длина ≥ 8 символов
   - содержит хотя бы одну цифру
   - содержит хотя бы одну букву

   Пример успешного ответа:
   ```json
   {"status": "strong"}
   ```
   Пример слабого пароля:
   ```json
   {"status": "weak"}
   ```

---

## Структура проекта

```
.
├── .github/workflows/
│   └── test_on_push.yaml      # CI GitHub Actions: установка зависимостей, запуск тестов, подсчет coverage
├── src/
│   ├── __init__.py            # Пустой файл, чтобы Python воспринимал папку как пакет
│   ├── app.py                 # Flask-приложение и логика проверки пароля
│   ├── tests.py               # Юнит-тесты всех эндпоинтов
│   └── data.json              # Пустой файл, в данном проекте не используется
├── .gitlab-ci.yml             # GitLab CI: запуск тестов и подсчет coverage
├── requirements.txt           # Зависимости проекта: Flask, pytest, coverage
└── README.md                  # Этот файл
```

---

##  Тестирование

### Локально:

```bash
# Установить зависимости
pip install -r requirements.txt

# Экспортировать PYTHONPATH
export PYTHONPATH=src  # Linux/Mac
# set PYTHONPATH=src     # Windows

# Запуск тестов
python -m unittest src.tests
```

### CI (GitHub Actions / GitLab CI):

- Автоматическая установка зависимостей
- Запуск тестов и подсчет coverage
- GitHub Actions использует файл `.github/workflows/test_on_push.yaml`
- GitLab CI использует файл `.gitlab-ci.yml`

---

##  Как запустить локально

```bash
export PYTHONPATH=src
python src/app.py
```

Приложение будет доступно по адресу: `http://127.0.0.1:8080/`

---

## Что сделано

- Создано Flask-приложение с проверкой надежности пароля
- Написаны unit-тесты для всех эндпоинтов
- Настроен CI-пайплайн (GitHub Actions / GitLab CI)
- Добавлен requirements.txt с зависимостями (Flask, pytest, coverage)
- Создан README с полным описанием

---

## Примечания

- `pytest` добавлен в зависимости, хотя проект использует `unittest`
