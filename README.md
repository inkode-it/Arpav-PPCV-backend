# Backend - Piattaforma Proiezioni Climatiche per il Nord-Est

#### Backend - Climate Projections Platform for North-Eastern Italy

[![Piattaforma Proiezioni Climatiche per il Nord-Est](https://github.com/inkode-it/Arpav-PPCV/raw/main/public/img/screenshot.png)](https://clima.arpa.veneto.it/)

## About
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
<br/><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

Commissioned by & Data credits to <br/>
<a href="https://www.arpa.veneto.it/"><img src="https://github.com/inkode-it/Arpav-PPCV/raw/main/public/img/logo_arpav.png" alt="ARPAV" style="background-color:white;padding:4px"></a>

Designed and developed in Italy by <br/>
<a rel="author" href="https://inkode.it"><img src="https://avatars.githubusercontent.com/u/64135645" alt="INKODE soc coop"></a>


# Project
Backend structure for support future climates indicators and models outputs web service pllatform.

# Structure

Docker services:
Django, PostGIS, Redis, a proxy for Threeds and Nginx.

# Create a custom project
Follow the naming conventions for python packages, generally lower case with underscores (_).
In the examples below, replace padoa-backend with whatever you would like to name your project.
No need for a Python virtual environment, the project runs using Docker 

- How to start your server using Docker

You need Docker or Docker-compose, get the latest stable official release for your platform.

## Procedure

1) Prepare the Environment


    git clone https://github.com/inkode-it/Arpav-PPCV-backend`


2) Copy `env.example` in `.env` and **customize it with your local settings**


3) Clone the Frontend repository inside this project and follow the instructions in the README.md file to start the frontend


    `git clone https://github.com/inkode-it/Arpav-PPCV`


4) Run docker-compose to start it up

    ```shell
    docker-compose build --no-cache
    docker-compose up -d
    ```    

5) Build images & start containers:

    `docker-compose up --build -d`


6) Make django migrations: 

    `docker exec -ti backend.api python manage.py makemigrations`


7) Migrate database:

    `docker exec -ti backend.api python manage.py migrate`


8) Create a Super User to access the Django Admin interface:

    `docker exec -ti backend.api python manage.py import_super_user`


9) To create base layer attributes as Variables, Forecast models, Scenario e etc. Run:

    `docker exec -ti backend.api python manage.py import_attributes`


10) To collect all Municipalities (from the geojson) and define geographical boundaries:

     `docker exec -ti backend.api python manage.py import_regions`


11) Scanning selected Threeds folders and copying metadata:

    `docker exec -ti backend.api python manage.py import_layers`

    NOTE: to update already imported layers, run the command with the `--refresh` flag


12) Stop & destroy containers (note using `-v` will remove the volumes)

    `docker-compose down`
