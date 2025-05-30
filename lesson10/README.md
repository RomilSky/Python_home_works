# 💪 Автотесты для интернет-магазина и калькулятора (Selenium + Allure)

## 📁 Структура проекта

```
lesson10/
│
├── pages/                  # Page Object классы
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── calculator_page.py
│
├── tests/                  # Папка с тестами
│   ├── test_calculator.py     # Тест калькулятора
│   └── test_shop_total.py     # Тест интернет-магазина
│
├── conftest.py             # Общие фикстуры (например, browser)
├── requirements.txt        # Зависимости проекта
└── README.md               # Описание проекта
```

---

## ⚙️ Установка и запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

Если файла `requirements.txt` пока нет — можно установить зависимости вручную:

```bash
pip install selenium pytest allure-pytest
```

---

### 2. Запуск тестов с генерацией отчета Allure

```bash
pytest --alluredir=allure-result
```

---

### 3. Построение и просмотр Allure-отчета

```bash
allure serve allure-result
```

Эта команда:

* Сгенерирует HTML-отчет из папки `allure-result`
* Автоматически откроет его в браузере

---

## ✨ Рекомендации по структуре

* Все тесты находятся в директории `tests/` — это **рекомендуемый подход** для PyTest и CI/CD-систем.
* Page Object-классы вынесены в директорию `pages/` для удобства поддержки и переиспользования.
* В коде используются `@allure.step`, `@allure.title`, `@allure.description` для улучшения отчетов.

---

## ✅ Покрытие

* 🔐 Логин в систему
* 🛒 Добавление товаров в корзину и оформление заказа
* ➗ Проверка калькулятора

---

## 📸 Пример Allure-отчета

После выполнения тестов с `--alluredir`, отчет будет выглядеть примерно так:

* Подробные шаги (`@allure.step`)
* Скриншоты (если добавлены при ошибках)
* Severity и Feature разметка

---

## 📌 Требования

* Python 3.10+
* Google Chrome / Firefox
* Установленный Allure:
