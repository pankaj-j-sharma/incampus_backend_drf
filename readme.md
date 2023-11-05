# setup
user 
    pankajs579
    Qbolbk@123

# cors header configurations
https://github.com/adamchainz/django-cors-headers#configuration

# for removing untracked files 
git rm -rf dashboard/__pycache__/urls.cpython-38.pyc

pip install IndianNameGenerator

https://zetcode.com/python/faker/#:~:text=AdvertisementsFaker,Faker%2C%20and%20by%20Ruby's%20Faker.

# export data from sqlite to be imported to other db
python manage.py dumpdata > incampus_db_data.json

# paytm payment gateway integration try to get the API keys in the incognito window 

# docker commands to run 
docker build -t incampusbackend-api .
docker run -d -p 8080:8000  -v .:/api --name incampus-backed-drf-api incampusbackend-api
