# Задание
Ваш скрипт должен разворачивать ваше приложение используя только docker compose up -d (за исключением использования переменных среды). Это может быть ваш свой проект, его наработки, либо какой-то готовый Docker образ на ваш выбор. Например, можно взять менеджер паролей KeeWeb, который я показывал на прошлом занятии. При использовании своего Docker образа вам нужно также приложить в репозиторий Docker файл.

# Пояснение к решению
Redmine - это issue tracker. Для входа в первый раз по <localhost:3001> логин и пароль: **admin**

Перемные окружения - связь с PostgreSQL
```
  redmine:
    container_name: redmine
    image: redmine:5.1.1
    ports:
      - 3001:3000
    environment:
      REDMINE_DB_POSTGRES: db
      REDMINE_DB_DATABASE: redmine
      REDMINE_DB_USERNAME: root
      REDMINE_DB_PASSWORD: root
    depends_on:
      - db
```
Volume redmine будет создан, если его нет. Иначе - будет использован существующий.

Network имеет драйвер bridge, для возможности взаимодействия между контейнерами в одной сети.
```
volumes:
  redmine:
networks:
  default:
    driver: bridge
```
