
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml rm --force
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d --remove-orphans
docker-compose -f docker-compose.yml restart nginx

#docker logs logging_app
docker logs logging_app_nginx
#docker logs logging_app_db

docker exec -it logging_app bash
