# Web application for polls

Application for creating and administering polls

## Project installation procedure

# For development

1. Clone the repository
2. Run the docker-compose file dev.yml
```
docker-compose -f docker-compose.dev.yml up -d
```
3. Create a superuser to enter the admin area
```
docker exec -it poll_app_web_1 python manage.py createsuperuser
```
4. Visit localhost:8000
