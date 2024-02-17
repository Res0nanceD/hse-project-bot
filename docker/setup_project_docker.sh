#!/bin/bash

# Путь до python3.10
PYTHON_PATH=$(which python3.10)

# Установка зависимостей из файла requirements.txt
if [ -f "requirements.txt" ]; then
  echo "Установка зависимостей из файла requirements.txt..."
  pwd
  pip install -r requirements.txt
  echo "Зависимости успешно установлены."
else
  echo "Файл requirements.txt не найден. Пропуск установки зависимостей."
fi

# Создание папки data, если она не существует
mkdir -p data

# Скачивание данных
curl -L $(yadisk-direct https://disk.yandex.ru/d/Ihh18yf4807QPA) -o data.zip
curl -L $(yadisk-direct https://disk.yandex.ru/d/OfkV_Ar_1jCIAA) -o models.zip

# Распаковка данных
unzip data.zip -d data
unzip models.zip

# Удаление архива
rm data.zip
rm models.zip
