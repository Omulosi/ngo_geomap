**Project**: Geojango NGO Project

**Description**: Displays a geographical mapping of all offices of a fictitious NGO.

## Getting Started

git clone the repo

### Prerequisites

A postgres database is required for development
Install appropriate postgis extension for your postgresql database
Install pipenv using Homebrew, Linuxbrew or pip


**Setting up the database with a user who has all privileges**
```sql
sudo -u postgres psql
postgres=# create database your_database;
postgres=# create user your_username with encrypted password 'your_password';
postgres=# grant all privileges on database your_database to your_username;
```
```
## Running the app

cd into the ngo_geomap folder
```python
cd ngo_geomap/
```

Create a virtual environment
```python
$ python -m venv venv
```

To activate the virtual environment run the command below
```python
$ source venv/bin/activate (linux environment)
```


Run the command to install all requirements from requirements.txt
```python
pip install -r requrements.txt
```


Run the application by starting the server
```python
python manage.py runserver
```

## Sample Home Page
![Alt text](./sample-home-pg.png?raw=true "Home Page Portal")


## Built With

*   [Django](https://www.djangoproject.com/) - Django
*   [GeoDjango](https://docs.djangoproject.com/en/3.1/ref/contrib/gis/) - GeoDjango
*   [Django Leaflet](https://django-leaflet.readthedocs.io/en/latest/) - Django Leaflet
*   Python3

## Author

*   **John Paul**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
