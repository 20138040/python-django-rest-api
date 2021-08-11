

    to run the django app using docker
    run command
    -- docker compose-up 

    to create superuser run 
    -- docker-compose  run --rm web ( this is the name of the service) sh -c "python manage.py createsuperuser"


    if want to run without docker 
     1 - install all the pacakges in the requirements.txt 
     
     2 - to run migration
     -- python manage.py migrate  

     3 - to run server
     -- python manage.py runserver 0.0.0.0:8008