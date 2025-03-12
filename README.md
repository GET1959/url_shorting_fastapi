# fastapi_train_task

Приложение реализовано в соответствии с техзаданием 
https://cloud.5dhub.tech/index.php/apps/onlyoffice/74316?filePath=%2F5DHUB%20(2)%2FWelcome%20Co-Builders%2FWelcome%20tasks%20instructions%2FFastAPI%20training%20task%20Backend.docx

Для запуска приложения необходимо:

1. Создать файл .env в соответствии с образцом .env.sample
2. Запустить контейнер в докере командой: docker-compose up --build -d
3. Применить миграции командой: docker compose exec short_url_task alembic upgrade head
4. Подключиться к базе данных можно, используя переменные из файла .env (host - POSTGRES_HOST, port - POSTGRES_PORT)