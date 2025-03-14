# fastapi_train_task

The application is implemented in accordance with the terms of reference 
https://cloud.5dhub.tech/index.php/apps/onlyoffice/74316?filePath=%2F5DHUB%20(2)%2FWelcome%20Co-Builders%2FWelcome%20tasks%20instructions%2FFastAPI%20training%20task%20Backend.docx

Description of the task
Implement an http service that processes incoming requests. The server starts at http://127.0.0.1:8080 (the default value can be changed).

<details>
<summary> List of possible endpoints (can be changed) </summary>

1. Get an abbreviated version of the transmitted URL.
POST /
The method accepts the URL string for shortening in the request body and returns a response with the code 201.

2. Return the original URL.
GET /<shorten-url-id>
The method takes the identifier of the shortened URL as a parameter and returns a response with the code 307 and the original URL in the Location header.

3. Make an async service request and return the data


To launch the application, you must:

1. Create a file .env according to the sample .env.sample
2. Run the containers in docker with the command: docker-compose up --build -d
3. Apply migrations with the command: docker compose exec short_url_task alembic upgrade head
4. The application will be available at: http://localhost:8080/docs
5. You can connect to the database using variables from the .env file (host - POSTGRES_HOST, port - POSTGRES_PORT)