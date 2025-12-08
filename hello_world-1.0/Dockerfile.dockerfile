# Използваме официален Python базов образ
FROM python:3.11-slim

# Работна директория вътре в контейнера
WORKDIR /app

# Копираме сорс кода (hello.py) в контейнера
COPY hello_world-1.0/hello.py /usr/local/bin/hello_world

# Указваме entrypoint – какво да се изпълни при стартиране
ENTRYPOINT ["python3", "/usr/local/bin/hello_world"]
