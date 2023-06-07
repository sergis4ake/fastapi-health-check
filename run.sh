docker build -t fastapi-app .
docker run -d -p 8080:8080 --restart=always --name fastapi-app fastapi-app
