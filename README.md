# IPL Stats
### To install please follow below steps for Django project (You need to activate virtual python env for that first)
1. cd ipl
2. pip install -r requirement.txt
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
6. celery -A ipl.config.celery_app worker -l info

Dependency for django project
1. Memcache server (brew install memcached or sudo apt-get install memcached)
2. Celery

### File update in Backend
Upload depends on celery task please make sure celery is running in background.

*for Match.csv*
Please call this api
url: /api/storage/match/
type: post
data: match_file (give file here)

*for Delivery.csv*
Please call this api
url: /api/storage/delivery/
type: post
data: delivery_file (give file here)


### To install please follow below steps for React project. You need to first update BASE_URL var in *src/constant.ts*
1. cd ipl_client
2. npm i
3. npm start
