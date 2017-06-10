# ServiceServer
Server that use Django Rest Framework provides RESTful services for
Cinema Tickets system. See the details below.

### Installation
* Enviroment

   Python 2.7


   Ubuntu16.04

   
* Install
  ```bash
  $ sudo apt-get install python-pip
  ```
* Use virtualenv to create the virtual enviroment
  ```bash
  $ pip install virtualenv
  ```
    
* Run local
  ```bash
  cd ServiceServer and create the virtual enviroment env
  $ virtualenv env

  active env
  $ source env/bin/active

  install some other needed packages
  $ pip install -r requestments.txt

  run the local server
  $ python manage.py runserver or python manage.py runserver 8001
  ``` 

  Now you can access it by http://localhost:8000 or http://localhost:8001.
     
