FROM python:3.11

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Копируйте requirements.txt в контейнер
COPY ./requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте остальные файлы приложения в контейнер
COPY . .

# Запустите приложение
CMD ["python", "dashboard.py"]
